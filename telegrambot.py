from canversation import *
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler

def main():
    updater = Updater(token='',use_context = True)
    dispatcher = updater.dispatcher
    handler = ConversationHandler(
        entry_points= [CommandHandler('start',start)],

        states={
            'Batafsil':[CallbackQueryHandler(Batafsil)],
            'qatnashmoq':[CallbackQueryHandler(qatnashmoq)],
            'photosend':[CallbackQueryHandler(photosend)],
            'tasdiqlash':[MessageHandler(Filters.photo,tasdiqlash)],
            'contact_callback':[MessageHandler(Filters.contact,contact_callback)],

            'selectmessagetype':[CallbackQueryHandler(selectmessagetype)],
            'add_active_users':[MessageHandler(Filters.text,add_active_users)],
            'send_message_user_id_id':[MessageHandler(Filters.text,send_message_user_id_id)],
            'send_message_user_id_message':[CallbackQueryHandler(send_message_user_id_message)],
            'send_message_user_id_text':[MessageHandler(Filters.text,send_message_user_id_text)],
            'send_message_user_id_photo':[MessageHandler(Filters.photo,send_message_user_id_photo)],
            'send_message_user_id_video':[MessageHandler(Filters.video,send_message_user_id_video)],

            'send_message_active_users':[CallbackQueryHandler(send_message_active_users)],
            'send_message_active_users_text':[MessageHandler(Filters.text,send_message_active_users_text)],
            'send_message_active_users_photo':[MessageHandler(Filters.photo,send_message_active_users_photo)],
            'send_message_active_users_video':[MessageHandler(Filters.video,send_message_active_users_video)],

            'all_users_send_message':[CallbackQueryHandler(all_users_send_message)],
            'all_users_send_message_text':[MessageHandler(Filters.text,all_users_send_message_text)],
            'all_users_send_message_photo':[MessageHandler(Filters.photo,all_users_send_message_photo)],
            'all_users_send_message_video':[MessageHandler(Filters.video,all_users_send_message_video)],

            'edit_home_page':[CallbackQueryHandler(edit_home_page)],
            'edit_home_page_text':[MessageHandler(Filters.text,edit_home_page_text)],
            'edit_home_page_batafsil_text':[MessageHandler(Filters.text,edit_home_page_batafsil_text)],
            'edit_home_page_dastur_text':[MessageHandler(Filters.text,edit_home_page_dastur_text)],
            'edit_home_page_tulov_text':[MessageHandler(Filters.text,edit_home_page_tulov_text)],
            'edit_home_page_aloqa_text':[MessageHandler(Filters.text,edit_home_page_aloqa_text)],


        },
        fallbacks=[CommandHandler('start',start),
        CommandHandler('admin', admin),
        CommandHandler('users', users),
        CommandHandler('activeusers', activeusers),
        CallbackQueryHandler(Batafsil),
        CallbackQueryHandler(qatnashmoq),
        ]
    )
    dispatcher.add_handler(handler)
    updater.start_polling()
    print('Running... [Press Ctrl+C to stop]')
    updater.idle()



main()
