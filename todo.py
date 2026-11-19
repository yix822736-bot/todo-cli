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

#1添加
def add_task(tasks):
    title = input("待办内容：")
    tasks.append({"title": title, "done": False})
    print("已添加")

#2查看
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

#3完成
def done_task(tasks):
    show_tasks(tasks)
    idx = ask_index(tasks, "要完成第几条：")
    if idx is None:
        return
    tasks[idx]["done"] = True
    print("已标记完成")

#4删除
def delete_task(tasks):
    show_tasks(tasks)
    idx = ask_index(tasks, "要删除第几条：")
    if idx is None:
        return
    removed = tasks.pop(idx)
    print(f"已删除：{removed['title']}")

#读编号
def ask_index(tasks, prompt):
    raw = input(prompt)
    try:
        n = int(raw)
    except ValueError:
        print("请输入数字编号")
        return None
    if n < 1 or n > len(tasks):
        print("编号不存在")
        return None
    return n - 1


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



