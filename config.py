import os
from dotenv import load_dotenv

load_dotenv(override=False)

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OWNER_ID = os.getenv('OWNER_ID')

COMMAND_PREFIX = "!"