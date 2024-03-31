import requests
import telebot
from telebot import types

# Your Telegram bot token
BOT_TOKEN = "6899480458:AAEDERCh7X4RefFxaIvNpW4PFQkLFqVex_Y"

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
CHANNEL_ID = "@your_channel_name_here"

def send_strings_as_messages(ips, channel_id):
    num_proxies = len(ips)
    for i in range(0, num_proxies, 5):  # Step by 5 to group proxies into sets of 5
        message = ""
        keyboard = types.InlineKeyboardMarkup()
        for j, ip_with_port in enumerate(ips[i:i+5], start=1):
            # Extract IP address without port
            ip = ip_with_port.split(':')[0]
            label = f"Proxy{i + j}"
            message += f"{label} "
            url_button = types.InlineKeyboardButton(text=label, url=f"tg://proxy?server={ip}&port=33333&secret=eee601e300d8e3fb8bfcec8828f9cf08347777772e636c6f7564666c6172652e636f6d")
            keyboard.add(url_button)
        bot.send_message(channel_id, message, reply_markup=keyboard)





@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn = types.KeyboardButton('Fetch and Send Data')
    markup.row(itembtn)
    bot.send_message(message.chat.id, "Press the button to fetch and send data:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Fetch and Send Data':
        # Fetch IPs from the first API endpoint
        ips1 = make_api_call("https://api.runonflux.io/apps/location/MEHD4")
        ips2 = make_api_call("https://api.runonflux.io/apps/location/MEHD")
        
        if ips1 and ips2:
            all_ips = ips1 + ips2  # Concatenate IPs from both endpoints
            send_strings_as_messages(all_ips, message.chat.id)
            bot.send_message(message.chat.id, "Data fetched and sent successfully!")
        else:
            bot.send_message(message.chat.id, "Failed to fetch data. Please try again later.")

bot.polling()
