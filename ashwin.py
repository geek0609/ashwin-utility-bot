#!/usr/bin/env python
#
# Copyright (C) 2021 Ashwin DS <astroashwin@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
import random
import time
from telegram import *
from telegram.ext import *
import requests
import json
import asyncio
import zipfile

BOT_API = os.environ.get("BOT_API")

bot = Bot(BOT_API)
updater = Updater(BOT_API, use_context=True, workers=128)
dispatcher = updater.dispatcher


def dump(url, file):
    print (file)
    r = requests.get(url, allow_redirects=True)
    filename = url.rsplit("/", 1)[1]
    print(filename)
    open(filename, "wb").write(r.content)
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall("dump")


def start_fun(update: Update, context: CallbackContext):
    while True:
        try:
            message_sent = bot.send_message(chat_id=update.effective_chat.id,
                                            text="Hey there, I am not ded (yet)",
                                            reply_to_message_id=update.message.message_id)
            break
        except Exception as e:
            print(e)


def help_fun(update: Update, context: CallbackContext):
    message = "How about no?"
    while True:
        try:
            message_sent = bot.send_message(disable_web_page_preview=True, parse_mode="MARKDOWN",
                                            chat_id=update.effective_chat.id,
                                            text=message, reply_to_message_id=update.message.message_id, )
            break
        except Exception as e:
            print(e)


def dump_fun(update: Update, context: CallbackContext):
    url = update.message.text.replace("/dump ", "")
    message_sent = bot.send_message(disable_web_page_preview=True, parse_mode="HTML", chat_id=update.effective_chat.id,
                                    text="You have given this link : " + url,
                                    reply_to_message_id=update.message.message_id, )
    time.sleep(1)
    bot.edit_message_text(text="Working on it....",chat_id = update.effective_chat.id, message_id = message_sent.message_id)
    time.sleep(1)
    dump(url.rsplit(' ')[0], url.rsplit(' ')[1])
    bot.edit_message_text(text="Done", chat_id=update.effective_chat.id,
                          message_id=message_sent.message_id)


start_command = CommandHandler("start", start_fun, run_async=True)
help_command = CommandHandler("help", help_fun, run_async=True)
dump_command = CommandHandler("dump", dump_fun, run_async=True)

dispatcher.add_handler(start_command)
dispatcher.add_handler(help_command)
dispatcher.add_handler(dump_command)
updater.start_polling()
