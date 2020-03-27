import requests as req
import json

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = req.get(url)
    if response.status_code != 200 or 'erro' in response.json():
        return 'Inexistente'
    data = response.json()
    return f"{data['logradouro']}; {data['complemento']}; {data['bairro']}; {data['uf']}"