import requests
from requests.exceptions import RequestException

def obter_previsao_do_tempo(city_id, api_key):
    url = f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção se a resposta não for bem-sucedida
        data = response.json()
        return data
    except RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
        return None
    except ValueError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

def main():
    api_key = '6cf13588b57142f0c752e3831d138664'
    city_id = 'SUA_CIDADE'  # Substitua pela sua cidade
    previsao = obter_previsao_do_tempo(city_id, api_key)

    if previsao:
        for dia in previsao.get('data', []):
            print(f"Data: {dia['date']}")
            print(f"Condição: {dia['text_icon']['text']['phrase']['reduced']}")
            print(f"Temperatura máxima: {dia['temperature']['max']}°C")
            print(f"Temperatura mínima: {dia['temperature']['min']}°C")
            print("=" * 30)

if __name__ == "__main__":
    main()
