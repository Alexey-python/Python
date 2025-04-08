import GPUtil
import psutil
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

gpus = GPUtil.getGPUs()
print(psutil.cpu_percent())
if gpus:
    for gpu in gpus:
        print(gpu.id)
        print(f"Название: {gpu.name}")
        print(f"Загрузка: {gpu.load*100:.2f}%")
        print(f"Использование памяти: {gpu.memoryUtil*100:.2f}%")
        print(f"Температура: {gpu.temperature:.2f}°C")
        print("-" * 20)
else:
    print("GPU не обнаружено.")

def Labeler(layout, posX, posY, text):
    layout.add_widget(Label(text=str(text), pos_hint={"center_x":posX,"center_y":posY}, font_size = 50))


class MyCalculatorApp(App):
    def build(self):

        Window.size = (1920,1080)
        Window.fullscreen = 'auto'
        Window.clearcolor = (.1, .1, .9, 1)

        layout = FloatLayout()
        Labeler(layout, 0.05, 0.1, f'ГП ID: {gpu.id}')
        Labeler(layout, 0.27, 0.2, f'Название ГП: {gpu.name}')
        Labeler(layout, 0.12, 0.3, f"Загрузка ГП: {gpu.load*100:.2f}%")
        Labeler(layout, 0.23, 0.4, f"Использование видеопамяти: {gpu.memoryUtil*100:.2f}%")
        Labeler(layout, 0.15, 0.5, f"Температура ГП: {gpu.temperature:.2f}°С")

        Labeler(layout, 0.11, 0.6, f"Загрузка ЦП: {psutil.cpu_percent()}%")
        Labeler(layout, 0.18, 0.7, f"Количество процессоров: {psutil.cpu_count()}")
        Labeler(layout, 0.36, 0.8, f"Частота ЦП: {psutil.cpu_freq()}")

        return layout

if __name__ == "__main__":
    MyCalculatorApp().run()