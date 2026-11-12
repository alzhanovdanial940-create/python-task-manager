# src/main.py

def add_task(tasks, task):
    tasks.append(task)
    print(f"✅ Задача '{task}' добавлена!")

def show_tasks(tasks):
    if not tasks:
        print("📭 Список задач пуст.")
        return
    print("\n📋 Список задач:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Задача '{removed}' удалена.")
    else:
        print("❌ Некорректный индекс.")

def search_tasks(tasks, keyword):
    """Ищет задачи, содержащие ключевое слово, и выводит их."""
    found_tasks = [t for t in tasks if keyword.lower() in t.lower()]
    print(f"\n🔍 Результаты поиска по запросу '{keyword}':")
    if not found_tasks:
        print("Ничего не найдено.")
        return
    for i, task in enumerate(found_tasks, 1):
        print(f"{i}. {task}")

def export_tasks_to_file(tasks, filename="exported_tasks.txt"):
    """Экспортирует текущий список задач в текстовый файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=== СПИСОК ЗАДАЧ (ЭКСПОРТ) ===\n")
            for i, task in enumerate(tasks, 1):
                file.write(f"{i}. {task}\n")
        print(f"📁 Задачи успешно экспортированы в файл '{filename}'!")
    except Exception as e:
        print(f"❌ Ошибка при экспорте задач: {e}")

def print_menu():
    print("\n" + "=" * 40)
    print("📋 МЕНЕДЖЕР ЗАДАЧ (CLI) — ФИНАЛЬНАЯ ВЕРСИЯ")
    print("=" * 40)
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Найти задачу")
    print("4. Экспортировать задачи в файл")
    print("5. Выход")
    print("=" * 40)

if __name__ == "__main__":
    todo_list = ["Купить хлеб", "Сделать лабораторную по DevOps"]
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            show_tasks(todo_list)
        elif choice == "2":
            new_task = input("Введите текст задачи: ")
            if new_task.strip():
                add_task(todo_list, new_task)
            else:
                print("❌ Ошибка: пустая строка не допускается.")
        elif choice == "3":
            query = input("Введите слово для поиска: ")
            search_tasks(todo_list, query)
        elif choice == "4":
            export_tasks_to_file(todo_list)
        elif choice == "5":
            print("👋 Выход из программы...")
            break
        else:
            print("❌ Неверный ввод! , попробуйте снова.")