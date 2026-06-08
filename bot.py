import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.environ.get("8934349207:AAHJr0PbiGkBkL4czG0ACGGvYNBwGUxnKkQ")
CHANNEL_LINK = "https://t.me/+gR00nolNZmA2MGQ1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "<b>What can this bot do?</b>\n\n"
        "What can this bot do?\n\n"
        "😋 CLICK ON JOIN CHANNEL NOW ! AND YOU WILL GET FREE QUOTEX SIGNALS\n\n"
        "🔗 Link 👇👇👇👇👇👇👇👇\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n\n"
        "<b>SIGNALS STARTING IN 5 MINUTES</b>\n"
        "🚀🚀🚀🚀🚀"
    )
    keyboard = [[InlineKeyboardButton("🎯 Join Channel", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup, parse_mode="HTML", disable_web_page_preview=True)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="<b>Quotex Trading Bot Help</b>\n\nThis bot provides market insights and algorithmic trading signal notifications.", parse_mode="HTML")

async def faq_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="<b>Frequently Asked Questions</b>\n\n<b>Q: Are these signals 100% accurate?</b>\nA: No, signals are based on algorithmic calculations. Trading involves risk.", parse_mode="HTML")

def main() -> None:
    if not TOKEN: return
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("faq", faq_command))
    application.run_polling()

if __name__ == '__main__':
    main()