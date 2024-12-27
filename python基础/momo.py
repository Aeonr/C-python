import tkinter as tk
import json
from tkinter import messagebox


class MemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("桌面备忘录")
        self.tasks = []  # 存储当前任务的列表
        self.completed_tasks = []  # 存储已完成任务的列表
        self.load_tasks()  # 加载任务
        self.load_completed_tasks()  # 加载已完成任务

        # 创建框架用于放置任务和完成按钮
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)
        self.update_task_frame()  # 初始化任务框架显示

        # 创建添加任务的按钮
        self.add_button = tk.Button(root, text="添加任务", command=self.open_add_task_window)
        self.add_button.pack(side=tk.TOP, pady=10)

        # 创建查看已完成任务的按钮
        self.view_completed_button = tk.Button(root, text="查看已完成任务", command=self.view_completed_tasks)
        self.view_completed_button.pack(side=tk.TOP, pady=10)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []
            messagebox.showerror("加载错误", "tasks.json 文件损坏，请检查文件内容。")

    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file)
        except Exception as e:
            messagebox.showerror("保存错误", f"保存 tasks.json 时出错: {str(e)}")

    def load_completed_tasks(self):
        try:
            with open("completed_tasks.json", "r") as file:
                self.completed_tasks = json.load(file)
        except FileNotFoundError:
            self.completed_tasks = []
        except json.JSONDecodeError:
            self.completed_tasks = []
            messagebox.showerror("加载错误", "completed_tasks.json 文件损坏，请检查文件内容。")

    def save_completed_tasks(self):
        try:
            with open("completed_tasks.json", "w") as file:
                json.dump(self.completed_tasks, file)
        except Exception as e:
            messagebox.showerror("保存错误", f"保存 completed_tasks.json 时出错: {str(e)}")

    def update_task_frame(self):
        # 清除任务框架中的所有子部件
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        for i, task in enumerate(self.tasks):
            # 创建一个框架来存放任务和完成按钮
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(pady=5)
            # 显示任务的标签
            task_label = tk.Label(task_frame, text=task)
            task_label.pack(side=tk.LEFT)
            # 创建完成任务的按钮
            complete_button = tk.Button(task_frame, text="完成", command=lambda index=i: self.complete_task(index))
            complete_button.pack(side=tk.LEFT, padx=10)
            # 创建编辑任务的按钮
            edit_button = tk.Button(task_frame, text="编辑", command=lambda index=i: self.edit_task(index))
            edit_button.pack(side=tk.LEFT, padx=10)

    def open_add_task_window(self):
        def add_task():
            task = entry.get()
            if task:
                self.tasks.append(task)
                self.save_tasks()
                self.update_task_frame()
                add_task_window.destroy()

        add_task_window = tk.Toplevel(self.root)
        add_task_window.title("添加任务")
        entry = tk.Entry(add_task_window, width=50)
        entry.pack(pady=10)
        save_button = tk.Button(add_task_window, text="保存", command=add_task)
        save_button.pack(pady=10)

    def complete_task(self, index):
        completed_task = self.tasks.pop(index)
        self.completed_tasks.append(completed_task)
        self.save_tasks()  # 保存当前任务
        self.save_completed_tasks()  # 保存已完成任务
        self.update_task_frame()  # 更新任务框架显示

    def view_completed_tasks(self):
        def delete_task():
            selected_index = completed_listbox.curselection()
            if selected_index:
                index = selected_index[0]
                if messagebox.askyesno("确认", "确定要删除该任务吗?"):  # 添加确认对话框
                    del self.completed_tasks[index]
                    self.save_completed_tasks()
                    self.view_completed_tasks()

        completed_window = tk.Toplevel(self.root)
        completed_window.title("已完成任务")
        completed_listbox = tk.Listbox(completed_window, height=20, width=50)
        completed_listbox.pack(pady=10)
        for task in self.completed_tasks:
            completed_listbox.insert(tk.END, task)
        # 仅添加一个删除按钮
        delete_button = tk.Button(completed_window, text="删除", command=delete_task)
        delete_button.pack(pady=10)
        close_button = tk.Button(completed_window, text="关闭", command=completed_window.destroy)
        close_button.pack(pady=10)

    def edit_task(self, index):
        def save_edited_task():
            edited_task = entry.get()
            if edited_task:
                self.tasks[index] = edited_task
                self.save_tasks()
                edit_task_window.destroy()
                self.update_task_frame()

        edit_task_window = tk.Toplevel(self.root)
        edit_task_window.title("编辑任务")
        entry = tk.Entry(edit_task_window, width=50)
        entry.insert(0, self.tasks[index])
        entry.pack(pady=10)
        save_button = tk.Button(edit_task_window, text="保存", command=save_edited_task)
        save_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoApp(root)
    root.mainloop()