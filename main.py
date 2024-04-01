import requests

from constants import ALPHA_VANTAGE_API_KEY


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


#TODO: CUANDO EL PRECIO DEL STOCK VARIE POR UN 5% ENTRE AYER Y ANTES DE AYER IMPRIMIMOS EN CONSOLA EL MSJ 'GET NEWS'
#USAMOS LA API DE 'https://www.alphavantage.co' PARA ACCEDER A ESTA INFORMACION

alphavantage_api='https://www.alphavantage.co/query'


#parametros que le pasaremos a nuestra API
parameters ={
    'function':'TIME_SERIES_DAILY',
    'symbol':'IBM',
    'apikey':ALPHA_VANTAGE_API_KEY
}


#making a GET request
response = requests.get(alphavantage_api, params=parameters)


#imprimos es codigo de estado de la peticion para saber si fue exitosa o no
print(response.status_code)
