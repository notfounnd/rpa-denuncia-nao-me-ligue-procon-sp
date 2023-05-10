import requests
import json

login = 'seu_usuario'
password = 'sua_senha'

url = 'https://api.bloqueio.procon.sp.gov.br/v1/User/login'

def get_access_token():

    payload = json.dumps({
        'name': login,
        'password': password,
        'type': 'Consumer',
        'typeDoc': 'CPF'
    })

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request('POST', url, headers=headers, data=payload)
    
    return response.json()['data']['token']
