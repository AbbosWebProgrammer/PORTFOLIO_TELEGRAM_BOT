from telegram import ReplyKeyboardMarkup,KeyboardButton,InputMediaPhoto
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from connectdb import *
from keybord import *
from sendmessagroup import *


def admin(update,context):
    users = get_admin_id()
    if str(update.effective_chat.id) in  users:
        murkup = main_menu()
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Assalomu aleykum Admin page xush kelibsiz!''',
            reply_markup=murkup)
        return "selectmessagetype"
    else:
        return "start"

def users(update,context):
    users = get_admin_id()
    if str(update.effective_chat.id) in  users:
        users_count=get_users_count()
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''{users_count}''',
            )
        return "admin"
    else:
        return "start"

def activeusers(update,context):
    users = get_admin_id()
    if str(update.effective_chat.id) in  users:
        users_count=get_active_users_count()
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''{users_count}''',
            )
        return "admin"
    else:
        return "start"


def selectmessagetype(update,context):

    query = update.callback_query
    query.answer()
    if query.data == 'Send message all users':
        murkup = messagetype()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                        message_id=update.callback_query.message.message_id,
                        text="Qanday xabar jo'natmoqchisiz",
                        reply_markup=murkup)
        return 'all_users_send_message'


    if query.data == 'Send message user':
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f''' Userni ID sini kiriting !
            ''')
        return 'send_message_user_id_id'
    if query.data == 'Send message active users':
        murkup = messagetype()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                        message_id=update.callback_query.message.message_id,
                        text="Qanday xabar jo'natmoqchisiz",
                        reply_markup=murkup)
        return 'send_message_active_users'
    if query.data == 'Add active users':
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f''' Userni ID sini kiriting !
            ''')
        return 'add_active_users'
    if query.data == 'Edit page':
        murkup=edit_page()
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f''' Nimani o'zgartirmoqchisiz ?
            ''',
            reply_markup=murkup
            )
        return 'edit_home_page'
def add_active_users(update,context):
    id = update.message.text
    try:
        createactiveuser(id)
        context.bot.send_message(chat_id = update.effective_chat.id,
                text="Qo'shildi",)
    except Exception as e:
        context.bot.send_message(chat_id = update.effective_chat.id,
                text="Qo'shilmadi",)
    return "admin"


def send_message_user_id_id(update,context):
    global id
    id = int(update.message.text)
    murkup=messagetype()
    context.bot.delete_message(chat_id = update.effective_chat.id,
            message_id = update.message.message_id,)
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Qanday xabar jo'natmoqchisiz",
            reply_markup=murkup)
    return "send_message_user_id_message"
def send_message_user_id_message(update,context):
    query = update.callback_query
    query.answer()
    if query.data == 'Send message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!",)
        return 'send_message_user_id_text'
    if query.data == 'Send photo message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Rasmli xabarni jo'nating!")
        return 'send_message_user_id_photo'
    if query.data == 'Send video message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Videoli xabarni jo'nating!")
        return 'send_message_user_id_video'
    if query.data == '<- Back':
        murkup=main_menu()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Assalomu aleykum Admin page xush kelibsiz",
                                reply_markup=murkup)
        return "selectmessagetype"

def send_message_user_id_text(update,context):
    message = update.message.text
    context.bot.send_message(chat_id=id,text=message)
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    return "admin"
def send_message_user_id_photo(update,context):
    file = update.message.photo[-1].file_id
    filename=str(update.update_id)+'.jpg'
    # print(update.message)
    caption=update.message.caption
    obj = context.bot.get_file(file)
    down=obj.download(filename)
    chatids=get_peoples_chat_id()

    context.bot.send_photo(
        chat_id=id,
        photo = open(filename,'rb'),
        caption=caption,
        )
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    return "admin"
def send_message_user_id_video(update,context):
    filename = update.message.video.file_name
    file_id = update.message.video.file_id
    caption=update.message.caption
    obj = context.bot.get_file(file_id)
    down=obj.download(filename)
    context.bot.send_video(
            chat_id= id,
            video=open(filename, 'rb'),
            caption=caption,)
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    return "admin"

# Active users send message

def send_message_active_users(update,context):

    query = update.callback_query
    query.answer()
    if query.data == 'Send message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!",)
        return 'send_message_active_users_text'
    if query.data == 'Send photo message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Rasmli xabarni jo'nating!")
        return 'send_message_active_users_photo'
    if query.data == 'Send video message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Videoli xabarni jo'nating!")
        return 'send_message_active_users_video'
    if query.data == '<- Back':
        murkup = main_menu()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Assalomu aleykum Admin page xush kelibsiz",
                                reply_markup=murkup)
        return "selectmessagetype"


def send_message_active_users_text(update,context):
    message = update.message.text
    chatids=get_active_usres_id()
    for i in chatids:
                context.bot.send_message(chat_id = int(i),
                                    text=message,
                                    )
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')

    return "Batafsil"

def send_message_active_users_photo(update,context):
    file = update.message.photo[-1].file_id
    filename=str(update.update_id)+'.jpg'
    print(update.message)
    caption=update.message.caption
    obj = context.bot.get_file(file)
    down=obj.download(filename)
    chatids=get_active_usres_id()
    for i in chatids:
        context.bot.send_photo(
        chat_id=int(i),
        photo = open(filename,'rb'),
        caption=caption,
         )
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    return "admin"

def send_message_active_users_video(update,context):
    filename = str(update.message.video.file_id)+'.mp4'
    file_id = update.message.video.file_id
    caption=update.message.caption
    obj = context.bot.get_file(file_id)
    down=obj.download(filename)
    # print(update.message)
    if down:
        # print("ishladi")
        chatids=get_active_usres_id()
        for i in chatids:
            context.bot.send_video(
            chat_id= int(i),
            video=open(filename, 'rb'),
            caption=caption,)
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    else:
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xatolik sodir bo'ldi
            ''')

    return "admin"


