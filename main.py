from datetime import date, datetime, timedelta
import requests
from constants import *
from newsapi import NewsApiClient
from twilio.rest import Client

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
print(final_value)
print(initial_value)

# #calculamos la variacion del precio del stock (ayer y antes deayer), para saber si disminuyo o incrementu el valor del stock
delta_stock=final_value-initial_value
print(delta_stock)


# calculamos el delta stock en cambio porcentual
# porcentual_increment=((valor Final-valor inicial)/valor inicial )x 100
porcentual_increment=((final_value-initial_value)/initial_value)*100
print(porcentual_increment)


if abs(porcentual_increment)>=0.2:
    print('get news')


    #TODO: USAMOS LA API DE https://newsapi.org PARA OBETENER LAS NOTICIAS RELACIONADAS CON NUESTRO STOCK 
    news_api="https://newsapi.org/v2/everything"


    #calculando la fecha de ayer con datatime
    today = date.today()
    yesterday = today - timedelta(days = 1)

    #parametros que le pasaremos a nuestra API, de acuerdo a la documentacion de la API
    news_parameters ={
        'apiKey':NEWS_API_KEY,
        'q':COMPANY_NAME,
        'searchIn':'title', #para restringir nuestra busqueda simplemente a los titulos de las noticias
        'language':'en', 
        'sortBy':'popularity',
                
    }


    #making a GET request
    response = requests.get(news_api, params=news_parameters)


    #imprimos es codigo de estado de la peticion para saber si fue exitosa o no
    print(response.status_code)


    #retorna un HTTPError para saber si un error ocurre durante el proceso
    print(response.raise_for_status)


    #imprimos la informacion en formato json()
    json_response=response.json()
    print(json_response)


    #las noticias se encuentran guardadas en el diccionario con valor 'articles', articles es una lista de diccionarios
    news_data=json_response['articles']
    print()
    # print(f'noticias: {news_data[0]}')
    # print(news_data)
    # print()
    # print(type(news_data))
    # print()
    # print(len(news_data))

    #creamos una lista de nuestras noticias
    news_list=news_data[:3]
        
    # print(news_list)
    # print(len(news_list))
    # print(type(news_list))
    
    
#TODO: USAMOS LA API DE https://www.twilio.com PARA ENVIAR UN MENSAJE A NUESTRO CELULAR, CON EL % DE CAMBIO, TITULO Y DESCRIPCION DE LA NOTICIA


    #mensaje que enviaremos a nuestro email
    # Extraemos  el título, la descripción y la URL de la primera noticia de la lista de noticias.
    first_news_title=news_list[0]['title']
    first_news_description=news_list[0]['description']
    first_news_url=news_list[0]['url']


    # Hacemos lo mismo para la segunda noticia.
    second_news_title=news_list[1]['title']
    second_news_description=news_list[1]['description']
    second_news_url=news_list[1]['url']


    # Y finalmente, para la tercera noticia.
    third_news_title=news_list[2]['title']
    third_news_description=news_list[2]['description']
    third_news_url=news_list[2]['url']


    # Después de tener toda la información necesaria, creamos un mensaje que contiene el título, la descripción y la URL de cada noticia.
    # Estás utilizando el formato de cadena f para insertar las variables directamente en la cadena.
    # \n se utiliza para crear una nueva línea, lo que ayuda a hacer que el mensaje sea más legible.
    msg=f"STOCKNAME:{STOCK}\nSTOCK PRICE VARIATION:{delta_stock}\nVARIATION PERCENTAGE:({round(porcentual_increment, 2)}%\n\nTITLE:{first_news_title}\nDESCRIPTION:{first_news_description}\nURL:{first_news_url}\n\n\nTITLE:{second_news_title}\nDESCRIPTION:{second_news_description}\nURL:{second_news_url}\n\n\nTITLE:{third_news_title}\nDESCRIPTION:{third_news_description}\nURL:{third_news_url}"

    
    client = Client(account_sid, auth_token)
    

    message = client.messages.create(
        
    from_='+14243560102',
    to='+817045317684',
    body=msg,
    )

    print(message.sid)


