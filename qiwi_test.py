import requests
import json
import pyqiwi
login = ''
token = ''


def balance(login, api_access_token):
    s = requests.Session()
    s.headers['Accept']= 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + login + '/accounts')
    return b.json()

if __name__ == '__main__':
    print(balance(login, token))
