# ربات ارسال پیام با دکمه شیشه‌ای
 - راهنمای کامل

## 🏷 عنوان پروژه
**ربات حرفه ای مدیریت پست های کانال تلگرام**

## 🌟 ویژگی های کلیدی
- ایجاد پست های متنی و تصویری
- افزودن دکمه های زیبا با لینک
- پشتیبانی از چند زبان (فارسی/انگلیسی)
- پیش نمایش قبل از ارسال
- محدودیت دسترسی ارسال به کانال

## 🛠 فناوری های استفاده شده
- پایتون 3.10+
- کتابخانه pyTelegramBotAPI
- فایل JSON برای مدیریت زبان ها

## 📦 راهنمای نصب

### پیش نیازها
```bash
git clone https://github.com/Arshiag556/ButtonPost.git
cd ButtonPost
python -m venv venv
source venv/bin/activate  # برای لینوکس/مک
venv\Scripts\activate  # برای ویندوز
pip install -r requirements.txt
```

### پیکربندی
1. اطلاعات زیر را در فایل `main.py` تکمیل کنید:

```python
TOKEN = 'YOUR_BOT_TOKEN'  # از @BotFather
CHANNEL_ID = '@YOUR_CHANNEL'  # ایدی چنل
ADMIN_ID = 123456789  # ایدی عددی
```

2. فایل `lang.json` را با ترجمه های خود تنظیم کنید

### اجرای ربات
```bash
python main.py
```

## 🎯 مثال استفاده
```python
# نمونه کد برای توسعه دهندگان
from telebot import TeleBot

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "خوش آمدید!")
```

## 🤝 مشارکت
1. پروژه را فورک کنید
2. یک شاخه جدید ایجاد کنید (`git checkout -b feature/قابلیت_جدید`)
3. تغییرات را کامیت کنید (`git commit -m 'افزودن قابلیت جدید'`)
4. به شاخه فشار دهید (`git push origin feature/قابلیت_جدید`)
5. یک درخواست کش باز کنید

## 📜 مجوز
این پروژه تحت **مجوز MIT** منتشر شده است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

## 💰 حمایت مالی

از توسعه این پروژه با ارزهای دیجیتال حمایت کنید:

**ارزهای دیجیتال:**
- بیت کوین: `bc1qfe63rl66wplznzwzlys95gnetjrg8lx4gcysw7`
- اتریوم: `0xde0D7CD3bAeA6a64D4e28cF10B1ECB03C6a231EA` 
- تتر (BEP20): `0xde0D7CD3bAeA6a64D4e28cF10B1ECB03C6a231EA`
- ترون (TRC20): `TKj9AGcMK8Qz8utcWQ5ZhnyA9tcLxLBTxW`
- لایت کوین: `ltc1q0ycmvh0qd5fsaj89hhqp842yvxgtygk4n5zvsz`

از حمایت شما از توسعه نرم افزارهای متن باز متشکریم!

---
## ✉️ ارتباط با توسعه دهنده
- ایمیل: arshiag556@gmail.com
- تلگرام: [@ArshY0X](https://t.me/ArshY0X)

---

🛠 توسعه داده شده با ❤️ توسط [آرشیا عابدی](https://github.com/Arshiag556) و [ایلیا عابدی](https://github.com/iliag556)