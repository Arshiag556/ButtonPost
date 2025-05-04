# 📝 Telegram Post Bot - راهنمای کامل برای GitHub

## 🏷 عنوان پروژه
**ربات ساخت و ارسال پست حرفه‌ای به کانال تلگرام**

## 🌟 ویژگی‌های کلیدی
- ساخت پست‌های متنی و تصویری
- افزودن دکمه‌های شیشه‌ای با لینک
- پشتیبانی از چندزبانی (فارسی/انگلیسی)
- امکان پیش‌نمایش قبل از ارسال
- محدودیت دسترسی برای ارسال به کانال

## 🛠 فناوری‌های استفاده شده
- Python 3.10+
- pyTelegramBotAPI
- JSON برای مدیریت زبان‌ها

## 📦 نحوه نصب و راه‌اندازی

### پیش‌نیازها
```bash
git clone https://github.com/Arshiaabedi/telegram-post-bot.git
cd telegram-post-bot
python -m venv venv
source venv/bin/activate  # برای لینوکس/macOS
venv\Scripts\activate  # برای ویندوز
pip install -r requirements.txt
```

### تنظیمات
1. فایل `config.py` را ایجاد کنید:
```python
TOKEN = 'توکن_ربات_شما'
CHANNEL_ID = '@آیدی_کانال_شما'
ADMIN_ID = 123456789  # آیدی عددی ادمین
```

2. فایل `lang.json` را با ترجمه‌های مورد نظر پر کنید.

### اجرا
```bash
python bot.py
```


## 🎯 نمونه استفاده
```python
# نمونه کد برای توسعه‌دهندگان
from telebot import TeleBot

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "خوش آمدید!")
```

## 🤝 مشارکت
1. ریپوی پروژه را Fork کنید
2. شاخه جدید ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. تغییرات را Commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. به شاخه اصلی Push کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request باز کنید

## 📜 مجوز
این پروژه تحت مجوز **MIT** منتشر شده است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

## ✉️ ارتباط با توسعه‌دهنده
- ایمیل: arshiag556@gmail.com
- تلگرام: [@ArshY0X](https://t.me/ArshY0X)


---

🛠 توسعه داده شده با ❤️ توسط [آرشیا عابدی](https://github.com/Arshiaabedi) , [ایلیا عابدی](https://github.com/iliag556)
