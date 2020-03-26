This project makes use of HTTP requests and how to send them appropriately using the 'requests' package.

We also make use of webhooks and how we can use them to connect our application to external services, such as phone notifications or Telegram messages.

With relatively litttle code (~50 lines) we're going to arrive at a fully-fledged Bitcoin price notification service that will be easily extendable to other cryptocurrencies and services.

Bitcoin price is a fickle thing. You never know where it's going to be at the end of the day. So, instead of checking various sites for the latest updates, we'll make a python app to do the work for us.

For this, we're going to use the popular automation website IFTTT. IFTTT ("if this, then that") is a web service that bridges the gap between different apps and devices.

We're going to create two IFTTT applets:
- One for emergency notification when Bitcoin price falls under a certain threshold; and
- another for regular Telegram updates on the Bitcoin price.

Both will be triggered by our Python app which will consume data from the Coinmarketcap API.

An IFTTT applet is composed of two parts:
1. a trigger and
2. an action.

In our case, the trigger will be a webhook service provided by IFTTT.

Our app will make an HTTP request to the webhook URL which will trigger an action. The action could be almost anything we want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.

Project Setup
Python 3 virtual environment:

$ mkvirtualenv -p $(which python3) bitcoin_notifications

Activating the virtual environment and installing the required dependencies:

$ workon bitcoin_notifications 		# To activate the virtual environment
$ pip install requests==2.18.4 		# We only need the requests package

We can deactivate the virtual environment by running the 'deactivate' shell command.