#  AllUsers send message
def all_users_send_message(update,context):

    query = update.callback_query
    query.answer()
    if query.data == 'Send message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!",)
        return 'all_users_send_message_text'
    if query.data == 'Send photo message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Rasmli xabarni jo'nating!")
        return 'all_users_send_message_photo'
    if query.data == 'Send video message':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text=" Videoli xabarni jo'nating!")
        return 'all_users_send_message_video'
    if query.data == '<- Back':
        murkup=main_menu()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Assalomu aleykum Admin page xush kelibsiz",
                                reply_markup=murkup)
        return "selectmessagetype"


def all_users_send_message_text(update,context):
    keys = []
    keys.append([InlineKeyboardButton("Батафсил",callback_data=str("Batafsil"))])
    murkup = InlineKeyboardMarkup(keys)
    message = update.message.text
    chatids=get_peoples_chat_id()
    for i in chatids:
                context.bot.send_message(chat_id = int(i),
                                    text=message,
                                    reply_markup=murkup
                                    )
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')

    return "Batafsil"

def all_users_send_message_photo(update,context):
    file = update.message.photo[-1].file_id
    filename=str(update.update_id)+'.jpg'
    # print(update.message)
    caption=update.message.caption
    obj = context.bot.get_file(file)
    down=obj.download(filename)
    chatids=get_peoples_chat_id()
    for i in chatids:
        context.bot.send_photo(
        chat_id=int(i),
        photo = open(filename,'rb'),
        caption=caption,
         )
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    return "admin"

def all_users_send_message_video(update,context):
    filename = str(update.message.video.file_id)+'.mp4'
    file_id = update.message.video.file_id
    caption=update.message.caption
    obj = context.bot.get_file(file_id)
    down=obj.download(filename)
    # print(update.message)
    if down:
        # print("ishladi")
        chatids=get_peoples_chat_id()
        for i in chatids:
            context.bot.send_video(
            chat_id= int(i),
            video=open(filename, 'rb'),
            caption=caption,)
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xabar jo'natildi''')
    else:
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''Xatolik sodir bo'ldi
            ''')

    return "admin"



def edit_home_page(update,context):
    query = update.callback_query
    query.answer()
    if query.data == 'Home page':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!",)
        return 'edit_home_page_text'
    if query.data == 'Batafsil':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!")
        return 'edit_home_page_batafsil_text'
    if query.data == 'Dastur':
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!")
        return 'edit_home_page_dastur_text'
    if query.data == "To'lov":
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!")
        return 'edit_home_page_tulov_text'
    if query.data == "Aloqa":
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Xabarni jo'nating!")
        return 'edit_home_page_aloqa_text'

    if query.data == '<- Back':
        murkup=main_menu()
        context.bot.editMessageText(chat_id = update.effective_chat.id,
                                message_id=update.callback_query.message.message_id,
                                text="Assalomu aleykum Admin page xush kelibsiz",
                                reply_markup=murkup)
        return "selectmessagetype"


def edit_home_page_text(update,context):
    edithomepagetext(f'''{update.message.text}''')
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''O'zgartirildi''')

    return "admin"

def edit_home_page_batafsil_text(update,context):
    edithomepagebatafsiltext(f'''{update.message.text}''')
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''O'zgartirildi''')

    return "admin"
def edit_home_page_dastur_text(update,context):
    edithomepagedasturtext(f'''{update.message.text}''')
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''O'zgartirildi''')
    return "admin"

def edit_home_page_tulov_text(update,context):
    edithomepagetulovtext(f'''{update.message.text}''')
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''O'zgartirildi''')
    return "admin"

def edit_home_page_aloqa_text(update,context):
    edithomepagealoqatext(f'''{update.message.text}''')
    context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = f'''O'zgartirildi''')

    return "admin"





