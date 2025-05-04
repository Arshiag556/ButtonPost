import telebot
from telebot import types
import json
import re

# Configuration
TOKEN = '7167390844:AAGgdmBvT235tAhR2-aBtG5PNewJMVjyDTU'
CHANNEL_ID = '@Arshiaabedi_dev'
ADMIN_ID = 6288319914  # Note: Make sure this is the correct admin ID

bot = telebot.TeleBot(TOKEN)
user_data = {}

# Load language file
try:
    with open('lang.json', 'r', encoding='utf-8') as f:
        LANGS = json.load(f)
except Exception as e:
    print(f"Failed to load language file: {e}")
    exit()


# Helper functions
def t(user_id, key, **kwargs):
    """Get translation for user's language"""
    lang = user_data.get(user_id, {}).get('lang', 'fa')
    return LANGS[lang].get(key, key).format(**kwargs)


def is_valid_url(url):
    """Check if URL is valid"""
    pattern = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'([A-Z0-9-]+\.)+[A-Z]{2,}'  # domain
        r'(:\d+)?'  # port
        r'(/.*)?$',  # path
        re.IGNORECASE
    )
    return bool(pattern.match(url))


def create_main_menu(user_id):
    """Create main menu keyboard"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(t(user_id, 'create_new'))
    return markup


# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(LANGS['fa']['lang_fa'], LANGS['en']['lang_en'])
    bot.send_message(message.chat.id, t(message.from_user.id, 'language_prompt'), reply_markup=markup)
    user_data[message.from_user.id] = {'step': 'choose_language'}


# Language selection
@bot.message_handler(func=lambda m: m.text in [LANGS['fa']['lang_fa'], LANGS['en']['lang_en']] and
                                    user_data.get(m.from_user.id, {}).get('step') == 'choose_language')
def set_language(message):
    lang = 'fa' if LANGS['fa']['lang_fa'] == message.text else 'en'
    user_data[message.from_user.id] = {'lang': lang}
    bot.send_message(message.chat.id, t(message.from_user.id, 'welcome'),
                     reply_markup=create_main_menu(message.from_user.id))


# Create new message
@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'create_new'))
def create_message(message):
    user_data[message.from_user.id].update({
        'step': 'waiting_for_content',
        'buttons': []
    })
    bot.send_message(message.chat.id, t(message.from_user.id, 'start_text_photo'),
                     reply_markup=types.ReplyKeyboardRemove())


# Handle message content
@bot.message_handler(content_types=['text', 'photo'],
                     func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_content')
def handle_content(message):
    uid = message.from_user.id
    user_data[uid]['step'] = 'waiting_for_button_count'

    if message.photo:
        user_data[uid]['photo'] = message.photo[-1].file_id
        user_data[uid]['text'] = message.caption or ''
    else:
        user_data[uid]['text'] = message.text
        user_data[uid]['photo'] = None

    # Create button count selection
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [f"{i} {t(uid, 'buttons')}" for i in range(1, 6)]
    markup.add(*buttons)
    bot.send_message(message.chat.id, t(uid, 'choose_buttons'), reply_markup=markup)


# Button count selection
@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_count')
def handle_button_count(message):
    try:
        uid = message.from_user.id
        count = int(message.text.split()[0])

        if 1 <= count <= 5:
            user_data[uid].update({
                'button_count': count,
                'current_button': 1,
                'step': 'waiting_for_button_text'
            })
            bot.send_message(uid, t(uid, 'enter_button_text', n=1),
                             reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(uid, t(uid, 'invalid_number'))
    except:
        bot.send_message(message.from_user.id, t(message.from_user.id, 'invalid_number'))


# Button text input
@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_text')
def handle_button_text(message):
    uid = message.from_user.id
    current = user_data[uid]['current_button']

    user_data[uid]['buttons'].append({'text': message.text, 'url': None})
    user_data[uid]['step'] = 'waiting_for_button_url'

    bot.send_message(uid, t(uid, 'enter_button_url', n=current))


# Button URL input
@bot.message_handler(func=lambda m: user_data.get(m.from_user.id, {}).get('step') == 'waiting_for_button_url')
def handle_button_url(message):
    uid = message.from_user.id
    current = user_data[uid]['current_button']

    if not is_valid_url(message.text):
        bot.send_message(uid, t(uid, 'invalid_url'))
        return

    user_data[uid]['buttons'][-1]['url'] = message.text

    if current < user_data[uid]['button_count']:
        user_data[uid]['current_button'] += 1
        user_data[uid]['step'] = 'waiting_for_button_text'
        bot.send_message(uid, t(uid, 'enter_button_text', n=current + 1))
    else:
        user_data[uid]['step'] = 'ready_to_send'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(t(uid, 'preview'), t(uid, 'send_to_channel'))
        markup.add(t(uid, 'restart'))
        bot.send_message(uid, t(uid, 'setup_done'), reply_markup=markup)


# Preview message
@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'preview') and
                                    user_data.get(m.from_user.id, {}).get('step') == 'ready_to_send')
def preview_message(message):
    uid = message.from_user.id
    data = user_data[uid]

    markup = types.InlineKeyboardMarkup(row_width=2)
    for btn in data['buttons']:
        markup.add(types.InlineKeyboardButton(btn['text'], url=btn['url']))

    try:
        if data['photo']:
            bot.send_photo(uid, data['photo'], caption=data['text'], reply_markup=markup)
        else:
            bot.send_message(uid, t(uid, 'preview_message', text=data['text']), reply_markup=markup)
    except Exception as e:
        bot.send_message(uid, f"Error creating preview: {str(e)}")


# Send to channel
@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'send_to_channel') and
                                    user_data.get(m.from_user.id, {}).get('step') == 'ready_to_send')
def send_to_channel(message):
    uid = message.from_user.id
    if uid != ADMIN_ID:
        bot.send_message(uid, t(uid, 'no_permission'))
        return

    data = user_data[uid]
    markup = types.InlineKeyboardMarkup(row_width=2)
    for btn in data['buttons']:
        markup.add(types.InlineKeyboardButton(btn['text'], url=btn['url']))

    try:
        if data['photo']:
            bot.send_photo(CHANNEL_ID, data['photo'], caption=data['text'], reply_markup=markup)
        else:
            bot.send_message(CHANNEL_ID, data['text'], reply_markup=markup)
        bot.send_message(uid, t(uid, 'sent_success'))
    except Exception as e:
        bot.send_message(uid, t(uid, 'send_error', error=str(e)))


# Restart process
@bot.message_handler(func=lambda m: m.text == t(m.from_user.id, 'restart'))
def restart_process(message):
    user_data.pop(message.from_user.id, None)
    send_welcome(message)


# Error handler
@bot.message_handler(func=lambda m: True)
def handle_unrecognized(message):
    bot.send_message(message.chat.id, "I didn't understand that. Please use the buttons provided.")


if __name__ == '__main__':
    print("✅ Bot is running...")
    bot.infinity_polling()
