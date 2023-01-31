import telebot
import openai

bot = telebot.TeleBot("API_from_@BotFather")
openai.api_key = "openAI_API"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am a bot that uses OpenAI to answer questions. How can I help you?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    question = message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"Answer the following question: {question}"),
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].text
    bot.reply_to(message, answer)

bot.polling()
