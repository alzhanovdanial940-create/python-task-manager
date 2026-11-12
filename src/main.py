# src/main.py

def add_task(tasks, task):
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nСписок задач:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Задача '{removed}' удалена.")
    else:
        print("Некорректный индекс.")

if __name__ == "__main__":
    todo_list = []
    add_task(todo_list, "Купить хлеб")
    add_task(todo_list, "Выполнить лабораторную работа №3")
    show_tasks(todo_list)
    remove_task(todo_list, 0)
    show_tasks(todo_list)

def search_tasks(tasks, keyword):
    """Ищет задачи, содержащие ключевое слово, и выводит их."""
    found_tasks = [t for t in tasks if keyword.lower() in t.lower()]
    
    print(f"\nРезультаты поиска по запросу '{keyword}':")
    if not found_tasks:
        print("Ничего не найдено.")
        return
    
    for i, task in enumerate(found_tasks, 1):
        print(f"{i}. {task}")
def print_menu():
    print("\n" + "=" * 30)
    print("📋 МЕНЕДЖЕР ЗАДАЧ (CLI)")
    print("=" * 30)
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Найти задачу")
    print("4. Выход")
    print("=" * 30)

if __name__ == "__main__":
    todo_list = ["Купить хлеб", "Сделать лабораторную по Git"]
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            show_tasks(todo_list)
        elif choice == "2":
            new_task = input("Введите текст задачи: ")
            todo_list.append(new_task)
            print("✅ Задача добавлена!")
        elif choice == "3":
            query = input("Введите слово для поиска: ")
            search_tasks(todo_list, query)
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("❌ Неверный ввод!! , попробуйте снова.")
        