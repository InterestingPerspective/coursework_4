class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url.strip("<>()[]{}")
        if "-" in salary:
            self.salary = int(salary.replace(" ", "").split("-")[0])
        else:
            self.salary = int(salary.replace(" ", "").strip("руб.eurEURsdUSDРУБ"))
        self.description = description

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary
