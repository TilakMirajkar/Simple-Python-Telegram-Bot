import telebot
import requests


BOT_TOKEN = "your_bot_api_token" 
'''
To get your bot API token
Search botfather on telegram and start a chat
/start > /newbot
and follow the rest instructions
'''
bot = telebot.TeleBot(BOT_TOKEN) #creates a bot instance


@bot.message_handler(commands=['start', 'hello']) #if user texts 'start' or 'hello', it replies
def send_welcome(message):
    bot.reply_to(message, "Hey, how are you doing?")


def get_daily_horoscope(sign: str, day: str) -> dict: #this function is used to get daily horoscope
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params=params)
    return response.json()


@bot.message_handler(commands=['horoscope']) #if user texts 'horoscope' bot asks your sign and goes to day_handler function
def sign_handler(message):
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message): #this functions takes day input and fetches teh horoscope by passing the values to fetch_horoscope
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign): #returns users horoscope based on sign & day
    day = message.text.upper()
    horoscope = get_daily_horoscope(sign, day) #horoscope instance 
    if "data" in horoscope:
        data = horoscope["data"]
        horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
        bot.send_message(message.chat.id, "Here's Your Horoscope:")
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't fetch the horoscope. Please try again.")

bot.infinity_polling() #to launch the bot


