import requests
import random
import telebot
from telebot import types

bot = telebot.TeleBot('api token')

def send_comic(message):

    response = requests.get('')
    max_comic_id = response.json()['num']
    comic_id = random.randint(1, max_comic_id)
    response = requests.get(f'https://api{comic_id}/info.0.json')
    data = response.json()


    bot.send_photo(message.chat.id, data['img'], caption=data['alt'])

def send_meme(message):

    response = requests.get('')

    memes = response.json()['data']['memes']
    meme = random.choice(memes)

    image_url = meme['url']

    bot.send_photo(message.chat.id, image_url)


def send_kitten(message):

    width = random.randint(200, 600)
    height = random.randint(200, 600)

    url = f'http://api{width}/{height}'
    bot.send_photo(message.chat.id, url)
    
def send_dog(message):

    response = requests.get('')
    data = response.json()


    image_url = data['message']
  
    bot.send_photo(message.chat.id, image_url)


def send_random_user(message):

    response = requests.get('')
    data = response.json()['results'][0]

    name = f"{data['name']['first']} {data['name']['last']}"
    email = data['email']
    phone_number = data['phone']
    password = data['login']['password']
    profile_picture = data['picture']['large']

   
    message_text = f"Name: {name}\n"
    message_text += f"Email: {email}\n"
    message_text += f"Phone Number: {phone_number}\n"
    message_text += f"Password: {password}\n"

   
    bot.send_message(message.chat.id, message_text)
    bot.send_photo(message.chat.id, profile_picture)


keyboard = types.ReplyKeyboardMarkup(row_width=2)
xkcd_button = types.KeyboardButton('')
meme_button = types.KeyboardButton('')
kitten_button = types.KeyboardButton('')
dog_button = types.KeyboardButton('')
randomuser_button = types.KeyboardButton('')
keyboard.add(xkcd_button, meme_button, kitten_button, dog_button, randomuser_button)


@bot.message_handler(func=lambda message: message.text == '')
def handle_xkcd_button(message):
    send_xkcd(message)

@bot.message_handler(func=lambda message: message.text == '')
def handle_meme_button(message):
    send_meme(message)

@bot.message_handler(func=lambda message: message.text == '')
def handle_kitten_button(message):
    send_kitten(message)

@bot.message_handler(func=lambda message: message.text == '')
def handle_dog_button(message):
    send_dog(message)

@bot.message_handler(func=lambda message: message.text == '')
def handle_randomuser_button(message):
    send_random_user(message)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, ' ', reply_markup=keyboard)

print("starting...")
bot.polling()


