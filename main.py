import telebot
from telebot import types
import json
import re

# Initial configuration
TOKEN = ''
CHANNEL_ID = ''
ADMIN_ID = 1234567

bot = telebot.TeleBot(TOKEN)
user_data = {}

# Load languages from JSON file
with open('lang.json', 'r', encoding='utf-8') as f:
    LANGS = json.load(f)

# Translation function
def t(user_id, key, **kwargs):
    lang = user_data.get(user_id, {}).get('lang', 'fa')
    return LANGS[lang].get(key, key).format(**kwargs)   

# URL validation function
def is_valid_url(url):
    # Check for http:// or https://
    return url.startswith("http://") or url.startswith("https://")

# Start bot and choose language
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(LANGS['fa']['lang_fa'], LANGS['en']['lang_en'])
    bot.send_message(message.chat.id, LANGS['fa']['language_prompt'], reply_markup=markup)
    user_data[message.from_user.id] = {'step': 'choose_language'}

@bot.message_handler(func=lambda m: m.text in [LANGS['fa']['lang_fa'], LANGS['en']['lang_en']])
def set_language(message):
    lang = 'fa' if 'فار' in message.text else 'en'
    user_data[message.from_user.id] = {'lang': lang}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(t(message.from_user.id, 'create_new'), t(message.from_user.id, 'send_to_channel'))
    bot.send_message(message.chat.id, t(message.from_user.id, 'welcome'), reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'create_new'))
def create_new_message(message):
    user_data[message.from_user.id].update({
        'step': 'waiting_for_text',
        'buttons': []
    })
    bot.send_message(message.chat.id, t(message.from_user.id, 'start_text'), reply_markup=types.ReplyKeyboardRemove())

    @bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_text')
    def get_message_text(message):
        user_data[message.from_user.id]['text'] = message.text
        user_data[message.from_user.id]['step'] = 'waiting_for_button_count'

        # Set the number of buttons to appear in each row
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                           row_width=3)  # Adjust 'row_width' to display buttons side by side

        # Add buttons for selecting button count (1 to 5)
        for i in range(1, 6):
            markup.add(f'{i} button' if user_data[message.from_user.id]['lang'] == 'en' else f'{i} دکمه')

        # Send message with button options
        bot.send_message(message.chat.id, t(message.from_user.id, 'choose_buttons'), reply_markup=markup)
@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_count')
def get_button_count(message):
    try:
        count = int(message.text.split()[0])
        user_data[message.from_user.id].update({
            'button_count': count,
            'current_button': 1,
            'step': 'waiting_for_button_text'
        })
        bot.send_message(message.chat.id, t(message.from_user.id, 'enter_button_text', n=1), reply_markup=types.ReplyKeyboardRemove())
    except:
        bot.send_message(message.chat.id, t(message.from_user.id, 'invalid_number'))

@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_text')
def get_button_text(message):
    uid = message.from_user.id
    cur = user_data[uid]['current_button']
    user_data[uid]['buttons'].append({'text': message.text, 'url': None})
    user_data[uid]['step'] = 'waiting_for_button_url'
    bot.send_message(message.chat.id, t(uid, 'enter_button_url', n=cur))

@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_url')
def get_button_url(message):
    uid = message.from_user.id
    cur = user_data[uid]['current_button']
    if not is_valid_url(message.text):
        bot.send_message(message.chat.id, "❌ لینک معتبر نیست. لطفاً لینک را با http یا https شروع کنید.")
        return  # exit the function to get the URL again
    user_data[uid]['buttons'][-1]['url'] = message.text
    if cur < user_data[uid]['button_count']:
        user_data[uid]['current_button'] += 1
        user_data[uid]['step'] = 'waiting_for_button_text'
        bot.send_message(message.chat.id, t(uid, 'enter_button_text', n=cur + 1))
    else:
        user_data[uid]['step'] = 'ready_to_send'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(t(uid, 'preview'), t(uid, 'send_to_channel'), t(uid, 'restart'))
        bot.send_message(message.chat.id, t(uid, 'setup_done'), reply_markup=markup)

@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'ready_to_send' and m.text == t(m.from_user.id, 'preview'))
def preview(message):
    uid = message.from_user.id
    data = user_data[uid]
    markup = types.InlineKeyboardMarkup()
    for btn in data['buttons']:
        markup.add(types.InlineKeyboardButton(btn['text'], url=btn['url']))
    bot.send_message(message.chat.id, t(uid, 'preview_message', text=data['text']), reply_markup=markup)

@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'ready_to_send' and m.text == t(m.from_user.id, 'send_to_channel'))
def send_to_channel(message):
    uid = message.from_user.id
    if uid != ADMIN_ID:
        bot.send_message(uid, t(uid, 'no_permission'))
        return
    data = user_data[uid]
    markup = types.InlineKeyboardMarkup()
    for btn in data['buttons']:
        markup.add(types.InlineKeyboardButton(btn['text'], url=btn['url']))
    try:
        bot.send_message(CHANNEL_ID, data['text'], reply_markup=markup)
        bot.send_message(uid, t(uid, 'sent_success'))
    except Exception as e:
        bot.send_message(uid, t(uid, 'send_error', error=str(e)))

@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'restart'))
def restart_process(message):
    user_data.pop(message.from_user.id, None)
    send_welcome(message)

if __name__ == '__main__':
    print("✅ Bot is running...")
    bot.polling(none_stop=True)
