from utils.API_Classes import HeadHunterAPI, SuperJobAPI
from utils.json_saver import JSONSaver
from utils.vacancy import format_vacancies, filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    print("Выберите платформу(ы) для поиска вакансий:")

    while True:
        filtered_vacancies = []

        chosen_platform = input("HeadHunter - 1, SuperJob - 2, обе - 3\n")
        if chosen_platform not in ["1", "2", "3"]:
            print("Неверный выбор. Попробуйте снова")
            continue

        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

        for page in range(10):
            if chosen_platform == "1":
                hh_vacancies = hh_api.get_vacancies(search_query, page)
                formatted_hh_vacancies = format_vacancies(hh_vacancies)
                filtered_vacancies.extend(filter_vacancies(formatted_hh_vacancies, filter_words))
            elif chosen_platform == "2":
                superjob_vacancies = superjob_api.get_vacancies(search_query, page)
                formatted_sj_vacancies = format_vacancies(superjob_vacancies)
                filtered_vacancies.extend(filter_vacancies(formatted_sj_vacancies, filter_words))
            else:
                hh_vacancies = hh_api.get_vacancies(search_query, page)
                superjob_vacancies = superjob_api.get_vacancies(search_query, page)
                formatted_hh_vacancies = format_vacancies(hh_vacancies)
                formatted_sj_vacancies = format_vacancies(superjob_vacancies)
                filtered_vacancies.extend(filter_vacancies(formatted_hh_vacancies, filter_words) + filter_vacancies(formatted_sj_vacancies, filter_words))

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            continue

        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)

        user_answer_1 = input("Добавить в файл? (y/n) ")
        if user_answer_1 == "y":
            for vac in top_vacancies:
                json_saver.add_vacancy(vac)

        user_answer_2 = input("Посмотреть вакансии в файле по зарплате? (y/n) ")
        if user_answer_2 == "y":
            salary_from, salary_to = input("Введите через пробел мин. и макс. зарплаты: ").split()
            for vac in json_saver.get_vacancies_by_salary(salary_from, salary_to):
                print(vac)
        else:
            break

        break


if __name__ == "__main__":
    user_interaction()
