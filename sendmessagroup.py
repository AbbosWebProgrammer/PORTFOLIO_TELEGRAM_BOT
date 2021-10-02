import requests
from  datetime import datetime
import pytz
import telegram
IST = pytz.timezone('Asia/Tashkent')
raw_TS=datetime.now(IST)
curr_date=raw_TS.strftime("%d-%m-%Y")
curr_time=raw_TS.strftime("%H:%M:%S")
telegram_auth_token = "1967693436:AAHJt2gOiC8L6eT7lqvbMZlR1XdZsSSUHNg"
telegram_group_id="newgroupnewbot"
msg=f" Message on {curr_date} at {curr_time}"
# msg=f" Message"

def send_msg_on_telegram(message,files):
    telegram_api_url=f"https://api.telegram.org/bot{telegram_auth_token}/sendPhoto?chat_id=@{telegram_group_id}&caption={message}"
    tel_resp=requests.post(telegram_api_url,files=files)
    if tel_resp.status_code==200:
        print("INTO :notication has been sent on Telegram")
    else:
        print("Error : could not send Message")

def send_msg_on_telegram_text(message):
    telegram_api_url=f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_resp=requests.post(telegram_api_url)
    if tel_resp.status_code==200:
        print("INTO :notication has been sent on Telegram")
    else:
        print("Error : could not send Message")

# send_msg_on_telegram_text("salomdewfrthydtijikwrtytnhgl;'gretrhyghj")