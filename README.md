# randombot

یک بات ساده تلگرام برای ارسال تصادفی محتواهای مختلف مثل کمیک، میم، عکس گربه، عکس سگ و پروفایل تصادفی انسان به کاربر!

---

## ویژگی‌ها

- ارسال کمیک تصادفی از XKCD
- ارسال میم تصادفی
- ارسال عکس گربه و سگ با اندازه تصادفی
- ارسال اطلاعات و عکس پروفایل تصادفی انسان (با استفاده از randomuser.me)
- کیبورد سفارشی برای راحتی انتخاب انواع محتوا توسط کاربر

---

## نصب و راه‌اندازی

### پیش‌نیازها

- پایتون ۳.۷ یا جدیدتر
- نصب کتابخانه‌های مورد نیاز:
  - `pyTelegramBotAPI`
  - `requests`

### مراحل نصب

۱. مخزن را کلون کنید:
```bash
git clone https://github.com/amirebayati/randombot.git
cd randombot
```

۲. کتابخانه‌های مورد نیاز را نصب کنید:
```bash
pip install pyTelegramBotAPI requests
```

۳. توکن بات تلگرام خود را جایگزین کنید:
در فایل `randombot.py` مقدار `'api token'` را با توکن بات تلگرام خود جایگزین کنید.

۴. اجرای بات:
```bash
python randombot.py
```

---

## نحوه استفاده

- دستور `/start` را ارسال کنید تا کیبورد بات فعال شود.
- با استفاده از دکمه‌ها می‌توانید:
  - کمیک تصادفی دریافت کنید
  - میم تصادفی دریافت کنید
  - عکس گربه یا سگ دریافت کنید
  - پروفایل تصادفی انسان دریافت کنید

---

## API های مورد استفاده

- XKCD: دریافت کمیک تصادفی
- imgflip: دریافت میم تصادفی
- placekitten: عکس تصادفی گربه
- dog.ceo: عکس تصادفی سگ
- randomuser.me: پروفایل تصادفی انسان

---

## توسعه‌دهنده

[@amirebayati](https://github.com/amirebayati)

---

# randombot (English)

A simple Telegram bot that sends random content such as comics, memes, kitten/dog images, and random user profiles to users!

## Features

- Send random XKCD comics
- Send random memes
- Send random kitten and dog images
- Send random user profiles (name, email, phone, avatar)
- Custom keyboard for easy access to bot functions

## Installation

### Prerequisites

- Python 3.7+
- Install required libraries:
  - `pyTelegramBotAPI`
  - `requests`

### Steps

1. Clone the repository:
```bash
git clone https://github.com/amirebayati/randombot.git
cd randombot
```

2. Install dependencies:
```bash
pip install pyTelegramBotAPI requests
```

3. Replace `'api token'` in `randombot.py` with your Telegram bot token.

4. Run the bot:
```bash
python randombot.py
```

## Usage

- Send `/start` to the bot to activate the custom keyboard.
- Use the buttons to get random comics, memes, kitten/dog images, or a random user profile.

## APIs Used

- XKCD for comics
- imgflip for memes
- placekitten for kitten images
- dog.ceo for dog images
- randomuser.me for random user profiles

## Author

[@amirebayati](https://github.com/amirebayati)
