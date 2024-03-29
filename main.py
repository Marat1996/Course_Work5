from classes.db_manager import DBManager
from utils.utils import create_database, create_table, insert_data_into_tables


def main():
    db_name = "course_work5"
    create_database(db_name)
    print(f"База данных {db_name} создана успешно.")
    create_table(db_name)
    print("Таблицы созданы успешно.")
    insert_data_into_tables(db_name)
    print("Данные успешно добавлены в таблицы.")

    user_interaction(db_name)


def user_interaction():
    print(" Привет!\n"
          " Выберите команду:\n"
          " 1 - Список всех компаний и количесво их вакансий\n 2 - Список всех вакансий с информацией по каждой\n 3 - "
          "Узнать среднюю зарплату \n 4 - Списсок вакансий, у которых зарплата выше средней\n 5 - Поискать по ключевому "
          "слову\n")

    while True:
        user_input = input()
        if user_input in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Попробуйте еще раз")

    if user_input == "1":
        all_companies = DBManager("course_work5").get_companies_and_vacancies_count()
        print("Список всех компаний и количество их вакансий:")
        for company, vacancy_count in all_companies:
            print(f"{company}: {vacancy_count} вакансий")
    elif user_input == "2":
        all_vacancies = DBManager("course_work5").get_all_vacancies()
        print("Список всех вакансий с информацией по каждой:")
        for vacancy in all_vacancies:
            print(vacancy)
    elif user_input == "3":
        avg_salary = DBManager("course_work5").get_avg_salary()
        print("Средняя зарплата по вакансиям:")
        for row in avg_salary:
            avg_salary_from = row[0]
            print(f"Средняя зарплата от: {avg_salary_from}")
    elif user_input == "4":
        high_salary = DBManager("course_work5").get_vacancies_with_higher_salary()
        print("Список вакансий с зарплатой выше средней:")
        for vacancy in high_salary:
            print(vacancy)
    elif user_input == "5":
        keyword_input = input("Введите ключевое слово: ")
        vacancy_with_keyword = DBManager("course_work5").get_vacancies_with_keyword(keyword_input)
        print("Список вакансий по заданному ключевому слову:")
        for vacancy in vacancy_with_keyword:
            print(vacancy)


if __name__ == '__main__':
    while True:
        user_interaction()
        user_choice = input("Продолжить? (да/нет): ")
        if user_choice.lower() != "да":
            break
