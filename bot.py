import telebot
from info import *
from markup import *
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json



bot = telebot.TeleBot(TOKEN)

users = {}
# Переменные

user_id = None

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Начать игру')


# Старт
@bot.message_handler(commands=["start"])
def welcome(message):
    global user_id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Приветствую, {user_name}! Это текстовая (и не только) игра в стиле D&D!", reply_markup=keyboard1)
    cell = ""
    users[user_id] = cell
    with open('dnd_bot_users.json', 'w') as file:
        json.dump(users, file, indent=4)
    return user_id and users


# Текст
@bot.message_handler(content_types=["text"])
def send_text(message):
    global user_id
    global mes
    if user_id in users:
        if message.text.lower() == "начать игру":
              mes = bot.send_message(message.chat.id, "Хорошо!", reply_markup=markup2)
              users[user_id]  = "start"
        else:
            bot.send_message(message.chat.id, "Я вас не понимаю!")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global user_id
    global mes
    # События в таверне
    def in_the_tavern(call):
        if call.data == 'Продолжить' and users[user_id] == "start":
            global photo_1
            global message_1
            bot.delete_message(call.from_user.id, mes.message_id)
            photo_1 = bot.send_photo(call.message.chat.id, photo=open('photos/photo1.png', 'rb'))
            message_1 = bot.send_message(call.message.chat.id, message_text_1, reply_markup=markup3)
            users[user_id] = "in_the_tavern"
        elif call.data == 'Продолжить_2' and users[user_id] == "in_the_tavern":
            global photo_2
            global message_2
            bot.delete_message(call.from_user.id, photo_1.message_id)
            bot.delete_message(call.from_user.id, message_1.message_id)
            photo_2 = bot.send_photo(call.message.chat.id, photo=open('photos/photo2.png', 'rb'))
            message_2 = bot.send_message(call.message.chat.id, message_text_2, reply_markup=markup4)
            users[user_id] = "in_the_tavern_2"
        elif call.data == 'Продолжить_3' and users[user_id] == "in_the_tavern_2":
            global photo_3
            global message_3
            bot.delete_message(call.from_user.id, photo_2.message_id)
            bot.delete_message(call.from_user.id, message_2.message_id)
            photo_3 = bot.send_photo(call.message.chat.id, photo=open('photos/photo3.png', 'rb'))
            message_3 = bot.send_message(call.message.chat.id, message_text_3, reply_markup=markup5)
            users[user_id] = "in_the_tavern_3"
        elif call.data == 'Продолжить_4' and users[user_id] == "in_the_tavern_3":
            global message_4
            message_4 = bot.edit_message_text(message_text_4, call.from_user.id, message_3.message_id, reply_markup=markup6)
            users[user_id] = "in_the_tavern_4"
        elif call.data == 'Продолжить_5' and users[user_id] == "in_the_tavern_4":
            global photo_4
            global message_5
            bot.delete_message(call.from_user.id, photo_3.message_id)
            bot.delete_message(call.from_user.id, message_4.message_id)
            photo_4 = bot.send_photo(call.message.chat.id, photo=open('photos/photo4.png', 'rb'))
            message_5 = bot.send_message(call.message.chat.id, message_text_5, reply_markup=markup7)
            users[user_id] = "in_the_tavern_5"
        
        elif call.data == 'Продолжить_6' and users[user_id] == "in_the_tavern_5":
            global message_6
            message_6 = bot.edit_message_text(message_text_6, call.from_user.id, message_5.message_id, reply_markup=markup1)
            users[user_id] = "in_the_tavern_6"
        
        elif call.data == 'Согласится' and users[user_id] == "in_the_tavern_6":
            global message_7
            message_7 = bot.edit_message_text(message_text_7_1, call.from_user.id, message_6.message_id, reply_markup=markup8)
            users[user_id] = "in_the_tavern_7_and_agree"

            
        elif call.data == 'Отказать' and users[user_id] == "in_the_tavern_6":
            message_7 = bot.edit_message_text(message_text_7_2, call.from_user.id, message_6.message_id, reply_markup=markup8)
            users[user_id] = "in_the_tavern_7_and_deny"
        
        elif call.data == 'Продолжить_7' and (users[user_id] == "in_the_tavern_7_and_agree" or users[user_id] == "in_the_tavern_7_and_deny"):
            global photo_5
            global message_8
            bot.delete_message(call.from_user.id, photo_4.message_id)
            bot.delete_message(call.from_user.id, message_7.message_id)
            photo_5 = bot.send_photo(call.message.chat.id, photo=open('photos/photo5.png', 'rb'))
            message_8 = bot.send_message(call.message.chat.id, message_text_8, reply_markup=markup9)
        
        def first_agree(call):
            if call.data == 'Продолжить_8' and users[user_id] == "in_the_tavern_7_and_agree":
                global photo_6
                global message_9
                bot.delete_message(call.from_user.id, photo_5.message_id)
                bot.delete_message(call.from_user.id, message_8.message_id)
                photo_6 = bot.send_photo(call.message.chat.id, photo=open('photos/photo6.png', 'rb'))
                message_9 = bot.send_message(call.message.chat.id, message_text_9, reply_markup=markup10)
                users[user_id] = "way_to_the_forest_1_and_agree"
        
        def first_deny(call):
            global photo_6
            global message_9
            if call.data == 'Продолжить_8' and users[user_id] == "in_the_tavern_7_and_deny":
                bot.delete_message(call.from_user.id, photo_5.message_id)
                bot.delete_message(call.from_user.id, message_8.message_id)
                photo_6 = bot.send_photo(call.message.chat.id, photo=open('photos/photo7.png', 'rb'))
                message_9 = bot.send_message(call.message.chat.id, message_text_10, reply_markup=markup10)
                users[user_id] = "way_to_the_forest_1_and_deny"


        first_agree(call)
        first_deny(call)
    in_the_tavern(call)
    
    # События в лесу
    
    def in_the_forest(call):
        def forest_and_agree(call):
            if call.data == 'Продолжить_9' and users[user_id] == "way_to_the_forest_1_and_agree":
                global message_10
                global photo_7
                bot.delete_message(call.from_user.id, photo_6.message_id)
                bot.delete_message(call.from_user.id, message_9.message_id)
                photo_7 = bot.send_photo(call.message.chat.id, photo=open('photos/photo8.png', 'rb'))
                message_10 = bot.send_message(call.message.chat.id, message_text_11, reply_markup=markup11)
                users[user_id] = "way_to_the_forest_2_and_agree"
            
            elif call.data == 'Продолжить_10' and users[user_id] == "way_to_the_forest_2_and_agree":
                global message_11
                global photo_8
                bot.delete_message(call.from_user.id, photo_7.message_id)
                bot.delete_message(call.from_user.id, message_10.message_id)
                photo_8 = bot.send_photo(call.message.chat.id, photo=open('photos/photo9.png', 'rb'))
                message_11 = bot.send_message(call.message.chat.id, message_text_12, reply_markup=markup12)
                users[user_id] = "way_to_the_forest_3_and_agree"

            elif call.data == 'Продолжить_11' and users[user_id] == "way_to_the_forest_3_and_agree":
                global message_12
                global photo_9
                bot.delete_message(call.from_user.id, photo_8.message_id)
                bot.delete_message(call.from_user.id, message_11.message_id)
                photo_9 = bot.send_photo(call.message.chat.id, photo=open('photos/photo11.png', 'rb'))
                message_12 = bot.send_message(call.message.chat.id, message_text_18, reply_markup=markup15)
                users[user_id] = "way_to_the_forest_4_and_agree"
            
            elif call.data == 'Продолжить_13' and users[user_id] == "way_to_the_forest_4_and_agree":
                global message_13
                global photo_10
                bot.delete_message(call.from_user.id, photo_9.message_id)
                bot.delete_message(call.from_user.id, message_12.message_id)
                photo_10 = bot.send_photo(call.message.chat.id, photo=open('photos/photo12.png', 'rb'))
                message_13 = bot.send_message(call.message.chat.id, message_text_19, reply_markup=markup16)
                users[user_id] = "way_to_the_forest_5_and_agree"

            elif call.data == 'Продолжить_14' and users[user_id] == "way_to_the_forest_5_and_agree":
                global message_14
                global photo_11
                bot.delete_message(call.from_user.id, photo_10.message_id)
                bot.delete_message(call.from_user.id, message_13.message_id)
                photo_11 = bot.send_photo(call.message.chat.id, photo=open('photos/photo13.png', 'rb'))
                message_14 = bot.send_message(call.message.chat.id, message_text_20, reply_markup=markup17)
                users[user_id] = "way_to_the_forest_6_and_agree"

        def forest_and_deny(call):
            if call.data == 'Продолжить_9' and users[user_id] == "way_to_the_forest_1_and_deny":
                global message_10
                global photo_7
                bot.delete_message(call.from_user.id, photo_6.message_id)
                bot.delete_message(call.from_user.id, message_9.message_id)
                photo_7 = bot.send_photo(call.message.chat.id, photo=open('photos/photo8.png', 'rb'))
                message_10 = bot.send_message(call.message.chat.id, message_text_11, reply_markup=markup11)
                users[user_id] = "way_to_the_forest_2_and_deny"
            
            elif call.data == 'Продолжить_10' and users[user_id] == "way_to_the_forest_2_and_deny":
                global message_11
                global photo_8
                bot.delete_message(call.from_user.id, photo_7.message_id)
                bot.delete_message(call.from_user.id, message_10.message_id)
                photo_8 = bot.send_photo(call.message.chat.id, photo=open('photos/photo9.png', 'rb'))
                message_11 = bot.send_message(call.message.chat.id, message_text_13, reply_markup=markup12)
                users[user_id] = "way_to_the_forest_3_and_deny"

            elif call.data == 'Продолжить_11' and users[user_id] == "way_to_the_forest_3_and_deny":
                global message_12
                global photo_9
                bot.delete_message(call.from_user.id, photo_8.message_id)
                bot.delete_message(call.from_user.id, message_11.message_id)
                photo_9= bot.send_photo(call.message.chat.id, photo=open('photos/photo10.png', 'rb'))
                message_12 = bot.send_message(call.message.chat.id, message_text_14, reply_markup=markup13)
                users[user_id] = "way_to_the_forest_4_and_deny"
            
            elif call.data == 'Продолжить_12' and users[user_id] == "way_to_the_forest_4_and_deny":
                global message_13
                global photo_10
                global message_14
                global photo_11
                bot.delete_message(call.from_user.id, photo_9.message_id)
                bot.delete_message(call.from_user.id, message_12.message_id)
                photo_10= bot.send_photo(call.message.chat.id, photo=open('photos/photo9.png', 'rb'))
                message_13 = bot.send_message(call.message.chat.id, message_text_15, reply_markup=markup14)
                users[user_id] = "way_to_the_forest_5_and_deny"

            elif call.data == 'Начать_бой' and users[user_id] == "way_to_the_forest_5_and_deny":
                bot.delete_message(call.from_user.id, photo_10.message_id)
                bot.delete_message(call.from_user.id, message_13.message_id)
                photo_11= bot.send_photo(call.message.chat.id, photo=open('photos/photo9.png', 'rb'))
                message_14 = bot.send_message(call.message.chat.id, message_text_16)
                users[user_id] = "way_to_the_forest_6_and_deny"

            elif call.data == 'Попробовать_договориться' and users[user_id] == "way_to_the_forest_5_and_deny":
                bot.delete_message(call.from_user.id, photo_10.message_id)
                bot.delete_message(call.from_user.id, message_13.message_id)
                photo_11= bot.send_photo(call.message.chat.id, photo=open('photos/photo9.png', 'rb'))
                message_14 = bot.send_message(call.message.chat.id, message_text_17)
                users[user_id] = "way_to_the_forest_6_and_deny"
        
        forest_and_agree(call)
        forest_and_deny(call)
    
    # События в городе
    def in_the_town(call):
        if call.data == 'Продолжить_15' and users[user_id] == "way_to_the_forest_6_and_agree":
            global message_15
            global photo_12
            bot.delete_message(call.from_user.id, photo_11.message_id)
            bot.delete_message(call.from_user.id, message_14.message_id)
            photo_12 = bot.send_photo(call.message.chat.id, photo=open('photos/photo14.png', 'rb'))
            message_15 = bot.send_message(call.message.chat.id, message_text_21, reply_markup=markup18)
            users[user_id] = "in_the_town_1"

        elif call.data == 'Продолжить_16' and users[user_id] == "in_the_town_1":
            global message_16
            global photo_13
            bot.delete_message(call.from_user.id, photo_12.message_id)
            bot.delete_message(call.from_user.id, message_15.message_id)
            photo_13 = bot.send_photo(call.message.chat.id, photo=open('photos/photo15.png', 'rb'))
            message_16 = bot.send_message(call.message.chat.id, message_text_22, reply_markup=markup19)
            users[user_id] = "in_the_town_2"

        elif call.data == 'Продолжить_17' and users[user_id] == "in_the_town_2":
            global message_17
            global photo_14
            bot.delete_message(call.from_user.id, photo_13.message_id)
            bot.delete_message(call.from_user.id, message_16.message_id)
            photo_14 = bot.send_animation(call.message.chat.id, open('photos/gif16.gif', 'rb'))
            message_17 = bot.send_message(call.message.chat.id, message_text_23, reply_markup=markup20)
            users[user_id] = "in_the_town_3"
        

        def in_the_town_and_agree(call):
            if call.data == 'Согласится_2' and users[user_id] == "in_the_town_3":
                global message_18
                global photo_15
                global message_19
                bot.delete_message(call.from_user.id, photo_14.message_id)
                bot.delete_message(call.from_user.id, message_17.message_id)
                photo_15 = bot.send_photo(call.message.chat.id, photo=open('photos/photo20.png', 'rb'))
                message_18 = bot.send_message(call.message.chat.id, message_text_26)
                message_19 = bot.send_message(call.message.chat.id, message_text_27)
                users[user_id] = "in_the_town_3_and_agree"
            
        
        def in_the_town_and_deny(call):
            if call.data == 'Отказать_2' and users[user_id] == "in_the_town_3":
                global message_18
                global message_19
                global photo_15
                bot.delete_message(call.from_user.id, photo_14.message_id)
                bot.delete_message(call.from_user.id, message_17.message_id)
                photo_15 = bot.send_photo(call.message.chat.id, photo=open('photos/photo19.png', 'rb'))
                message_18 = bot.send_message(call.message.chat.id, message_text_24)
                message_19 = bot.send_message(call.message.chat.id, message_text_25)
                users[user_id] = "in_the_town_3_and_deny"
        
        in_the_town_and_deny(call)
        in_the_town_and_agree(call)

    in_the_town(call)
    in_the_forest(call)


bot.polling(non_stop=True)