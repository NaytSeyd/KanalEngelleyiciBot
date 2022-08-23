# Copyright (C) 2022 naytseyd <https://github.com/NaytSeyd/KanalEngelleyiciBot>
#
# This file is part of <https://github.com/NaytSeyd/KanalEngelleyiciBot> project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from platform import python_version

from pyrogram import __version__, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from client import LOGS, app


# Kanal olarak mesaj gönderenleri yasaklar ve mesajı siler
# Tartışma kanalını etkilemez
@app.on_message(filters.group)
async def block_channels(client, message):
    chat = message.chat
    msg_channel = message.sender_chat
    get_chat = await client.get_chat(chat.id)
    if (
        msg_channel
        and get_chat.linked_chat
        and get_chat.linked_chat.id != msg_channel.id
        and str(msg_channel.id).startswith('-100')
    ):
        await client.delete_messages(chat.id, message.id)
        await chat.ban_member(msg_channel.id)


@app.on_message(filters.command(['start', 'help'], ['/', '!']) & filters.private)
async def start_message(client, message):
    me = await client.get_me()
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text='👨🏻‍💻 Yapımcım', url='https://t.me/NightShade'
                ),
                InlineKeyboardButton(
                    text='Beni grubuna ekle',
                    url=f'https://t.me/{me.username}?startgroup=new',
                ),
            ]
        ]
    )
    return await message.reply(
        'Merhaba! Ben, gruplarınızda yazan kanalları engelleyebiliyorum.\nBeni grubunuza ekleyerek çalışmamı sağlayabilirsiniz.',
        reply_markup=keyboard,
    )


@app.on_message(filters.new_chat_members, group=1)
async def welcome_message(client, message):
    me = await client.get_me()
    for user in message.new_chat_members:
        if user.id == me.id:
            return await message.reply('Beni gruba eklediğiniz için teşekkürler!')


app.start()
LOGS.info(
    f'\n\nBot aktif!\nPython {python_version()}\nPyrogram {__version__}\nhttps://github.com/naytseyd\n'
)
idle()
app.stop()
LOGS.info('Bot kapatıldı!')
