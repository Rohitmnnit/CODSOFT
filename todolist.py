import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create list to store tasks
        self.tasks = []

        # Create entry widget to input tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Create button to add tasks
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)

        # Create button to delete selected task
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
