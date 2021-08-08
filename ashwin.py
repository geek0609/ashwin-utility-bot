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


BOT_API = os.environ.get("BOT_API")

bot = Bot(BOT_API)
updater = Updater(BOT_API, use_context=True, workers=128)
dispatcher = updater.dispatcher

