# Telegram Bot for Fetching Cryptocurrency Pair Data
This is a Telegram bot developed in Python that allows you to retrieve information about cryptocurrency pairs using the DexScreener API. The bot enables you to search for specific pairs and displays details such as price, volume, price changes, and liquidity.

## Requirements
Python 3.x
Python packages: requests, telebot
## Setup
Obtain a Telegram bot token by following the instructions in the official documentation.
Replace 'BOT_TOKEN' in the code with your Telegram bot token.
## Usage
Run the main.py script to start the bot.
Open a conversation with the bot on Telegram.
Use the /price command followed by the symbol or contract of the cryptocurrency you want to search for. For example: /price WBTC or /price 0x4585fe77225b41b697c938b018e2ac67ac5a20c0.
The bot will respond with information about the found cryptocurrency pair.
## Additional Commands
/request_count: Displays the total number of requests made to the bot.
Contributions
Contributions to this project are welcome. If you want to make improvements or corrections, you can fork the repository, make the changes, and submit a pull request.

## Acknowledgments
This bot is based on the DexScreener API and utilizes the telebot library for Telegram integration.

# Notes
Please note that the bot uses the DexScreener API to fetch cryptocurrency pair data. Ensure that the API is up and running and accessible.
