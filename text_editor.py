#задание 4
import tkinter as tk
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        self.filename = None
        self.text_modified = False  # Флаг изменения текста

        self.create_menu()
        self.create_text_widget()

        # Обработчик закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить как", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_editor)

        menubar.add_cascade(label="Файл", menu=file_menu)
        self.root.config(menu=menubar)

    def create_text_widget(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text.yview)

        # Отслеживание изменений в тексте
        self.text.bind("<KeyRelease>", self.mark_as_modified)

    def mark_as_modified(self, event=None):
        """Помечает текст как изменённый"""
        self.text_modified = True

    def open_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        if not filepath:
            return

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
                self.filename = filepath
                self.text_modified = False  # Сбрасываем флаг при открытии
                self.root.title(f"Текстовый редактор - {filepath}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{str(e)}")

    def save_as(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        if not filepath:
            return

        self._save_to_file(filepath)

    def _save_to_file(self, filepath):
        """Общая логика сохранения в файл"""
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)
                self.filename = filepath
                self.text_modified = False  # Сбрасываем флаг после сохранения
                self.root.title(f"Текстовый редактор - {filepath}")
            return True
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")
            return False

    def save_changes(self):
        """Сохранение изменений с проверкой имени файла"""
        if self.filename:
            return self._save_to_file(self.filename)
        else:
            return self.save_as() is not None

    def exit_editor(self):
        """Выход через меню"""
        self.on_closing()

    def on_closing(self):
        """Обработчик закрытия окна"""
        if not self.text_modified:
            self.root.destroy()
            return

        # Создаём своё окно с тремя кнопками
        save_box = tk.Toplevel(self.root)
        save_box.title("Простой редактор")
        save_box.resizable(False, False)

        # Центрируем окно
        window_width = 300
        window_height = 120
        screen_width = save_box.winfo_screenwidth()
        screen_height = save_box.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        save_box.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Сообщение
        msg = tk.Label(save_box, text="Текст был изменён. \nСохранить изменения?")
        msg.pack(pady=10)

        # Кнопки
        btn_frame = tk.Frame(save_box)
        btn_frame.pack(pady=5)

        def on_yes():
            save_box.destroy()
            if self.save_changes():
                self.root.destroy()

        def on_no():
            save_box.destroy()
            self.root.destroy()

        def on_cancel():
            save_box.destroy()

        tk.Button(btn_frame, text="Да", width=8, command=on_yes).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Нет", width=8, command=on_no).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Отмена", width=8, command=on_cancel).pack(side=tk.LEFT, padx=5)

        save_box.transient(self.root)
        save_box.grab_set()
        self.root.wait_window(save_box)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.geometry("600x400")
    root.mainloop()