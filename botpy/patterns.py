from bottery.conf.patterns import Pattern
from bottery.message import render
from bottery.views import pong
import clima, datetime, re, os


def hello(message):
    return render(message, 'hello.md')


def tempclima(message):
    with open("templates/previsao.md") as file_r:
        texto = file_r.read()
        data = re.search(r'[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
    if  data.group() == datetime.datetime.now().strftime('%d/%m/%Y'):
        pass
    else:
        clima.req_clima()
    return render(message, 'previsao.md')

patterns = [
    Pattern('ping', pong),
    Pattern('Ping', pong),
    Pattern('hello', hello),
    Pattern('Hello', hello),
    Pattern('Olá', hello),
    Pattern('olá', hello),
    Pattern('Ola', hello),
    Pattern('ola', hello),
    Pattern('clima', tempclima),
    Pattern('Clima', tempclima),
    # Pattern('')
]
