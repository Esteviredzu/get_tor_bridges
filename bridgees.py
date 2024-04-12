from telethon.sync import TelegramClient
import time
import os
import CONFIG

api_id = CONFIG.api_id
api_hash = CONFIG.api_hash

client = TelegramClient('user_session', api_id, api_hash)

async def main():
    async with client:
        await client.send_message('@GetBridgesBot', 'Bridges')
        time.sleep(4)
        messages = await client.get_messages('@GetBridgesBot', limit=1)
        try:
            with open("bridges.txt", "w") as file:
                for message in messages:
                    file.write(message.message)
            os.system("cat bridges.txt")
        except:
            for message in messages:
                print(message.message)

client.loop.run_until_complete(main())
