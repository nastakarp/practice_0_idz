#задание 5
import tkinter as tk
from tkinter import ttk, messagebox


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисование фигур")

        # Переменные для хранения координат
        self.coords = []

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Notebook для переключения между разными типами фигур
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Создаем вкладки
        self.create_line_tab()
        self.create_triangle_tab()
        self.create_ellipse_tab()
        self.create_filled_shapes_tab()

    def create_line_tab(self):
        #Вкладка для рисования линии
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Линия")

        # Элементы управления
        frame = ttk.LabelFrame(tab, text="Координаты линии")
        frame.pack(padx=10, pady=10, fill=tk.X)

        labels = ["X1:", "Y1:", "X2:", "Y2:"]
        self.line_entries = []

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=0, column=i * 2, padx=5)
            entry = ttk.Entry(frame, width=8)
            entry.grid(row=0, column=i * 2 + 1, padx=5)
            self.line_entries.append(entry)

        # Установим значения по умолчанию
        self.line_entries[0].insert(0, "50")
        self.line_entries[1].insert(0, "50")
        self.line_entries[2].insert(0, "150")
        self.line_entries[3].insert(0, "150")

        # Кнопка рисования
        ttk.Button(tab, text="Нарисовать линию", command=self.draw_line).pack(pady=10)

        # Холст для рисования
        self.line_canvas = tk.Canvas(tab, bg="white", width=400, height=300)
        self.line_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_triangle_tab(self):
        #Вкладка для рисования треугольника
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Треугольник")

        # Элементы управления
        frame = ttk.LabelFrame(tab, text="Координаты вершин")
        frame.pack(padx=10, pady=10, fill=tk.X)

        labels = ["X1:", "Y1:", "X2:", "Y2:", "X3:", "Y3:"]
        self.triangle_entries = []

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=i // 2, column=(i % 2) * 2, padx=5)
            entry = ttk.Entry(frame, width=8)
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=5)
            self.triangle_entries.append(entry)

        # Установим значения по умолчанию
        self.triangle_entries[0].insert(0, "100")
        self.triangle_entries[1].insert(0, "50")
        self.triangle_entries[2].insert(0, "50")
        self.triangle_entries[3].insert(0, "150")
        self.triangle_entries[4].insert(0, "150")
        self.triangle_entries[5].insert(0, "150")

        # Кнопка рисования
        ttk.Button(tab, text="Нарисовать треугольник", command=self.draw_triangle).pack(pady=10)

        # Холст для рисования
        self.triangle_canvas = tk.Canvas(tab, bg="white", width=400, height=300)
        self.triangle_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_ellipse_tab(self):
        #Вкладка для рисования эллипса и окружности
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Эллипс/Окружность")

        # Элементы управления
        frame = ttk.LabelFrame(tab, text="Параметры фигуры")
        frame.pack(padx=10, pady=10, fill=tk.X)

        labels = ["X:", "Y:", "Ширина:", "Высота:"]
        self.ellipse_entries = []

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=0, column=i * 2, padx=5)
            entry = ttk.Entry(frame, width=8)
            entry.grid(row=0, column=i * 2 + 1, padx=5)
            self.ellipse_entries.append(entry)

        # Установим значения по умолчанию
        self.ellipse_entries[0].insert(0, "50")
        self.ellipse_entries[1].insert(0, "50")
        self.ellipse_entries[2].insert(0, "100")
        self.ellipse_entries[3].insert(0, "150")

        # Кнопки рисования
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Нарисовать эллипс", command=lambda: self.draw_ellipse(False)).pack(side=tk.LEFT,
                                                                                                       padx=5)
        ttk.Button(btn_frame, text="Нарисовать окружность", command=lambda: self.draw_ellipse(True)).pack(side=tk.LEFT,
                                                                                                          padx=5)

        # Холст для рисования
        self.ellipse_canvas = tk.Canvas(tab, bg="white", width=400, height=300)
        self.ellipse_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_filled_shapes_tab(self):
        #Вкладка для рисования закрашенных фигур
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Закрашенные фигуры")

        # Элементы управления
        frame = ttk.LabelFrame(tab, text="Выберите фигуру")
        frame.pack(padx=10, pady=10, fill=tk.X)

        self.shape_var = tk.StringVar()
        shapes = ["Прямоугольник", "Эллипс", "Окружность"]

        for shape in shapes:
            rb = ttk.Radiobutton(frame, text=shape, variable=self.shape_var, value=shape)
            rb.pack(anchor=tk.W, padx=5, pady=2)

        self.shape_var.set(shapes[0])

        # Кнопка рисования
        ttk.Button(tab, text="Нарисовать фигуру", command=self.draw_filled_shape).pack(pady=10)

        # Холст для рисования
        self.filled_canvas = tk.Canvas(tab, bg="white", width=400, height=300)
        self.filled_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def get_coords(self, entries):
        #Получение координат из полей ввода
        try:
            return [int(entry.get()) for entry in entries]
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа для координат")
            return None

    def draw_line(self):
        #Рисование линии
        coords = self.get_coords(self.line_entries)
        if coords is None:
            return

        self.line_canvas.delete("all")
        self.line_canvas.create_line(*coords, fill="green", width=2)

    def draw_triangle(self):
        #Рисование треугольника
        coords = self.get_coords(self.triangle_entries)
        if coords is None:
            return

        self.triangle_canvas.delete("all")

        # Рисуем 3 линии разными цветами
        self.triangle_canvas.create_line(coords[0], coords[1], coords[2], coords[3], fill="black", width=2)
        self.triangle_canvas.create_line(coords[2], coords[3], coords[4], coords[5], fill="red", width=2)
        self.triangle_canvas.create_line(coords[4], coords[5], coords[0], coords[1], fill="blue", width=2)

    def draw_ellipse(self, is_circle):
        #Рисование эллипса или окружности
        coords = self.get_coords(self.ellipse_entries)
        if coords is None:
            return

        self.ellipse_canvas.delete("all")

        if is_circle:
            # Для окружности используем минимальный размер из ширины и высоты
            size = min(coords[2], coords[3])
            coords[2] = size
            coords[3] = size

        self.ellipse_canvas.create_oval(
            coords[0], coords[1],
            coords[0] + coords[2], coords[1] + coords[3],
            outline="black", width=2
        )

    def draw_filled_shape(self):
        #Рисование закрашенной фигуры
        self.filled_canvas.delete("all")

        shape = self.shape_var.get()
        x, y, width, height = 60, 60, 120, 180

        if shape == "Прямоугольник":
            self.filled_canvas.create_rectangle(
                x, y, x + width, y + height,
                fill="orange", outline="black"
            )
        elif shape == "Эллипс":
            self.filled_canvas.create_oval(
                x, y, x + width, y + height,
                fill="orange", outline="black"
            )
        elif shape == "Окружность":
            size = min(width, height)
            self.filled_canvas.create_oval(
                x, y, x + size, y + size,
                fill="orange", outline="black"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.geometry("600x500")
    root.mainloop()