import os
from abc import ABC, abstractmethod
import requests


class ApiClient(ABC):
    """Класс для получения вакансий с помощью API"""
    @abstractmethod
    def get_vacancies(self, vacancy, page=None):
        pass


class HeadHunterAPI(ApiClient):
    def get_vacancies(self, vacancy, page=None):
        url = "https://api.hh.ru/vacancies"
        response = requests.get(url, params={"per_page": 100, "page": page, "text": vacancy})
        return response.json()["items"]


class SuperJobAPI(ApiClient):
    def get_vacancies(self, vacancy, page=None):
        secret_key = os.getenv('SJ_API_KEY')
        url = "https://api.superjob.ru/2.0/vacancies/"
        response = requests.get(url, headers={"X-Api-App-Id": secret_key}, params={"count": 100,
                                                                                   "page": page,
                                                                                   "keyword": vacancy})
        return response.json()["objects"]
