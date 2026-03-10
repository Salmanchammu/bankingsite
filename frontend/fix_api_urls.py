import os
import glob
import re

target_dir = 'c:/Users/salma/Downloads/smart-bank-v2-FIXED/smartbank_v2/frontend'
files_to_fix = glob.glob(os.path.join(target_dir, '*.js')) + glob.glob(os.path.join(target_dir, '*.html'))

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it's a dash script, replace all fetches
    if filename.endswith('staffdash.js') or filename.endswith('admindash.js'):
        if 'const API =' not in content:
            content = "const API = window.SMART_BANK_API_BASE || 'http://localhost:5001/api';\n\n" + content
        content = content.replace("'http://localhost:5001/api", "API + '")
        content = content.replace("`http://localhost:5001/api", "`${API}")
    
    # Handled separately: face-auth and others
    if filename.endswith('face-auth-fixed.js') or filename.endswith('staff-auth.js'):
        if 'const API =' not in content:
            content = "const API = window.SMART_BANK_API_BASE || 'http://localhost:5001/api';\n" + content
        content = content.replace("'http://localhost:5001/api", "API + '")
        content = content.replace("`http://localhost:5001", "`${API.replace('/api','')}") # for the endpoints that omit /api

    if filename.endswith('userdash.js') or filename.endswith('chatbot.js') or filename.endswith('reset-password.html') or filename.endswith('forgot-password.html'):
        content = content.replace("= 'http://localhost:5001/api'", "= window.SMART_BANK_API_BASE || 'http://localhost:5001/api'")
        
    if filename.endswith('staff.html'):
        # There's a login fetch
        content = content.replace("'http://localhost:5001/api", "(window.SMART_BANK_API_BASE || 'http://localhost:5001/api') + '")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
for f in files_to_fix:
    fix_file(f)

print("Files Fixed!")
