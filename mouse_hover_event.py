import tkinter as tk
from tkinter import messagebox


class HoverApp:
    def __init__(self, master):
        self.master = master
        master.title("Hover")  # Устанавливаем заголовок окна

        # Создаем Label с начальным текстом
        self.label = tk.Label(
            master,
            text="Не трогай.",
            font=('Arial', 12),
            fg='black',
            justify='center'  # Выравнивание текста по центру
        )
        self.label.pack(expand=True, fill='both')  # Размещаем label с возможностью расширения

        # Привязываем события мыши
        self.label.bind("<Enter>", self.on_mouse_enter)  # <Enter> - аналог MouseHover
        self.label.bind("<Leave>", self.on_mouse_leave)  # Дополнительно - возврат к исходному состоянию

    def on_mouse_enter(self, event):
        #Обработчик события наведения курсора на label
        self.label.config(
            text="ERROR!!!",
            fg='red'
        )
        messagebox.showerror(
            "Fatal ERROR!",
            "Написано же\nНЕ трогать!"
        )

    def on_mouse_leave(self, event):
        #Обработчик события когда курсор уходит с label
        self.label.config(
            text="Не трогай.",
            fg='black'
        )


# Создаем и запускаем приложение
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")  # Устанавливаем размер окна
    app = HoverApp(root)
    root.mainloop()