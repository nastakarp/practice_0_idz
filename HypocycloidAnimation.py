import tkinter as tk
import numpy as np
from math import sin, cos, pi


class HypocycloidAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Анимация гипоциклоида с катящейся окружностью")

        # Параметры гипоциклоида
        self.k = 6  # число зубцов
        self.r = 20  # радиус маленькой окружности
        self.R = self.r * self.k  # радиус большой окружности
        self.t = 0
        self.speed = 0.05  # скорость

        self.cx, self.cy = 300, 300  # центр экрана

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Старт", command=self.start_animation)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Стоп", command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT)

        self.path_points = []
        self.animation_id = None

    def hypocycloid_point(self, t):
        k = self.k
        r = self.r
        x = r * (k - 1) * (cos(t) + cos((k - 1) * t) / (k - 1))
        y = r * (k - 1) * (sin(t) - sin((k - 1) * t) / (k - 1))
        return self.cx + x, self.cy - y

    def update_animation(self):
        if self.animation_id is None:
            return

        self.canvas.delete("all")

        # Вычисление текущей точки гипоциклоида
        x, y = self.hypocycloid_point(self.t)
        self.path_points.append((x, y))

        # Рисуем траекторию
        if len(self.path_points) > 1:
            self.canvas.create_line(self.path_points, fill="red", width=2)

        # Центр маленькой катящейся окружности
        R1 = self.r
        R2 = self.R
        center_x = self.cx + (R2 - R1) * cos(self.t)
        center_y = self.cy - (R2 - R1) * sin(self.t)

        # Рисуем большую окружность
        self.canvas.create_oval(
            self.cx - R2, self.cy - R2,
            self.cx + R2, self.cy + R2,
            outline="black"
        )

        # Рисуем маленькую окружность (катящуюся)
        self.canvas.create_oval(
            center_x - R1, center_y - R1,
            center_x + R1, center_y + R1,
            outline="blue"
        )

        # Рисуем линию от центра маленькой окружности к точке на окружности
        self.canvas.create_line(center_x, center_y, x, y, fill="black")

        # Рисуем точку на траектории
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="green", outline="green")

        # Следующий кадр
        self.t += self.speed
        if self.t > 2 * pi:
            self.t = 0
            self.path_points.clear()

        self.animation_id = self.root.after(50, self.update_animation)

    def start_animation(self):
        if self.animation_id is None:
            self.animation_id = self.root.after(0, self.update_animation)

    def stop_animation(self):
        if self.animation_id is not None:
            self.root.after_cancel(self.animation_id)
            self.animation_id = None


if __name__ == "__main__":
    root = tk.Tk()
    app = HypocycloidAnimation(root)
    root.mainloop()
