import json
import os

FILE = "tasks.json"


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def add_task(tasks):
    title = input("待办内容：")
    tasks.append({"title": title, "done": False})
    print("已添加")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("暂无待办")
        return
    for i, t in enumerate(tasks):
        if t["done"]:
            mark = "✓"
        else:
            mark = " "
        print(f"{i + 1}. [{mark}] {t['title']}")


def done_task(tasks):
    show_tasks(tasks)
    n = int(input("要完成第几条："))
    if n < 1 or n > len(tasks):
        print("编号不存在")
        return
    tasks[n - 1]["done"] = True
    print("已标记完成")


def delete_task(tasks):
    show_tasks(tasks)
    n = int(input("要删除第几条："))
    if n < 1 or n > len(tasks):
        print("编号不存在")
        return
    removed = tasks.pop(n - 1)
    print(f"已删除：{removed['title']}")


tasks = load_tasks()

while True:
    print("1. 添加  2. 查看  3. 完成  4. 删除  5. 退出")
    choice = input("选一个：")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        done_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        save_tasks(tasks)
        print("再见")
        break
    else:
        print("没有这个选项")
