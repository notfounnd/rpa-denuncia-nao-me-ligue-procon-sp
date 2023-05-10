from auth_user import get_access_token
import requests
import json
import csv

url = 'https://api.bloqueio.procon.sp.gov.br/v1/ChatMessage/CreateReport'

token = get_access_token()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}


def generate_phone_number_dict():
    with open('files/phone_number_list.csv', 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        phone_number_dict = []

        for row in csv_reader:
            phone_number_dict.append(row)

        return phone_number_dict

def generate_report(phone_number_dict):
    for phone in phone_number_dict:
        
        naomeligue_meu_telefone = phone['naomeligue_meu_telefone']
        naomeligue_empresa_enchendo_saco = phone['naomeligue_empresa_enchendo_saco']
        naomeligue_numero_enchendo_saco = phone['naomeligue_numero_enchendo_saco']
        naomeligue_data = phone['naomeligue_data']
        naomeligue_hora = phone['naomeligue_hora']
        naomeligue_motivo = phone['naomeligue_motivo']

        payload = json.dumps([
            {
                'chatMessageId': 17,
                'chatMessage': None,
                'textButton': 'Ligação',
                'input': False,
                'inputType': None,
                'select': True,
                'answerDescription': 'Qual foi o meio do contato',
                'urlForOptions': 'GetContactForms',
                'referenceOptionId': 26,
                'property': 'ContactForms',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 26,
                'createdAt': '2021-05-05T18:01:41.98',
                'updatedAt': '2021-05-05T18:01:42.3433333'
            },
            {
                'chatMessageId': 4,
                'textButton': f'{naomeligue_numero_enchendo_saco}',
                'input': True,
                'inputType': 'text',
                'select': False,
                'answerDescription': 'Qual o número que entrou em contato',
                'urlForOptions': None,
                'referenceOptionId': None,
                'property': 'calledNumber',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': True,
                'id': 6,
                'createdAt': '2019-07-27T18:26:12.237',
                'updatedAt': '2021-05-05T18:01:42.3433333'
            },
            {
                'chatMessageId': 18,
                'chatMessage': None,
                'textButton': 'Venda de Produto ou Serviço',
                'input': False,
                'inputType': None,
                'select': True,
                'answerDescription': 'Qual foi o motivo do contato',
                'urlForOptions': 'GetContactReasons',
                'referenceOptionId': 5,
                'property': 'ContactReasons',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 27,
                'createdAt': '2021-05-05T18:01:41.98',
                'updatedAt': '2021-05-05T18:01:42.3433333'
            },
            {
                'chatMessageId': 6,
                'chatMessage': None,
                'textButton': 'Internet Banda Larga',
                'input': False,
                'inputType': None,
                'select': True,
                'answerDescription': 'Qual produto foi oferecido',
                'urlForOptions': 'GetProducts',
                'referenceOptionId': None,
                'property': 'product',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 7,
                'createdAt': '2019-07-29T08:06:50.553',
                'updatedAt': None
            },
            {
                'chatMessageId': 14,
                'textButton': f'{naomeligue_empresa_enchendo_saco}',
                'input': True,
                'inputType': 'text',
                'select': False,
                'answerDescription': 'Qual empresa ofereceu este produto/serviço',
                'urlForOptions': None,
                'referenceOptionId': 9,
                'property': 'supplier',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 21,
                'createdAt': '2019-07-29T08:08:27.527',
                'updatedAt': None
            },
            {
                'chatMessageId': 15,
                'chatMessage': None,
                'textButton': f'{naomeligue_meu_telefone}',
                'input': False,
                'inputType': None,
                'select': False,
                'answerDescription': 'Em qual número você recebeu este contato',
                'urlForOptions': 'GetPhones',
                'referenceOptionId': 31,
                'property': 'receivedNumber',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 22,
                'createdAt': '2019-07-29T08:08:27.527',
                'updatedAt': '2021-05-05T18:01:42.3433333'
            },
            {
                'chatMessageId': 22,
                'chatMessage': None,
                'textButton': 'Vivo',
                'input': False,
                'inputType': None,
                'select': True,
                'answerDescription': 'Operadora de telefonia da sua linha telefônica',
                'urlForOptions': 'GetTelecomOperators',
                'referenceOptionId': 22,
                'property': 'telecomOperator',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 32,
                'createdAt': '2021-05-05T18:01:42.1233333',
                'updatedAt': '2021-05-05T18:01:42.3433333'
            },
            {
                'chatMessageId': 10,
                'textButton': f'{naomeligue_data}',
                'input': True,
                'inputType': 'date',
                'select': False,
                'answerDescription': 'Data do contato',
                'urlForOptions': None,
                'referenceOptionId': 10,
                'property': 'callDate',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 13,
                'createdAt': '2019-07-29T09:56:17.517',
                'updatedAt': '2021-05-05T18:01:42.31'
            },
            {
                'chatMessageId': 25,
                'textButton': f'{naomeligue_hora}',
                'input': True,
                'inputType': 'time',
                'select': False,
                'answerDescription': 'Horário do contato',
                'urlForOptions': None,
                'referenceOptionId': None,
                'property': 'callHour',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 36,
                'createdAt': '2021-07-19T20:41:08.8666667',
                'updatedAt': None
            },
            {
                'chatMessageId': 9,
                'textButton': f'{naomeligue_motivo}',
                'input': True,
                'inputType': 'textarea',
                'select': False,
                'answerDescription': 'Descrição',
                'urlForOptions': None,
                'referenceOptionId': None,
                'property': 'description',
                'urlForRedirect': None,
                'paramForSearch': None,
                'required': True,
                'phoneMask': False,
                'id': 12,
                'createdAt': '2019-07-29T09:48:20.633',
                'updatedAt': None
            }
        ], ensure_ascii=False).encode('utf-8')

        response = requests.request('POST', url, headers=headers, data=payload)

        try:
            print(response.json()['data'])
        except:
            print(f'Erro ao reportar: {naomeligue_numero_enchendo_saco}')

phone_number_dict = generate_phone_number_dict()
generate_report(phone_number_dict)
