from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def messagetype():
    keys = []
    keys.append([InlineKeyboardButton("Send message",callback_data=str("Send message"))])
    keys.append([InlineKeyboardButton("Send photo message",callback_data=str("Send photo message"))])
    keys.append([InlineKeyboardButton("Send video message",callback_data=str("Send video message"))])
    keys.append([InlineKeyboardButton("<- Back",callback_data=str("<- Back"))])
    murkup = InlineKeyboardMarkup(keys)
    return murkup
def main_menu():
    keys = []
    keys.append([InlineKeyboardButton("Send message all users",callback_data=str("Send message all users"))])
    keys.append([InlineKeyboardButton("Send message user",callback_data=str("Send message user"))])
    keys.append([InlineKeyboardButton("Send message active users ",callback_data=str("Send message active users"))])
    keys.append([InlineKeyboardButton("Add active users",callback_data=str("Add active users"))])
    keys.append([InlineKeyboardButton("Edit page",callback_data=str("Edit page"))])
    murkup = InlineKeyboardMarkup(keys)
    return murkup

def edit_page():
    keys = []
    keys.append([InlineKeyboardButton("Home page",callback_data=str("Home page"))])
    keys.append([InlineKeyboardButton("Batafsil",callback_data=str("Batafsil"))])
    keys.append([InlineKeyboardButton("Dastur",callback_data=str("Dastur"))])
    keys.append([InlineKeyboardButton("To'lov",callback_data=str("To'lov"))])
    keys.append([InlineKeyboardButton("Aloqa",callback_data=str("Aloqa"))])
    keys.append([InlineKeyboardButton("<- Back",callback_data=str("<- Back"))])
    murkup = InlineKeyboardMarkup(keys)
    return murkup
