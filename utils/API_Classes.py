from abc import ABC, abstractmethod
import requests


class ApiClient(ABC):
    @abstractmethod
    def get_vacancies(self, vacancy):
        pass


class HeadHunterAPI(ApiClient):
    def get_vacancies(self, vacancy):
        url = "https://api.hh.ru/vacancies"
        response = requests.get(url, params={"text": vacancy})
        return response.json()


class SuperJobAPI(ApiClient):
    def get_vacancies(self, vacancy):
        secret_key = "v3.r.137694277.7ae90664952b2dc2a83b0940a5d08ef0d3bbd30b.d3362aa40e4240913e37d2150527a455127b7ace"
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {"X-Api-App-Id": secret_key}
        params = {"keyword": vacancy}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
