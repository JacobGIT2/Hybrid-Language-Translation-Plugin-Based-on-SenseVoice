from telethon import TelegramClient, events
import asyncio
from inference import process_audio
import os


api_id = 0  # 替换为您的 API ID
api_hash = ''  # 替换为您的 API hash
phone = ''

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.message.audio:
        audio = event.message.audio
        file_path = await event.message.download_media()
        text = process_audio(file_path)
        if os.path.exists(file_path):  # 检查文件是否存在
            os.remove(file_path)
        print(text)
        await event.reply(text)

async def main():
    await client.start(phone)
    print("客户端已启动，正在监听新消息...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
