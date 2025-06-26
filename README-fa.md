<div dir="rtl" align="right">

# ربات ارسال پیام با دکمه شیشه‌ای - راهنمای کامل

## پیش نمایش

<p align="center">
  <img src="Images/Screenshot_2025-05-05-00-48-26-676_org.telegram.messenger.jpg" alt="Bot Preview">
</p>

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

- BTC: `bc1q94at0ecvv2ldcp4wx373npvn5tssu7z78yp9dk`
- ETH: `0xF4e732262D4e2ADbb3Ac00C887b247188EF230D9` 
- USDT (BEP20): `0xF4e732262D4e2ADbb3Ac00C887b247188EF230D9`
- TRX (TRC20): `TTvrTWctxRxG9mQmbVpCjRkoDazCWjcPYF`
- LTC: `ltc1q897dhng7s0m9nlytkaujzs6r33a2qv8ey3xwue`

از حمایت شما از توسعه نرم افزارهای متن باز متشکریم!

---
## ✉️ ارتباط با توسعه دهنده
- ایمیل: arshiag556@gmail.com
- تلگرام: [@ArshY0X](https://t.me/ArshY0X)

---

🛠 توسعه داده شده با ❤️ توسط [آرشیا عابدی](https://github.com/Arshiag556) و [ایلیا عابدی](https://github.com/iliag556)
</div>