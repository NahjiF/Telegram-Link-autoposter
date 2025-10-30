import asyncio
import csv
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)


async def post_item(name, image_url, link_url):
    caption = (
        f"😍💗💦 {name} 😍💗💦\n"
        f"Mega link below 👇\n{link_url}\n\n"
        f"Join @AsunaGallery for exclusive content!"
    )

    keyboard = [
        [InlineKeyboardButton("📘 Tutorial", url="https://t.me/+yBPUeZVXFcBjYzIx")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await bot.send_photo(
        chat_id=TELEGRAM_CHANNEL_ID,
        photo=image_url,
        caption=caption,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )

    print(f"✅ Posted: {name}")


async def autopost_from_csv(csv_path, delay_seconds):
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get("name")
            image_url = row.get("image_url")
            link_url = row.get("link_url")

            if not name or not image_url or not link_url:
                print(f"⚠️ Skipping row with missing data: {row}")
                continue

            try:
                await post_item(name, image_url, link_url)
                await asyncio.sleep(delay_seconds)
            except Exception as e:
                print(f"❌ Error posting {name}: {e}")
                continue


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, default="models.csv", help="Path to CSV file")
    parser.add_argument("--delay", type=int, default=100, help="Delay between posts (seconds)")
    args = parser.parse_args()

    asyncio.run(autopost_from_csv(args.csv, args.delay))
