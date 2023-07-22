import json
import os
from abc import ABC, abstractmethod


class WorkWithVacancies(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(WorkWithVacancies):
    """Класс для добавления, получения, удаления вакансий в JSON файл"""
    SAVER_FILE = "vacancies.json"

    def add_vacancy(self, vacancy):
        data = {"name": vacancy.name, "url": vacancy.url, "salary": vacancy.salary, "description": vacancy.description}
        if os.path.exists(self.SAVER_FILE):
            with open(self.SAVER_FILE, encoding="utf-8") as f:
                current_data = json.load(f)
            current_data.append(data)
            with open(self.SAVER_FILE, 'w', encoding="utf-8") as f:
                json.dump(current_data, f, ensure_ascii=False, indent=4)
        else:
            with open(self.SAVER_FILE, 'w', encoding="utf-8") as f:
                json.dump([data], f, ensure_ascii=False, indent=4)

    def get_vacancies_by_salary(self, salary):
        suitable_vacancies = []
        if "-" in salary:
            frm, to = salary.replace(" ", "").strip("руб.eurEURsdUSDРУБ").split("-")
            with open(self.SAVER_FILE, encoding="utf-8") as f:
                current_data = json.load(f)
            for data in current_data:
                if int(frm) <= data["salary"] <= int(to):
                    suitable_vacancies.append(data)
        else:
            slr = int(salary.replace(" ", "").strip("руб.eurEURsdUSDРУБ"))
            with open(self.SAVER_FILE, encoding="utf-8") as f:
                current_data = json.load(f)
            for data in current_data:
                if data["salary"] == slr:
                    suitable_vacancies.append(data)

        return suitable_vacancies

    def delete_vacancy(self, vacancy):
        with open(self.SAVER_FILE, encoding="utf-8") as f:
            current_data = json.load(f)
        for data in current_data:
            if data["url"] == vacancy.url:
                current_data.remove(data)
        with open(self.SAVER_FILE, 'w', encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)
