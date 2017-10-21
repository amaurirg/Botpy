import xmltodict
import requests
from siglas import tempo_clima
import datetime


date_pt = {'Sunday': 'Domingo', 'Monday': 'Segunda', 'Tuesday': 'Terça', 'Wednesday': 'Quarta',
           'Thursday': 'Quinta', 'Friday': 'Sexta', 'Saturday': 'Sábado'}


def req_clima():
    temp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/244/previsao.xml')  # para 4 dias

    dct_temp = xmltodict.parse(temp.text)

    with open("templates/previsao.md", "w") as file_w:
        file_w.write('Previsão para os próximos 4 dias\n\n')
        file_w.write('*{0} - {1}*\n\n'.format(dct_temp['cidade']['nome'], dct_temp['cidade']['uf']))

        for item in dct_temp['cidade']['previsao']:
            dia = item['dia'].split('-')
            date_week = datetime.datetime(int(dia[0]), int(dia[1]), int(dia[2])).strftime('%A')
            file_w.write('*{0}* - {1}/{2}\n'.format(date_pt[date_week], dia[2], dia[1]))
            tempo = tempo_clima(item['tempo'])
            file_w.write(tempo + '\n')
            file_w.write('Mín: {0}° - Máx: {1}°\n\n'.format(item['minima'], item['maxima']))

        atualizado = dct_temp['cidade']['atualizacao'].split('-')
        file_w.write('_(Atualizado em {0}/{1}/{2})_'.format(atualizado[2], atualizado[1], atualizado[0]))
