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
Описание: {self.description}"""

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from
