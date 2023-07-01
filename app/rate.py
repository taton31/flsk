import requests
import xml.etree.ElementTree as ET
import datetime

def get_rate(cur_from, cur_to, value):
    today = datetime.datetime.now().strftime('%d/%m/%Y')
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + today)


    rate = dict()
    root = ET.fromstring(response.text)
    for valute in root.findall('Valute'):
        rate[valute.find('Name').text] = float(valute.find('Value').text.replace(',','.')) / float(valute.find('Nominal').text.replace(',','.'))

    return (rate[cur_from] / rate[cur_to]) * value

print(get_rate('Венгерских форинтов', 'Турецких лир', 88))