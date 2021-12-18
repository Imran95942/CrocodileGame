from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('1951787106:AAFbVL0eaJha8luz8IjPa8xBaftpoztWBU4')
MONGO_URI = getenv('MONGO_URI')
SUDO_USERS = list(map(int, getenv('isIam07').split()))
