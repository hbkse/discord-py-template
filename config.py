import os
from dotenv import load_dotenv

load_dotenv(override=False)

DISCORD_BOT_TOKEN: str = os.getenv('DISCORD_BOT_TOKEN')
OWNER_ID: int = int(os.getenv('OWNER_ID'))
TESTING_GUILD_ID: int = int(os.getenv('TESTING_GUILD_ID'))

COMMIT_HASH: str = os.getenv('COMMIT_HASH') or 'local'

COMMAND_PREFIX: str = "!"