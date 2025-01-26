# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("", ""))
API_HASH = getenv("", "")
BOT_TOKEN = getenv("", "")
OWNER_ID = list(map(int, getenv("5716292248", "").split()))
MONGO_DB = getenv("", "")
LOG_GROUP = getenv("2450739959", "")
CHANNEL_ID = int(getenv("2486152287", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "30"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
