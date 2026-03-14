import os

# Email Configuration for Smart Bank
# On Render: set SMTP_SENDER_EMAIL and SMTP_SENDER_PASSWORD as env vars in the dashboard
# Locally: these fall back to the values below

SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
try:
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
except ValueError:
    SMTP_PORT = 587  # fallback if env var was set incorrectly
SENDER_EMAIL = os.environ.get("SMTP_SENDER_EMAIL", "builtforbank@gmail.com")
SENDER_PASSWORD = os.environ.get("SMTP_SENDER_PASSWORD", "hlhp upfq ufgi qiev")
SMTP_USE_SSL = os.environ.get("SMTP_USE_SSL", "false").lower() == "true"

# Resend API Configuration
# By default, Resend requires a verified domain. 
# RECOMMENDED: verify "buildforbank.com" in Resend dashboard
# RESEND_FROM = "Smart Bank <support@buildforbank.com>"

_RESEND_KEY = os.environ.get("RESEND_API_KEY")
_ON_CLOUD = any(os.environ.get(k) for k in ['RENDER', 'RAILWAY_ENVIRONMENT', 'PORT'])

# Intelligent fallback for RESEND_FROM
# If on cloud and key exists, but no verified sender is set, fallback to onboarding@resend.dev
if _RESEND_KEY and _ON_CLOUD and not os.environ.get("RESEND_FROM"):
    RESEND_FROM = "Smart Bank <onboarding@resend.dev>"
else:
    RESEND_FROM = os.environ.get("RESEND_FROM", f"Smart Bank <{SENDER_EMAIL}>")
