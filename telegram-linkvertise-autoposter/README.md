# Telegram Linkvertise Autoposter Bot 🤖

A Python bot that automatically posts promotional or affiliate links (e.g. Linkvertise URLs) with images and captions to a Telegram channel.

## 🚀 Features
- Automatically posts content from a CSV file
- Inline "Tutorial" button in each post
- Configurable delay between posts
- Uses .env for secure API tokens

## 🗂️ Project Structure
```
bot.py            # Main bot script
.env.example      # Example environment config
requirements.txt  # Python dependencies
models.csv        # Sample data file
```

## ⚙️ Setup

1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/telegram-linkvertise-autoposter.git
   cd telegram-linkvertise-autoposter
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment file
   ```bash
   cp .env.example .env
   ```
   Then edit .env and fill in your TELEGRAM_BOT_TOKEN and TELEGRAM_CHANNEL_ID.

4. Edit your CSV
   Add your own image URLs, names, and Linkvertise links inside models.csv.

5. Run the bot
   ```bash
   python bot.py --csv models.csv --delay 100
   ```

## 🧰 Tech Stack
- Python 3.10+
- python-telegram-bot
- dotenv

## 📜 License
MIT License © 2025
