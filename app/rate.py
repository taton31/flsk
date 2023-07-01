import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_rate(cur_from, cur_to, value):
    today = datetime.now().strftime('%d/%m/%Y')
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + today)


    rate = dict()
    root = ET.fromstring(response.text)
    for valute in root.findall('Valute'):
        rate[valute.find('CharCode').text] = float(valute.find('Value').text.replace(',','.')) / float(valute.find('Nominal').text.replace(',','.'))
    rate['RUB'] = 1

    return (rate[cur_from] / rate[cur_to]) * value
