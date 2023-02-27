from telebot import TeleBot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from sqlite3 import connect

token = "Your token"
bot = TeleBot(token)
news_type = 0
news_types = ["1","2","3","4","5","6","7"]

conn = connect("./bot_users.db", check_same_thread=False)
cur = conn.cursor()

def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS Users_data(
                first_name,
                last_name,
                age,
                news_type,
                country,                                                    
                chat_id
            )""")                                                   # creates 2 tables in bot_users.db
    cur.execute("""CREATE TABLE IF NOT EXISTS Stop_list(
                chat_ids
    )""")

def stop_list():
    cur.execute("""SELECT chat_ids FROM Stop_list""")               # getting ids of people that do not want receiving news anymore
    stop_list = cur.fetchall()
    return stop_list

def chat_ids():
    cur.execute("""SELECT chat_id FROM Users_data""")
    chat_ids = cur.fetchall()                                       # get chat ids all registered users 
    return chat_ids

############################################################## Commands ######################################################################################

@bot.message_handler(commands=['start'])
def launch(message):
    id = message.chat.id
    bot.send_message(id, f"Hey {message.chat.first_name}, nice to see you here, I'm a newsletter bot.\nNews comes every 4 hours"
        "\nI have three types of news: sports (NBA), crypto news," 
        "politics\nTo select the type of news, enter one of the following options:\n1. Sports (NBA)\n2. Crypto news"
        "\n3. Politics\n4. Sports (NBA) + crypto news\n5. Sports (NBA) + politics\n6. Crypto news + politics\n7. All news")
    
    choice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    choice.row("1", "2", "3", "4", "5", "6", "7")
    bot.send_message(id, "Please provide your choice", reply_markup=choice)


@bot.message_handler(commands=['stop'])
def stop(message):
    id = message.chat.id
    
    if (f"{id}",) not in stop_list(): 
        options_menu = InlineKeyboardMarkup()
        option1 = InlineKeyboardButton(text="yes", callback_data="Stop the bot")
        option2 = InlineKeyboardButton(text="no", callback_data="Dont`t stop the bot")
        options_menu.add(option1, option2)
        bot.send_message(id, "Are you sure you want to stop the bot?", reply_markup=options_menu)
    else:
        bot.send_message(id, "At the moment you do not receive news, if you would like to continue receiving news type /resume command")


@bot.message_handler(commands=['resume'])
def resume(message):
    id = message.chat.id
    
    if (f"{id}",) in stop_list():
        options_menu = InlineKeyboardMarkup()
        option1 = InlineKeyboardButton(text="yes", callback_data="Restart the bot")
        option2 = InlineKeyboardButton(text="no", callback_data="Dont`t restart the bot")
        options_menu.add(option1, option2)
        bot.send_message(id, "Do you want to start receiving news again?", reply_markup=options_menu)
    else:
        bot.send_message(id, "You are currently receiving news, if you want to stop that, type /stop command")

@bot.message_handler(commands=['support'])
def support(message):
    id = message.chat.id
    
    reasons_menu = InlineKeyboardMarkup()
    reason1 = InlineKeyboardButton(text="Complaints", callback_data="Support")
    reason2 = InlineKeyboardButton(text="Suggestions for improving the bot", callback_data="Support")
    reason3 = InlineKeyboardButton(text="Other questions", callback_data="Support")
    reasons_menu.add(reason1, reason2, reason3)
    bot.send_message(id, "Select the reason for contacting technical support", reply_markup=reasons_menu)
    


###############################################################################################################################################

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    
    if call.data == "Stop the bot":
        bot.send_message(call.from_user.id, "Ok, i got you, if you would like to continue receiving news, type /resume command")
        cur.execute(f"""INSERT INTO Stop_list (chat_ids)
                        VALUES("{call.from_user.id}")""")
        conn.commit()

    elif call.data == "Dont`t stop the bot":
        bot.send_message(call.from_user.id, "Thank you for staying with me")
    
    elif call.data == "Restart the bot":
        bot.send_message(call.from_user.id, "Cool that you are again with me, hope you are enjoying while using the bot)")
        cur.execute(f"""DELETE FROM Stop_list
                        WHERE chat_ids = "{call.from_user.id}"; """)
        conn.commit()

    elif call.data == "Dont`t restart the bot":
        bot.send_message(call.from_user.id, "Alright, if you would like to continue receiving news, hit /resume command")

    elif call.data == "Support":
        bot.send_message(call.from_user.id, "Thank you for contacting us, our specialist will contact you :)")

################################################################################################################################################

@bot.message_handler(content_types=['text'])
def registration(message):
    id = message.chat.id
    
    if (f"{id}",) not in chat_ids():
        if message.text in news_types:
            global news_type
            news_type = message.text
            bot.send_message(id, "Awesome, in order to complete the registration you need to enter your first name, last name, age,\
                                country you are currently in\nExample: Ilon Mask 51 USA")
        
        if len(message.text.split(" ")) == 4:
            bot.send_message(id, "Cool!Thanks, from now on every 4 hours you will receive the news that you have chosen.\
                                \n\nThe following commands are available:\n/stop - if you want to stop the bot\
                                \n/resume - if you want to receive news again\n/support - if you need to contact technical support")
            data = message.text.split(" ")
            cur.execute(f"""INSERT INTO Users_data (first_name, last_name, age, news_type, country, chat_id)
                            VALUES("{data[0]}", "{data[1]}", "{data[2]}", "{news_type}", "{data[3]}", "{id}")""")
            conn.commit()

    else:
        bot.send_message(id, "You are already registered\n\nThe following commands are available:\n/stop - if you want to stop the bot\
                            \n/resume - if you want to receive news again\n/support - if you need to contact technical support")

#####################################################################################################################################################

if __name__ == "__main__":
    
    try:
        create_tables()
        bot.polling()
    
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except ConnectionError as e:
        print(e)