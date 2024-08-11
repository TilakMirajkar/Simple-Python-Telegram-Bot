import telebot
import requests
import pyowm
from newsapi import NewsApiClient


BOT_TOKEN = "your_bot_token" 
'''
To get your bot API token
Search botfather on telegram and start a chat
/start > /newbot
and follow the rest instructions
'''
bot = telebot.TeleBot(BOT_TOKEN) #creates a bot instance


@bot.message_handler(commands=['start', 'hello']) #if user texts 'start' or 'hello', it replies
def send_welcome(message):
    bot.reply_to(message, "Hey, how are you doing?\n Here are some available commands\n/horoscope\n/weather\n/news")


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



owm = pyowm.OWM('your_owm_api')
''' 
To get you Weather API go to 'OpenWeatherMap'
Create your account and you'll get your API key
'''

@bot.message_handler(commands=['weather']) #if user texts 'weather' bot asks the city for the weather, jumps to get_weather function
def get_weather_msg(message):
    text = "Which city's weather would you like to get?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, get_weather)

def get_weather(message):
    city = message.text  
    manager = owm.weather_manager()
    observation = manager.weather_at_place(city) #get weather of the city
    w = observation.weather
    sent_message = f"Weather in {city}: {w.status}, {w.temperature('celsius')['temp']}°C"
    bot.send_message(message.chat.id, sent_message)
    



newsapi = NewsApiClient(api_key="your_newsAPI")
'''
To get you News API key go to 'NewsAPI'
Create your account and you'll get your API key
'''

@bot.message_handler(commands=['news']) #if user texts 'news' bot generates top 10 headline from US in English
def get_top_headlines(message):
    bot.send_message(message.chat.id, "Here's Top Headlines!")
    top_headlines = newsapi.get_top_headlines(language='en', country='us') #get top headlines data
    headlines=''
    for i, article in enumerate(top_headlines['articles'][:10], start=1):
        headlines += f"{i}. {article['title']}\n" #get first 10 articles and their titles
    bot.send_message(message.chat.id, headlines)
    return 0




bot.infinity_polling() #to launch the bot
