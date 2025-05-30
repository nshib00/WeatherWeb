from requests_html import HTMLSession
from dotenv import find_dotenv, load_dotenv
from os import getenv
from datetime import datetime


load_dotenv(find_dotenv())


class WeatherAPIService:
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    query_params = {
        "unitGroup": "metric",
        "lang": "ru",
        "key": getenv("API_KEY")
    }

    @classmethod
    def __build_query(cls, query: str) -> str:
        query += "?"
        for i, param in enumerate(cls.query_params.items()):
            p_name, p_value = param

            if i < len(cls.query_params) - 1:
                query += f"{p_name}={p_value}&"
            else:
                query += f"{p_name}={p_value}"
        return query


    @classmethod
    def get_today_weather(cls, city_query: str):
        today = datetime.now().strftime(r"%Y-%m-%d")
        request_url = cls.__build_query(f"{cls.url}/{city_query}/{today}")

        with HTMLSession() as session:
            response = session.get(request_url)
            print(request_url)

        return response.json()

