import requests
import telebot
from telebot import types

# Your Telegram bot token
BOT_TOKEN = "6483606225:AAGJJnzhL4r17qAkChxBWkapqENRX4Hno84"
CHANNEL_ID ="@vpn_pvc"
# Password for authentication
PASSWORD = "Myhorseisblack69"

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
    num_proxies = len(ips)
    for i in range(0, num_proxies, 7):  # Step by 5 to group proxies into sets of 5
        message = "\n"

        for j, ip_with_port in enumerate(ips[i:i+7], start=1):
            # Extract IP address without port
            ip = ip_with_port.split(':')[0]
            label = f"Proxy{i + j}"
            message += f"vless://dbda02f3-3d45-4785-b4f4-c9c3feb2dd5f@{ip}:36664?type=tcp&security=reality&pbk=dXl41aTQs_k4-62GFxC5GnRIQm9oMO5x8MKfgVgreGo&fp=firefox&sni=greenpepper.ir&sid=9d&spx=%2F&flow=xtls-rprx-vision#@vpn_pvc-r4e@vpn_pvc\n\n\n"


    bot.send_message(CHANNEL_ID, f"@vpn_pvc free premium proxy and VPN \n share and react! \n جهت تداوم به اشتراک بگذارید\n{message}")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please enter the password to access the bot's functionalities:")
    bot.register_next_step_handler(message,echo_all)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == PASSWORD:
        markup = types.ReplyKeyboardMarkup()
        itembtn = types.KeyboardButton('Fetch and Send Data')
        markup.row(itembtn)
        bot.send_message(message.chat.id, "Press the button to fetch and send data:", reply_markup=markup)
        bot.register_next_step_handler(message,handle_fetch)
    else:
        bot.send_message(message.chat.id, "Incorrect password. Please try again.")

@bot.message_handler(func=lambda message: True)
def handle_fetch(message):
    if message.text == 'Fetch and Send Data':
        # Fetch IPs from the first API endpoint
        ips1 = make_api_call("https://api.runonflux.io/apps/location/dh1u")
        
        if ips1:
            all_ips = ips1  # Concatenate IPs from both endpoints
            send_strings_as_messages(all_ips, message.chat.id)
            #bot.send_message(message.chat.id, "Data fetched and sent successfully!")
        else:
            bot.send_message(message.chat.id, "Failed to fetch data. Please try again later.")

bot.polling()
