# ChatGPT Telegram Bot

This is a simple Telegram bot powered by OpenAI's ChatGPT. The bot allows users to interact with ChatGPT through Telegram, providing conversational AI capabilities.

## Features

- Responds to user queries using the ChatGPT API.
- Simple command to start interaction (`/start`).
- Continuously listens and responds to messages in the chat.

## Requirements

- Python 3.7+
- The following Python packages:
  - `python-telegram-bot`
  - `openai`

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chatgpt_telegram_bot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd chatgpt_telegram_bot
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables for the API keys:
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   export TELEGRAM_TOKEN='your-telegram-bot-token'
   ```

5. Run the bot:
   ```bash
   python telegram_chatgpt_bot.py
   ```

## Usage

- Start the bot in your Telegram client by sending `/start`.
- Send any message to the bot, and it will reply using the ChatGPT API.

## License

This project is licensed under the MIT License.
