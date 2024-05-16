from telethon import TelegramClient, events
import asyncio
import re
import random
import string

API_ID = '25875948'
API_HASH = 'bbc8cd4753b320c932bd56254d2917a0'

async def start_bot():
    phone_number = input("Enter your phone number: ")
    session_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    client = TelegramClient(session_name, API_ID, API_HASH)
    
    # Send code request
    await client.start(phone=phone_number)
    try:
        await client.send_code_request(phone_number)
    except Exception as e:
        if "code expired" in str(e):
            await asyncio.sleep(10)  # Wait for 10 seconds before retrying
            await client.send_code_request(phone_number)
    
    # Sign in automatically
    code = input("Enter the code you received: ")
    await client.sign_in(phone=phone_number, code=code)
    
    # استعداد البوت للعمل
    group_urls = ['https://t.me/O7650', 'https://t.me/qwqwqwuy6']
    @client.on(events.NewMessage(chats=group_urls))
    async def handler(event):
        message = event.message
        if message.text:
            print("Received message:", message.text)  # Log the received message
            # استخراج الكلمة بعد "اول" باستخدام التعبير العادي
            match = re.search(r'اول\s+(\w+)', message.text)
            if match:
                word_to_send = match.group(1)
                print("Sending message:", word_to_send)  # Log the message being sent
                await message.reply(word_to_send)  # Reply to the message in the group
            # استخراج الكلمة بين القوسين بعد "اول"
            match = re.search(r'اول\s+\(([^)]+)\)', message.text)
            if match:
                word_to_send = match.group(1)
                print("Sending message:", word_to_send)  # Log the message being sent
                await message.reply(word_to_send)  # Reply to the message in the group
            # استخراج الكلمة بين الاقتباسات بعد "اول"
            match = re.search(r'اول\s+"([^"]+)"', message.text)
            if match:
                word_to_send = match.group(1)
                print("Sending message:", word_to_send)  # Log the message being sent
                await message.reply(word_to_send)  # Reply to the message in the group

    async with client:
        await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(start_bot())
