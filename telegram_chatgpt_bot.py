import os
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')  # Store your OpenAI key as an environment variable

# Set up the Telegram Bot API token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Store your Telegram token as an environment variable

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text('Hi! I am a ChatGPT-powered bot. Ask me anything!')

def chatgpt_response(user_input):
    """Get a response from the ChatGPT API."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming messages from the user."""
    user_message = update.message.text
    response = chatgpt_response(user_message)
    update.message.reply_text(response)

def main():
    """Start the bot."""
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start polling for updates from Telegram
    updater.start_polling()

    # Run the bot until you send a stop signal
    updater.idle()

if __name__ == '__main__':
    main()
