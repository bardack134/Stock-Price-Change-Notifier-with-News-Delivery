# Stock-Price-Change-Notifier-with-News-Delivery

This project uses Python to monitor the price of a stock (TSLA for Tesla Inc) and sends a text message via Twilio API when the price changes by more than 1% between yesterday and the day before yesterday. It also search news related to the company using the NewsAPI and includes this news in the text message.

**Tools**


**requests**: Python library to send HTTP requests, allowing the program to interact with web APIs to search data.

**Twilio**: Twilio is a platform that lets you send text messages to your cellphone from your apps using APIs.

**Alpha Vantage API**: provides stock prices, technical indicators, and other financial data, helping the program stay updated on stocks.

**NewsAPI**: gives access to news from online sources, helping the program fetch recent news about companies and stocks.
