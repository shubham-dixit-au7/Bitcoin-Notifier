<h1> BitCoin Notifier </h1>

<h3> Bitcoin  </h3>
Bitcoin emerged out of the 2008 global economic crisis when big banks were caught misusing borrowers' money, manipulating the system, and charging exorbitant fees. To address such issues, Bitcoin creators wanted to put the owners of bitcoins in-charge of the transactions, eliminate the middleman, cut high interest rates and transaction fees, and make transactions transparent. They created a distributed network system, where people could control their funds in a transparent way. Bitcoin has grown rapidly and spread far in a relatively short period of time. Across the world, companies from a large jewellery chain in the US, to a private hospital in Poland, accept bitcoin currency. Multi-billion-dollar corporations such as Dell, PayPal, Microsoft, Expedia, etc., are dealing in bitcoins. Websites promote bitcoins, magazines are publishing bitcoin news, and forums are discussing cryptocurrencies and trading in bitcoins. Bitcoin has its own Application Programming Interface (API), price index, trading exchanges and exchange rate. However, there are issues with bitcoins such as hackers breaking into accounts, high volatility of bitcoins, and long transaction delays. Elsewhere, particularly people in third world countries find Bitcoins as a reliable channel for transacting money bypassing pesky intermediaries.

<h3> IFTTT </h3>
What is IFTTT? If This Then That, also known as IFTTT is a freeware web-based service that creates chains of simple conditional statements, called applets. An applet is triggered by changes that occur within other web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest. What is Telegram?

<h3> Telegram </h3>
Telegram is a cloud-based instant messaging and voice over IP service. Telegram client apps are available for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type. Telegram's client-side code is open-source software but the source code for recent versions is not always immediately published, whereas its server-side code is closed-source and proprietary. The service also provides APIs to independent developers. In March 2018, Telegram stated that it had 200 million monthly active users. Default messages and media in Telegram are encrypted when stored on its servers, but can be accessed by the Telegram service provider, who holds the encryption keys. In addition Telegram provides optional end-to-end encrypted "secret" chats between two online users, yet not for groups or channels. The client-server communication is also encrypted. The service provides end-to-end encryption for voice calls.

<h3> Project Overview: </h3>

• This Project will send notification of bitcoin latest price for every one hour. 

• The notifications will be sent to telegram channel “Bitcoin Notifier” , email notification and a text message. 

• The channel is global and anyone can access the channel and get regular updates of bitcoin prices.

<h3> Features: </h3> 

• Notifications are sent when price is increased from threshold value on your phone and email is sent to the linked email id.

• General notifications of price updates occur on Telegram channel "Bicoin Notifier". Anyone with the link can join and chat along the     channel.

• General notifications are also sent as a text message to numbers linked with the service.

<h3> Working Procedure: </h3>

• Project runs under Virtual Environment Setup. 

 pip install virtualenv

 virtualenv --version

 virtualenv bitcoin_notifier

 pip install requests==2.18.4

 C:\Users\SHIELD\Desktop\bitcoin_notifier\Scripts\activate.bat

• The Project is divided into four functions/modules: 

 get_bitcoin_price() – Here I have used request module to collect data from source(‘blockchain.com’), Once it gets data it will convert the data into json format which is returned back to the function. 

 post_bitcoin_price() – Here the formatted data is sent to users as notifications once it acquires data from previous module. 

 format_bitcoin_history() - The main objective of this module is to format the notification message which will be sent to users.

 main()  – Here it will integrate all the steps and sets up timer to repeat the process at certain intervals.

• IFTTT Applets: 

 Webhooks, Telegram, Notifications, Email and Android SMS services are used here. 

 When an event 'bitcoin_price_emergency is occurred in the webhooks it will send the event value to Notification in your phone and an email is sent to the email listed in the service.

 When and event 'bitcoin_price_update is occurred in the webhooks it will send the event value to the Telegram Channel 'Bitcoin Notifier' and text message to the phone number linked to the service.



Credentials-

Webhooks Key- tsFD78FzQe6DYQNPMKrB4

Telegram Channel Link- (@bitcoin_notifier)https://t.me/bitcoin_notifier

Email linked to the service- shbmdxt@gmail.com

Phone Number linked to the service- +917905655943
