from os import replace
from telegram import ReplyKeyboardMarkup,KeyboardButton,InputMediaPhoto
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from adminpage import *
import json
import urllib.request
import time

def start(update,context):

    chatids=get_peoples_chat_id()
    firstname = update.message.chat.first_name
    username = update.message.chat.username
    if not update.effective_chat.id in chatids:
        createuser(update.effective_chat.id,firstname,username)

    keys = []
    keys.append([InlineKeyboardButton("Батафсил",callback_data=str("Batafsil"))])
    murkup = InlineKeyboardMarkup(keys)


    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f'''Муваффақиятли обуна билан табриклаймиз !
        ''')
    time.sleep(1)
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f'''
        Ассалому алайкум, {firstname} !
        ''',
    )
    time.sleep(1)
    context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo = open("photo.jpg",'rb'),

                caption=f'''
Ассалому алейкум, {firstname} !

{gethomepagetext()}''',
                reply_markup=murkup
            )
    return "Batafsil"

def Batafsil(update,context):
    query = update.callback_query
    name=get_people_name(update.effective_chat.id)
    keys = []
    keys.append([InlineKeyboardButton("Қатнашаман",callback_data=str("Qatnashmoq"))])
    murkup = InlineKeyboardMarkup(keys)
    if query.data=='Batafsil':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
text=f'''
Ассалому алейкум,  {name} !

{gethomepagebatafsiltext()}''',
            reply_markup=murkup
            )
    return 'qatnashmoq'
def qatnashmoq(update,context):


    query = update.callback_query
    query.answer()
    if query.data=='Qatnashmoq':
        contact_keyboard = KeyboardButton('Рақам жўнатиш', request_contact=True)
        markup= [[contact_keyboard ]]
        reply_markup = ReplyKeyboardMarkup(markup,one_time_keyboard=True,resize_keyboard=True)
        context.bot.send_message(
             chat_id=update.effective_chat.id,
            text=f'''Илтимос телефон рақамингизни жўнатинг.
        ''' ,
        reply_markup=reply_markup
        )

    return 'contact_callback'
def contact_callback(update,context):

    contact = update.effective_message.contact
    phone = contact.phone_number
    date=get_people_info( update.effective_chat.id)
    message= f'''Chat_id: {date[1]}
        Name: {date[2]}
        Username: @{date[3]}
        Phone:+{phone}
            '''
    send_msg_on_telegram_text(message)
    createactiveusernumber(update.effective_chat.id,phone)
    createactiveusernumber(update.effective_chat.id,phone)
    createactiveusernumber(update.effective_chat.id,phone)
    keys = []
    keys.append([InlineKeyboardButton("Тўлов қоғозни жўнатиш",callback_data=str("Rasmni jo'natish"))])
    murkup = InlineKeyboardMarkup(keys)
    removeKeyboard = {'remove_keyboard':True}
    removeKeyboardEncoded = json.dumps(removeKeyboard)
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'''{gethomepagedasturtext()}
''',
            reply_markup=removeKeyboardEncoded

            )
    time.sleep(2)
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'''{gethomepagetulovtext()}
''',
            reply_markup=murkup

            )

    return "photosend"

def photosend(update,context):
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'''Тўлов қилинган қоғозини жўнатинг.
    ''',
            )
    return 'tasdiqlash'

def tasdiqlash(update,context):

    file = update.message.photo[-1].file_id
    filename=str(update.update_id)+'.jpg'
    obj = context.bot.get_file(file)
    down=obj.download(filename)

    if down:
        createimages(update.effective_chat.id,filename)
        date=get_people_info( update.effective_chat.id)
        message= f'''
        Chat_id: {date[1]}
        Name: {date[2]}
        Username: @{date[3]}
        Phone:{date[6]}
            '''
        files={'photo':open(filename,'rb')}
        send_msg_on_telegram(message,files)

        keys = []
        keys.append([InlineKeyboardButton(text="Сайтга ўтиш", url="https://biznesintellekt.uz/")])
        murkup = InlineKeyboardMarkup(keys)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'''{gethomepagealoqatext()}''',
        reply_markup=murkup
            )
    return "Batafsil"




