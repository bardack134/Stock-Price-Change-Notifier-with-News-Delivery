from datetime import date, timedelta
import requests
from constants import ALPHA_VANTAGE_API_KEY


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


#TODO: CUANDO EL PRECIO DEL STOCK VARIE POR UN 5% ENTRE AYER Y ANTES DE AYER IMPRIMIMOS EN CONSOLA EL MSJ 'GET NEWS'
#USAMOS LA API DE 'https://www.alphavantage.co' PARA ACCEDER A ESTA INFORMACION
alphavantage_api='https://www.alphavantage.co/query'


#parametros que le pasaremos a nuestra API
alphavantage_parameters ={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':ALPHA_VANTAGE_API_KEY
}


#making a GET request
response = requests.get(alphavantage_api, params=alphavantage_parameters)


#imprimos es codigo de estado de la peticion para saber si fue exitosa o no
print(response.status_code)


#retorna un HTTPError para saber si un error ocurre durante el proceso
print(response.raise_for_status)


#imprimos la informacion en formato json()
json_response=response.json()
print(json_response)


# print(json_response['Time Series (Daily)'].keys()) #para acceder a las fecchas 
print(json_response['Time Series (Daily)']['2024-04-01']['4. close']) #para acceder al dato 'close' de la respectiva fecha 



#en esta lista guardaremos los datos de ayer y el dia anterior que se encuentren en nuestro json_response
data=[]


#usamos list comprehension para crear una lista con los valores 'close' de nuestro diccionario json_response    
data=[values for key, values in json_response['Time Series (Daily)'].items()]


#accediendo al valor 'close' del elemento de nuestro primer elemento y segundo elemento de nuestra lista de diccionarios 'data  
final_value=float((data[0]['4. close'])) #yesterday closing price
initial_value=float((data[1]['4. close']))# before closing price


# #calculamos la variacion del precio del stock (ayer y antes deayer), para saber si disminuyo o incrementu el valor del stock
delta_stock=final_value-initial_value
print(delta_stock)


# calculamos el delta stock en cambio porcentual
# porcentual_increment=((valor Final-valor inicial)/valor inicial )x 100
porcentual_increment=((final_value-initial_value)/initial_value)*100
print(porcentual_increment)


if porcentual_increment<=-0.2 and porcentual_increment>=0.2:
    print('get news')


 
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

