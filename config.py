from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "17694201"))
API_HASH = getenv("API_HASH", "eb8b38c80b362ae8673ac2b59bac17c6")
BOT_TOKEN = getenv("BOT_TOKEN", "5306766511:AAHVWc-nXC1cn8x3a3sg_JjrSmHOqKfDjjE")
SESSION_NAME = getenv("SESSION_NAME", "BABUyLmVKvo58t-ERlmmGvHMZUczLcKSwud8UDfKyh9kLzX4jFRUpEgthR5lBf8OPvljttJ3a8jhcoXgEyz0YvcxAji8IE6kEpyOGTxbyaa2jYIYfZC5ZBpoeGNw7zUAGJglV4CRkNUKmJchKJROVHj9qkx-mA92dUc-O0cCdqIgVUWWIVb1bzJVw8_sZAnbfojboSens6aE9kou_JqyYqWBKZqw4TbPSKlkOvmiPwuN7q-07fErnke7MiXJOyopAKSxpdSfYHylUNInzh2HcF_i95lQ1K7yxAP-8s3e8lwFnQ8tJR2sLthepZbfqih2L8MDY7eqYQy1oizR7XtW9MMeAAAAASq-5kwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "5036835528")
ALIVE_NAME = getenv("ALIVE_NAME", "Oliver")
BOT_USERNAME = getenv("BOT_USERNAME", "NLLNBOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Oliethon/bot")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LLLG_5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ7LZ")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5036835528").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "IIIT2").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
