import os

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEBUG = DEVELOPMENT = not PRODUCTION

FACEBOOK_APP_ID = ""
FACEBOOK_APP_SECRET = ""
FACEBOOK_PAGE_ID = ""
FACEBOOK_PAGE_ACCESS_TOKEN = ""
FACEBOOK_WEBHOOK_VERIFY_TOKEN = "change_this_to_your_own_token"
FACEBOOK_BOT_NAME = ""

