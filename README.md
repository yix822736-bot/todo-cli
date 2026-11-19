# 待办清单 CLI

一个用 Python 编写的命令行待办事项工具。支持添加、查看、标记完成、删除待办，数据通过 JSON 文件持久化，退出后重新打开数据仍在。

## 功能
- 添加待办
- 查看待办列表（编号 + 完成状态）
- 标记某条为已完成
- 删除某条待办
- 退出自动保存到 tasks.json，启动自动加载

## 运行方式
需要 Python 3.10 及以上：

    python todo.py

## 技术点
- 数据结构：列表 + 字典（每条待办是 {"title": ..., "done": ...}）
- 功能按函数拆分：add_task / show_tasks / done_task / delete_task
- JSON 文件读写：json.dump 保存、json.load 加载，with open 管理文件
- 输入校验：编号先转 int 再验范围，非法编号不崩溃

## 开发说明
本项目为 12 周 AI 应用开发冲刺的第一个项目，使用 AI 辅助工具协作完成。
