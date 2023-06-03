import requests
import telebot

bot_token = 'BOT_TOKEN'
request_count = 0
# Función para enviar mensajes al bot
def bot_send_text(chat_id, bot_message):
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={bot_message}'
    response = requests.get(send_text)
    return response.json()

# Función para obtener los datos del par seleccionado
def get_pair_data(chat_id, pair_query):
    url = f"https://api.dexscreener.com/latest/dex/search?q={pair_query}"
    found = False

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Filtrado de pares
        for pair in data['pairs']:
            txns_h24 = pair['txns']['h24']
            if pair['baseToken']['symbol'] == pair_query or pair['baseToken']['address'] == pair_query:
                found = True
                pair_symbol = pair['baseToken']['symbol']

                if pair['priceChange']['h24'] > 0:
                    bot_send_text(chat_id, f"◽◽{pair_symbol}/USDC◽◽\n\n🔗Chain: {pair['chainId']}\n💵Price : ${pair['priceUsd']}\n📗Buys: {txns_h24['buys']} 📕Sells: {txns_h24['sells']}\n💸Volume 24hs: ${pair['volume']['h24']}\n🟢Price change: +{pair['priceChange']['h24']}%\n🏦 Liquidity: ${pair['liquidity']['usd']}\n{pair['url']} ")
                else:
                    bot_send_text(chat_id, f"◽◽{pair_symbol}/USDC◽◽\n\n🔗Chain: {pair['chainId']}\n💵Price : ${pair['priceUsd']}\n📗Buys: {txns_h24['buys']} 📕Sells: {txns_h24['sells']}\n💸Volume 24hs: ${pair['volume']['h24']}\n🔴Price change: {pair['priceChange']['h24']}%\n🏦 Liquidity: ${pair['liquidity']['usd']}\n{pair['url']} ")
                break
        
        if not found:
            bot_send_text(chat_id, "Contract or symbol not found.")
            
    except requests.exceptions.RequestException as e:
        bot_send_text(chat_id, "An error occurred while making the request. Please try again later.")

# Función principal
def main():
    bot = telebot.TeleBot(bot_token)

    # Comando personalizado /get_data
    @bot.message_handler(commands=['price'])
    def handle_get_data(message):
        global request_count
        request_count += 1
        # Guardamos el ID del usuario
        chat_id = message.chat.id

        # Obtenemos el parámetro después del comando
        command = message.text.split()
        if len(command) > 1:
            pair_query = command[1]
            get_pair_data(chat_id, pair_query)
        else:
            bot_send_text(chat_id, "Add coin symbol or contract \nExample: \n/price WBTC\n/price 0x4585fe77225b41b697c938b018e2ac67ac5a20c0")
    # Comando personalizado /request_count
    @bot.message_handler(commands=['request_count'])
    def handle_request_count(message):
        bot_send_text(message.chat.id, f"Total requests: {request_count}")

    bot.polling()

if __name__ == '__main__':
    main()
