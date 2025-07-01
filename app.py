#задание 1
import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Копирование текста")
        self.root.geometry("400x300")

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Текстовое поле (аналог TextBox)
        self.text_box = ttk.Entry(self.root, width=30)
        self.text_box.pack(pady=20)

        # Кнопка (аналог Button)
        self.button = ttk.Button(
            self.root,
            text="Копировать",
            command=self.copy_text
        )
        self.button.pack(pady=10)

        # Метка (аналог Label)
        self.label = ttk.Label(self.root, text="", font=('Arial', 12))
        self.label.pack(pady=20)

    def copy_text(self):
        #Копирует текст из текстового поля в метку
        text = self.text_box.get()
        self.label.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()