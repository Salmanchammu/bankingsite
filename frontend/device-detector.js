/**
 * Smart Bank - Device Detector Utility
 * Silently detects if the user is on a mobile or desktop device.
 */
(function () {
    window.SmartBankDeviceDetector = {
        getDeviceType: function () {
            const ua = navigator.userAgent;
            if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
                return "tablet";
            }
            if (/Mobile|Android|iP(hone|od)|IEMobile|BlackBerry|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)) {
                return "mobile";
            }
            return "desktop";
        },

        // Helper to get formatted device info for logging
        getDeviceInfo: function () {
            return {
                type: this.getDeviceType(),
                platform: navigator.platform,
                userAgent: navigator.userAgent,
                screen: `${window.screen.width}x${window.screen.height}`
            };
        }
    };

    console.log("Device detector initialized: ", window.SmartBankDeviceDetector.getDeviceType());
})();
