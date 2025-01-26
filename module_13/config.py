import os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv('TELEGRAM_BOT_TOKEN')

price = {
    'medium': 1500,
    'large': 2000,
    'extra-large': 3000,
}
