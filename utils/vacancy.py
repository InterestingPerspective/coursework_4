class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, vacancy):
        if len(vacancy) == 34:
            self.name = vacancy["name"]
            self.url = vacancy["alternate_url"]
            if vacancy["salary"] is None:
                self.salary_from = None
                self.salary_to = None
                self.currency = None
            else:
                self.salary_from = vacancy["salary"]["from"]
                self.salary_to = vacancy["salary"]["to"]
                self.currency = vacancy["salary"]["currency"]
            self.description = vacancy["snippet"]["requirement"]
        else:
            self.name = vacancy["profession"]
            self.url = vacancy["link"]
            self.salary_from = vacancy["payment_from"]
            self.salary_to = vacancy["payment_to"]
            self.currency = vacancy["currency"]
            self.description = vacancy["candidat"]

    def __str__(self):
        return f"""
Вакансия: {self.name}
Ссылка: {self.url}
Зарплата: {self.salary_from} {self.currency}
Описание: {self.description}\n"""

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from


def filter_vacancies(hh_or_sj_vacancies, filter_words):
    """Фильтрует вакансии по ключевым словам"""

    filtered_vacancies = []

    for vacancy in hh_or_sj_vacancies:
        for word in filter_words:
            if word.lower() in vacancy.description.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies


def format_vacancies(vacancies):
    """Создаёт список из объектов класса Vacancy с изменённой зарплатой"""

    formatted_vacancies = []

    for vacancy in vacancies:
        formatted_vacancy = Vacancy(vacancy)
        if formatted_vacancy.salary_from is None:
            formatted_vacancy.salary_from = 0
        formatted_vacancies.append(formatted_vacancy)

    return formatted_vacancies


def sort_vacancies(vacancies):
    """Сортирует вакансии по зарплате по убыванию"""

    sorted_vacancies = sorted(vacancies, key=lambda d: d.salary_from, reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies, top):
    """Возвращает top вакансий с самой большой зарплатой"""

    return vacancies[:top]


def print_vacancies(vacancies):
    """Выводит инфу по вакансиям"""
    for vacancy in vacancies:
        print(vacancy)
