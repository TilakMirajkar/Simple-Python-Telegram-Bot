# Telegram Horoscope Chatbot

This project is a simple yet effective Telegram chatbot that provides users with their daily horoscope based on their zodiac sign and the desired day.

## Getting Started

Follow these steps to set up and run the Telegram Horoscope Chatbot:

### Step 1: Create a Telegram Bot

1. Open the Telegram app and search for **BotFather**.
2. Start a chat with BotFather, type `/newbot` to create a new bot.
3. Follow the prompts to give your bot a name and a username and then lastly **Copy your token**.

### Step 2: Set Up the Project

1. Clone this repository or download the source code to your local machine.
   ```bash
   git clone https://github.com/TilakMirajkar/Telegram-Horoscope-Bot.git
   ```
2. Install the required Python libraries by running:
   ```bash
   pip install pyTelegramBotAPI requests
   ```
3. Open the `bot.py` file in your preferred code editor.
4. Locate the `BOT_TOKEN` variable and replace `"your_bot_token_here"` with the API token you obtained from BotFather:
   ```python
   BOT_TOKEN = "your_bot_token_here"
   ```

### Step 3: Run the Bot

1. Run the bot by executing the following command:
   ```bash
   python bot.py
   ```

### Step 4: Interact with Your Bot

1. Open Telegram and search for your bot using the username you provided during setup.
2. Start a chat with your bot by clicking on it and typing `/start`.
3. You can now use commands like `/horoscope` to interact with your bot and receive your daily horoscope.

## Commands

- `/start` or `/hello`: Starts the bot and greets the user.
- `/horoscope`: Initiates the process of retrieving your daily horoscope.

## Conclusion

This Telegram Horoscope Chatbot is a straightforward and enjoyable way to receive daily horoscopes. With just a few simple steps, you can have your own personal horoscope bot running and ready to provide insights to you and your friends.

Feel free to customize and expand the bot to add more features or improve its functionality!