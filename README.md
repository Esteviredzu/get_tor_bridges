# get_tor_bridges

## Code Explanation

This Python script utilizes the Telethon library to interact with the Telegram API. Here's a breakdown of its functionality:

1. Imports necessary modules.
2. Reads configuration data (API ID and API hash) from an external file named `CONFIG.py`.
3. Initializes a Telethon client using the provided API ID and API hash.
4. Defines an asynchronous function named `main()` which:
    - Sends a message to a Telegram bot named `@GetBridgesBot`.
    - Waits for 4 seconds.
    - Retrieves the last message from the chat with the bot.
    - Writes the message to a file named `bridges.txt` and prints its contents to the console.
5. Executes the `main()` function within a Telethon client loop.

## Obtaining Configuration Data

Before running the script, obtain the following configuration data:

- **API ID**: Obtain from the [Telegram API development platform](https://my.telegram.org/auth).
- **API Hash**: Provided when creating a new application on the Telegram API development platform.

Create a file named `CONFIG.py` in the script directory and define the following variables:

```python
# CONFIG.py

# Telegram API credentials
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
