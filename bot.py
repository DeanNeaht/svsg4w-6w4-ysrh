# -*- coding: utf-8 -*-

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from config import TOKEN, admin_id
from messages import start_message, help_message, opros_message, game_message, freelance_message
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Я родилсяяя!!!")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message, reply_markup=kb.markup3)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message, reply_markup=kb.markup3)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    if message.text == "Платные опросы":
        keyboard = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="Анкетка.ру", url="https://www.anketka.ru/referral/6869423")
        url_button2 = types.InlineKeyboardButton(text="You think", url="https://youthink.io/?source=e3L1m9__kk")
        url_button3 = types.InlineKeyboardButton(text="Мое мнение", url="https://www.moemnenie.ru/f/11156912")
        keyboard.add(url_button1).add(url_button2).add(url_button3)
        await message.reply(opros_message, reply_markup=keyboard)
    elif message.text == "Для мобильного телефона":
        keyboard_1 = types.InlineKeyboardMarkup()
        url_button4 = types.InlineKeyboardButton(text="Apperwall", url="https://apperwall.com/?p=2DdEhKcy")
        url_button5 = types.InlineKeyboardButton(text="Advertapp на Android", url="http://go.advertapp.net/4a8qq5")
        url_button6 = types.InlineKeyboardButton(text="PayForInstall на Android", url="https://play.google.com/store/apps/details?id=melchindmitry.oncreate.pfi")
        url_button7 = types.InlineKeyboardButton(text="PayForInstall на iOS", url="https://apps.apple.com/ru/app/pfi/id1450915982")
        keyboard_1.add(url_button4).add(url_button5).add(url_button6).add(url_button7)
        await message.reply(game_message, reply_markup=keyboard_1)
    elif message.text == "Фриланс":
        keyboard_2 = types.InlineKeyboardMarkup()
        url_button8 = types.InlineKeyboardButton(text="Advego", url="https://advego.com/8XgEQdtkrk")
        url_button9 = types.InlineKeyboardButton(text="Work-zilla", url="https://work-zilla.com/?ref=1436000")
        url_button10 = types.InlineKeyboardButton(text="FL.ru", url="https://www.fl.ru/projects/?ref=158503")
        keyboard_2.add(url_button8).add(url_button9).add(url_button10)
        await message.reply(freelance_message, reply_markup=keyboard_2)
    else:
        await message.reply('Я тебя не понимаю. Напиши /help.')



