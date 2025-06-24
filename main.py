import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

main_button = InlineKeyboardMarkup()
main_button.add(InlineKeyboardButton("🎰 Играть в 1Win", url="https://1wqgju.life/?p=glfz"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        f"👋 Добро пожаловать, {message.from_user.first_name}!\n\n"
        "🎲 Здесь ты можешь начать играть прямо сейчас.\n"
        "🔐 Актуальный промокод: *LUCKYSPI11*\n\n"
        "Нажми кнопку ниже, чтобы перейти в 1Win и начать игру!",
        reply_markup=main_button, parse_mode="Markdown")

@bot.message_handler(commands=['promo'])
def promo(message):
    bot.send_message(message.chat.id,
        "🎁 Промокод: *LUCKYSPI11*\n"
        "💰 Введи его при регистрации, чтобы получить бонусы!",
        parse_mode="Markdown")

@bot.message_handler(commands=['bonus'])
def bonus(message):
    bot.send_message(message.chat.id,
        "💸 Бонусы:\n• До 500% на первый депозит\n• Ежедневные акции и фриспины\n• Кэшбэк до 30%\n"
        "Не забудь указать промокод *LUCKYSPI11*", parse_mode="Markdown")

@bot.message_handler(commands=['faq'])
def faq(message):
    bot.send_message(message.chat.id,
        "❓ Частые вопросы:\n\n"
        "🔹 Как пополнить? — Через карту, крипту, ЕРИП и т.д.\n"
        "🔹 Как вывести? — Обычно в течение 5 минут\n"
        "🔹 Игры? — Aviator, Sweet Bonanza, JetX и многое другое")

@bot.message_handler(commands=['games'])
def games(message):
    bot.send_message(message.chat.id,
        "🎮 Топ игры:\n• Aviator ✈️\n• JetX 🚀\n• Crazy Time 🎡\n• Sweet Bonanza 🍬\n• Mines 💣")

@bot.message_handler(commands=['support'])
def support(message):
    bot.send_message(message.chat.id,
        "🆘 Поддержка: напиши сюда 👉 @твой_ник")

print("Бот запущен.")
bot.infinity_polling()
