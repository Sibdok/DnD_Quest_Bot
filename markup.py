import telebot
from messages import *
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *


bot = telebot.TeleBot(TOKEN)



# Маркапы
markup1 = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton("Согласиться", callback_data='Согласится')
item2 = types.InlineKeyboardButton("Отказать", callback_data='Отказать')
markup1.add(item1, item2)

markup2 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить')
markup2.add(item1)

markup3 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_2')
markup3.add(item1)

markup4 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_3')
markup4.add(item1)

markup5 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_4')
markup5.add(item1)

markup6 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_5')
markup6.add(item1)

markup7 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_6')
markup7.add(item1)

markup8 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_7')
markup8.add(item1)

markup9 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_8')
markup9.add(item1)

markup10 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_9')
markup10.add(item1)

markup11 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_10')
markup11.add(item1)

markup12 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_11')
markup12.add(item1)

markup13 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_12')
markup13.add(item1)

markup14 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Начать бой", callback_data='Начать_бой')
item2 = types.InlineKeyboardButton("Попробовать договориться", callback_data='Попробовать_договориться')
markup14.add(item1, item2)

markup15 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_13')
markup15.add(item1)

markup16 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_14')
markup16.add(item1)

markup17 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_15')
markup17.add(item1)

markup18 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_16')
markup18.add(item1)

markup19 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Продолжить", callback_data='Продолжить_17')
markup19.add(item1)

markup20 = types.InlineKeyboardMarkup(row_width=1)
item1 = types.InlineKeyboardButton("Согласиться и спрятать", callback_data='Согласится_2')
item2 = types.InlineKeyboardButton("Отказать и уничтожить", callback_data='Отказать_2')
markup20.add(item1, item2)
