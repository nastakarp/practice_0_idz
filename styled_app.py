#задание 3
import tkinter as tk
from tkinter import ttk, font


class StyledApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Доска объявлений")
        self.root.geometry("600x400")

        # Настройка фонового изображения
        self.bg_image = tk.PhotoImage(file="butterfly.png")
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создание элементов
        self.create_widgets()

    def create_widgets(self):
        # Метка с настраиваемым шрифтом
        custom_font = font.Font(family="Arial", size=14, weight="bold", slant="italic")
        self.label = tk.Label(
            self.root,
            text="",
            font=custom_font,
            fg="white",
            bg="#333333",
            wraplength=500,  # Перенос текста, если он не помещается
            justify="center"  # Выравнивание по центру
        )
        self.label.pack(pady=20)

        # Поле ввода
        self.text_box = tk.Entry(self.root, width=40)
        self.text_box.pack(pady=10)

        # Кнопка с измененным цветом
        style = ttk.Style()
        style.configure(
            "Custom.TButton",
            foreground="black",
            background="#4CAF50",
            font=('Helvetica', 12),
            padding=10
        )
        self.button = ttk.Button(
            self.root,
            text="Отобразить текст",
            style="Custom.TButton",
            command=self.update_label
        )
        self.button.pack(pady=20)

    def update_label(self):
        self.label.config(text=self.text_box.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = StyledApp(root)
    root.mainloop()