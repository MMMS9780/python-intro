#タスクを管理するデータ構造の設定
tasks = []

#タスクを追加する関数
def add_task(task):
    tasks.append(task)
    print(f'タスク "{task}" を追加しました。')

#タスクを表示する関数
def show_tasks():
    if not tasks:
        print("タスクはありません。")
    else:
        print("タスク一覧:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

#タスクを削除する関数
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'タスク "{removed_task}" を削除しました。')
    else:
        print("無効なタスク番号です。")

#メインループ
def main():
    while True:
        print("\n1.タスクを追加")
        print("2.タスクを表示")
        print("3.タスクを削除")
        print("4.終了")

        choice = input("選択してください: ")

        if choice == '1':
            task = input("タスクを入力してください: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            task_number = int(input("削除するタスク番号を入力してください: "))
            delete_task(task_number)
        elif choice == '4':
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度試してください。")

if __name__ == "__main__":
    main()