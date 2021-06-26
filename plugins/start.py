#(©)Codexbotz

import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages, get_messages_ip

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(argument[1])
                end = int(argument[2])
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
            try:
                messages = await get_messages(client, ids)
            except:
        elif len(argument) == 2:
            try:
                ids = [int(argument[1])]
                messages = await get_messages_ip(client, ids)
            except:
                return
        elif len(argument) == 4:
            try:
                ids = [int(argument[1])]
                messages = await get_messages(client, ids)
            except:
                return
        temp_msg = await message.reply("😊 කරුණාකර මදක් ‍රැඳී සිටින්න...")
        try:
            await message.reply_text(ADVERT_TEXT)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None
                caption_new = caption.replace("@WMR_", "").replace("@gatayaofficialnew", "").replace("@gatayaofficial", "").replace("@gataya", "").replace("@MovieWorld2000", "").replace("@MovieWorld2001", "").replace("@cinemahubsl", "").replace("@WEB_SERIES_SL", "").replace("@CC_New", "").replace("@iMediaShare", "").replace("@TvSeriesBay", "").replace("@CC_ALL", "").replace("@CC_X265", "").replace("@x265SL", "").replace("@CC", "").replace("@GlinkZ", "").replace("@GlinkZFilms", "").replace("@GlinkZGroup", "").replace("@GlinkZmovies", "").replace("@BM_Links", "").replace("@RickyChannel", "").replace("@Dramaost", "").replace("@lubokvideo", "")

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption_new, parse_mode = 'html', reply_markup = reply_markup)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption_new, parse_mode = 'html', reply_markup = reply_markup)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = "<b>📌මගෙන් Film ගන්න නම් ඔයා අපේ Channel එකට Join වෙලා ඉන්න ඕනි.\n📌You need to join in my Channel to use me.\n\n⏳පහල Button එක Click කරල Channel එකට Join වෙන්න.\n⏳Kindly Please join Channel</b>\n\n😇Join වුනාට පස්සෙ පහල 'තියන Try Again' උඩ Click කරන්න. ඔයාට Film එක ලැබෙයි.\nAfter Join to Channel hit on 'Try Again' Text to Get Movie"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>\n\n<a href='https://t.me/{client.username}?start={argument}'>👍🏽 Try Again 🔗</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🇱🇰 Join Channel❗️", url = client.invitelink)]])
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )
