# Copyright (C) 2022 naytseyd <https://github.com/NaytSeyd/KanalEngelleyiciBot>
#
# This file is part of <https://github.com/NaytSeyd/KanalEngelleyiciBot> project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from logging import CRITICAL, INFO, basicConfig, getLogger
from os import environ

from dotenv import load_dotenv
from pyrogram import Client, enums

load_dotenv('config.env')

API_ID = environ.get('API_ID', None)
API_HASH = environ.get('API_HASH', None)
BOT_TOKEN = environ.get('BOT_TOKEN', None)

LOGS = getLogger(__name__)

basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M',
    level=INFO,
)

# https://github.com/TeamDerUntergang/Telegram-SedenUserBot/blob/seden/sedenbot/__init__.py#L94
def set_logger():
    # Turns off out printing Session value
    pyrogram_syncer = getLogger('pyrogram.syncer')
    pyrogram_syncer.setLevel(CRITICAL)

    # Closes some junk outputs
    pyrogram_session = getLogger('pyrogram.session.session')
    pyrogram_session.setLevel(CRITICAL)

    pyrogram_auth = getLogger('pyrogram.session.auth')
    pyrogram_auth.setLevel(CRITICAL)

    asyncio = getLogger('asyncio')
    asyncio.setLevel(CRITICAL)


set_logger()

app = Client(
    name='KanalEngelleyiciBot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, parse_mode=enums.ParseMode.MARKDOWN
)
