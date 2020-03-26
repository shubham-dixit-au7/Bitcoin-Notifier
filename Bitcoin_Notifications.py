import time
from datetime import datetime
import requests

bitcoin_api_url = 'https://blockchain.info/ticker'
ifttt_webhooks_url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'
bitcoin_price_limiter = 500500

def get_bitcoin_price():
	response = requests.get(bitcoin_api_url)
	response_json = response.json()
	price = response_json['INR']['last']
	return price

def post_bitcoin_price(event,price):
	data = {'value1': price}
	# event = 'bitcoin_price_emergency'
	key ='d2WST2V5enRIzqonl1uQFR'
	url = ifttt_webhooks_url.format(event, key)
	requests.post(url, json=data)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        print(date)
        price = bitcoin_price['price']
        print(price)
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: <b>{}</b>₹'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)

def main():
    bitcoin_history = []
    while True:
        price = get_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < bitcoin_price_limiter:
            post_bitcoin_price('bitcoin_price_emergency', price)
        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5:
            post_bitcoin_price('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []
        
        time.sleep(1 * 5)  # Sleep for 5 minutes (for testing purposes you can set it to a lower number)
        

if __name__ == '__main__':
    main()


