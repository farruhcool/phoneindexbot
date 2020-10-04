import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN ="1256541898:AAE5-vJEBOSFJsLkN0QwhYB8EgXcyqS-yzQ"
admins = [
    81039470
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
