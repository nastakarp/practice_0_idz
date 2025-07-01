#задание 2
import tkinter as tk
from tkinter import messagebox, ttk


class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма приветствия")
        self.root.geometry("400x250")

        # Создаем ToolTip (в Tkinter нет встроенного, создадим свой)
        self.create_tooltip_system()

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_tooltip_system(self):
        """Создаем систему для отображения подсказок"""
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.withdraw()
        self.tooltip.overrideredirect(True)
        self.tooltip_label = tk.Label(
            self.tooltip,
            text="",
            background="lightyellow",
            relief="solid",
            borderwidth=1,
            padx=5,
            pady=3
        )
        self.tooltip_label.pack()
        self.current_widget = None

        # Привязываем события мыши
        self.root.bind("<Enter>", self.schedule_tooltip)
        self.root.bind("<Leave>", self.hide_tooltip)

    def schedule_tooltip(self, event):
        """Запланировать показ подсказки"""
        widget = event.widget
        if hasattr(widget, "tooltip_text"):
            self.current_widget = widget
            self.root.after(500, self.show_tooltip)

    def show_tooltip(self):
        """Показать подсказку"""
        if self.current_widget:
            x, y, _, _ = self.current_widget.bbox("insert")
            x += self.current_widget.winfo_rootx() + 25
            y += self.current_widget.winfo_rooty() + 25

            self.tooltip_label.config(text=self.current_widget.tooltip_text)
            self.tooltip.geometry(f"+{x}+{y}")
            self.tooltip.deiconify()

    def hide_tooltip(self, event):
        """Скрыть подсказку"""
        self.current_widget = None
        self.tooltip.withdraw()
        self.root.after_cancel(self.show_tooltip)

    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Label "Name:"
        lbl_name = ttk.Label(self.root, text="Name:")
        lbl_name.pack(pady=(20, 5))

        # Инструкция
        lbl_instruction = ttk.Label(self.root, text="Напишите ваше имя.")
        lbl_instruction.pack(pady=(0, 10))

        # Поле ввода с подсказкой
        self.entry_name = ttk.Entry(self.root, width=25)
        self.entry_name.pack(pady=5)
        self.entry_name.tooltip_text = "Введите\nваше имя"  # Текст подсказки

        # Кнопка
        btn_submit = ttk.Button(
            self.root,
            text="Ввод",
            command=self.show_greeting
        )
        btn_submit.pack(pady=20)

    def show_greeting(self):
        """Показать приветствие в MessageBox"""
        name = self.entry_name.get()
        if name:
            messagebox.showinfo(
                "Приветствие",
                f"Здравствуй, {name}!"
            )
        else:
            messagebox.showwarning(
                "Ошибка",
                "Пожалуйста, введите ваше имя"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()