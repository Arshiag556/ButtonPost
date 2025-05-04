<a id="فارسی"></a>
<div dir="rtl">

# 📝 ربات پست تلگرام - راهنمای کامل

## 🏷 عنوان پروژه
**ربات حرفه‌ای مدیریت پست کانال تلگرام**

## 🌟 ویژگی‌های کلیدی
- ساخت پست‌های متنی و تصویری
- افزودن دکمه‌های زیبا با لینک
- پشتیبانی از چندزبانی (فارسی/انگلیسی)
- امکان پیش‌نمایش قبل از ارسال
- محدودیت دسترسی برای ارسال به کانال

## 🛠 فناوری‌های استفاده شده
- پایتون ۳.۱۰ به بالا
- کتابخانه pyTelegramBotAPI
- JSON برای مدیریت زبان‌ها

## 📦 راهنمای نصب

### پیش‌نیازها
```bash
git clone https://github.com/Arshiaabedi/telegram-post-bot.git
cd telegram-post-bot
python -m venv venv
source venv/bin/activate  # لینوکس/مک
venv\Scripts\activate  # ویندوز
pip install -r requirements.txt
```

### تنظیمات
1. ایجاد فایل `config.py`:
```python
TOKEN = 'توکن_ربات_شما'  # از @BotFather دریافت کنید
CHANNEL_ID = '@آیدی_کانال'  # کانال مقصد
ADMIN_ID = 123456789  # آیدی عددی شما
```

2. تنظیم فایل `lang.json` با ترجمه‌های مورد نظر

### اجرای ربات
```bash
python bot.py
```

## 💰 حمایت مالی

از توسعه این پروژه با ارزهای دیجیتال حمایت کنید:

**ارزهای دیجیتال:**
- بیت‌کوین: `bc1qfe63rl66wplznzwzlys95gnetjrg8lx4gcysw7`
- اتریوم: `0xde0D7CD3bAeA6a64D4e28cF10B1ECB03C6a231EA` 
- تتر (BEP20): `0xde0D7CD3bAeA6a64D4e28cF10B1ECB03C6a231EA`
- ترون (TRC20): `TKj9AGcMK8Qz8utcWQ5ZhnyA9tcLxLBTxW`
- لایت‌کوین: `ltc1q0ycmvh0qd5fsaj89hhqp842yvxgtygk4n5zvsz`

## 🤝 مشارکت
1. انشعاب از مخزن
2. ایجاد شاخه جدید (`git checkout -b feature/feature-name`)
3. ثبت تغییرات (`git commit -m 'Add some feature'`)
4. ارسال به شاخه (`git push origin feature/feature-name`)
5. ایجاد درخواست ادغام

## 📜 مجوز
این پروژه تحت مجوز **MIT** منتشر شده است - جزئیات در فایل [LICENSE](LICENSE) موجود است.

## ✉️ ارتباط با توسعه‌دهنده
- ایمیل: arshiag556@gmail.com
- تلگرام: [@ArshY0X](https://t.me/ArshY0X)

</div>

---

🛠 توسعه داده شده با ❤️ توسط [آرشیا عابدی](https://github.com/Arshiaabedi), [ایلیا عابدی](https://github.com/iliag556)

