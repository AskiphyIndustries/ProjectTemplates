import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.DB_FILE = os.getenv("DB_FILE")
        self.BOT_OWNER = os.getenv("BOT_OWNER")