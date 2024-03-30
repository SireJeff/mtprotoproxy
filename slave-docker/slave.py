import requests
import telebot
from telebot import types

# Your Telegram bot token
BOT_TOKEN = "6300332682:AAGDxjH9qmVTl8XJF_LMugVoNEMM-cPOZZI"

bot = telebot.TeleBot(BOT_TOKEN)

def make_api_call(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract IPs from the response data
            ips = [entry.get('ip', '') for entry in response.json().get('data', [])]
            return ips
        else:
            print("API call failed with status code:", response.status_code)
            return []
    except Exception as e:
        print("Error occurred:", e)
        return []

def send_strings_as_messages(ips, chat_id):
    for ip in ips:
        message = f"tg://proxy?server={ip}&port=33333&secret=eee601e300d8e3fb8bfcec8828f9cf08347777772e636c6f7564666c6172652e636f6d"
        bot.send_message(chat_id, message)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Fetch and Send Data')
    markup.row(itembtn)
    bot.send_message(message.chat.id, "Press the button to fetch and send data:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Fetch and Send Data':
        # Fetch IPs from the first API endpoint
        ips1 = make_api_call("https://api.runonflux.io/apps/location/MEHD4")
        if ips1:
            send_strings_as_messages(ips1, message.chat.id)
            bot.send_message(message.chat.id, "Data from first endpoint fetched and sent successfully!")
        else:
            bot.send_message(message.chat.id, "Failed to fetch data from first endpoint. Please try again later.")
        
        # Fetch IPs from the second API endpoint
        ips2 = make_api_call("https://api.runonflux.io/apps/location/MEHD")
        if ips2:
            send_strings_as_messages(ips2, message.chat.id)
            bot.send_message(message.chat.id, "Data from second endpoint fetched and sent successfully!")
        else:
            bot.send_message(message.chat.id, "Failed to fetch data from second endpoint. Please try again later.")

bot.polling()
