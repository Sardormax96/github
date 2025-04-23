from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = '978768091:AAENMQ4_h3xnPraINsYLJQgWuC92QdVthCc'

# Command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your simple Telegram bot!")

# Set up and run the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

