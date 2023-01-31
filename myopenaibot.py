import telebot
import openai

bot = telebot.TeleBot("5627888121:AAE5zoiNMcrddeN7EXf8dsAd5aFZ0cHIp6c")
openai.api_key = "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"

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
