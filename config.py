# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("24954614", ""))
API_HASH = getenv("854d71e266722a054d214898c754c70b", "")
BOT_TOKEN = getenv("8008338461:AAHkro3WBkBuyJhnEo-BJHr6kEF8jZ8UwIw", "")
OWNER_ID = list(map(int, getenv("5716292248", "").split()))
MONGO_DB = getenv("mongodb+srv://jeetnarayantiwari5:FGXfMWTnAsaEB4u2@cluster0.2whtu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
LOG_GROUP = getenv("2450739959", "")
CHANNEL_ID = int(getenv("2486152287", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "30"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
