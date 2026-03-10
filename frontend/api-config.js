/**
 * Smart Bank - API Configuration
 * Dynamically determines the backend API base URL based on the current hostname.
 * This allows the app to work on localhost, local IP, or production domains.
 */

const getApiBase = () => {
    const hostname = window.location.hostname;
    const isLocal = !hostname || hostname === 'localhost' || hostname === '127.0.0.1' ||
        hostname.startsWith('192.168.') || hostname.startsWith('10.');

    if (isLocal) {
        // Use the current hostname/IP but port 5000
        const host = hostname || 'localhost';
        return `http://${host}:5000/api`;
    }
    return window.location.origin + '/api';
};

const API_BASE_URL = getApiBase();


// Export for use in modules if needed, or just keep as global
window.SMART_BANK_API_BASE = API_BASE_URL;
console.log('API Base URL configured as:', window.SMART_BANK_API_BASE);

// --- GLOBAL FETCH INTERCEPTOR ---
// Monkey-patch window.fetch to provide systemic fixes for all requests
const originalFetch = window.fetch;

window.fetch = async function (url, options) {
    if (!options) options = {};
    if (!options.headers) options.headers = {};

    // 1. TUNNEL BYPASS
    // Adds the Bypass-Tunnel-Reminder header for Localtunnel/Ngrok
    const hostname = window.location.hostname;
    const isLocal = !hostname || hostname === 'localhost' || hostname === '127.0.0.1';
    if (!isLocal) {
        if (options.headers instanceof Headers) {
            options.headers.append('Bypass-Tunnel-Reminder', 'true');
        } else {
            options.headers['Bypass-Tunnel-Reminder'] = 'true';
        }
    }

    // 2. CREDENTIALS ENFORCEMENT
    // Force credentials: 'include' for all internal API calls.
    // This is CRITICAL for session persistence across different ports/origins.
    const isInternalAPI = typeof url === 'string' && (url.includes(':5000/api') || url.includes('/api/'));
    if (isInternalAPI) {
        options.credentials = 'include';
    }

    try {
        const response = await originalFetch(url, options);

        // 3. UNAUTHORIZED (401) HANDLING
        // Skip 401 redirection if the request was to a login or auth-check endpoint
        const isAuthEndpoint = typeof url === 'string' && (
            url.includes('/login') ||
            url.includes('/signup') ||
            url.includes('/register') ||
            url.includes('/face/') ||
            url.includes('/auth/check')
        );

        if (response.status === 401 && !isAuthEndpoint) {
            console.warn('API returned 401 Unauthorized. Redirecting to login...');

            // Clear all auth data to be sure
            localStorage.removeItem('user');
            localStorage.removeItem('staff');
            localStorage.removeItem('admin');
            localStorage.removeItem('token');

            // Prevent redirect loop if already on login page
            const path = window.location.pathname;
            if (!path.includes('user.html') && !path.includes('staff.html') && !path.includes('mobile-auth.html')) {
                if (path.includes('mobile-')) {
                    window.location.href = 'mobile-auth.html';
                } else {
                    window.location.href = 'user.html';
                }
            }
        }
        return response;
    } catch (error) {
        throw error;
    }
};

console.log('✓ Global Fetch Interceptor active');
