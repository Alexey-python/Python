from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

equation = ''
Labeler = Label(text="lo", size_hint = (.33, .15), pos_hint={"center_x":0.4,"center_y":0.85}, font_size = 100)

class MyCalculatorApp(App):
    def build(self):

        Window.size = (480,720)
        layout = FloatLayout()

        ButtonZero = Button(text="0", size_hint = (.33, .15), pos_hint={"center_x":0.5,"center_y":0.05}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonZero.bind(on_press=self.ButtonZero_press)
        layout.add_widget(ButtonZero)

        ButtonEight = Button(text="8", size_hint = (.33, .15), pos_hint={"center_x":0.5,"center_y":0.2}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonEight.bind(on_press=self.ButtonEight_press)
        layout.add_widget(ButtonEight)

        ButtonFive = Button(text="5", size_hint = (.33, .15), pos_hint={"center_x":0.5,"center_y":0.35}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonFive.bind(on_press=self.ButtonFive_press)
        layout.add_widget(ButtonFive)
    
        ButtonTwo = Button(text="2", size_hint = (.33, .15), pos_hint={"center_x":0.5,"center_y":0.5}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonTwo.bind(on_press=self.ButtonTwo_press)
        layout.add_widget(ButtonTwo)

        ButtonOne = Button(text="1", size_hint = (.33, .15), pos_hint={"center_x":0.17,"center_y":0.5}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonOne.bind(on_press=self.ButtonOne_press)
        layout.add_widget(ButtonOne)

        ButtonFour = Button(text="4", size_hint = (.33, .15), pos_hint={"center_x":0.17,"center_y":0.35}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonFour.bind(on_press=self.ButtonFour_press)
        layout.add_widget(ButtonFour)

        ButtonSeven = Button(text="7", size_hint = (.33, .15), pos_hint={"center_x":0.17,"center_y":0.2}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonSeven.bind(on_press=self.ButtonSeven_press)
        layout.add_widget(ButtonSeven)

        ButtonThree = Button(text="3", size_hint = (.33, .15), pos_hint={"center_x":0.83,"center_y":0.5}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonThree.bind(on_press=self.ButtonThree_press)
        layout.add_widget(ButtonThree)

        ButtonSix = Button(text="6", size_hint = (.33, .15), pos_hint={"center_x":0.83,"center_y":0.35}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonSix.bind(on_press=self.ButtonSix_press)
        layout.add_widget(ButtonSix)

        ButtonNine = Button(text="9", size_hint = (.33, .15), pos_hint={"center_x":0.83,"center_y":0.2}, font_size = 100, background_color = (0.0, 33.0, 55.0, 0.5))
        ButtonNine.bind(on_press=self.ButtonNine_press)
        layout.add_widget(ButtonNine)

        ButtonMinus = Button(text="-", size_hint = (.33, .15), pos_hint={"center_x":0.83,"center_y":0.05}, font_size = 100, background_color = (165.0, 255.0, 0.0, 0.5))
        ButtonMinus.bind(on_press=self.ButtonMinus_press)
        layout.add_widget(ButtonMinus)

        ButtonPlus = Button(text="+", size_hint = (.33, .15), pos_hint={"center_x":0.17,"center_y":0.05}, font_size = 100, background_color = (165.0, 255.0, 0.0, 0.5))
        ButtonPlus.bind(on_press=self.ButtonPlus_press)
        layout.add_widget(ButtonPlus)

        ButtonDivision = Button(text="/", size_hint = (.33, .15), pos_hint={"center_x":0.17,"center_y":0.65}, font_size = 100, background_color = (165.0, 255.0, 0.0, 0.5))
        ButtonDivision.bind(on_press=self.ButtonDivision_press)
        layout.add_widget(ButtonDivision)

        ButtonMultiplication = Button(text="X", size_hint = (.33, .15), pos_hint={"center_x":0.5,"center_y":0.65}, font_size = 100, background_color = (165.0, 255.0, 0.0, 0.5))
        ButtonMultiplication.bind(on_press=self.ButtonMultiplication_press)
        layout.add_widget(ButtonMultiplication)

        ButtonAnswer = Button(text="=", size_hint = (.33, .15), pos_hint={"center_x":0.83,"center_y":0.65}, font_size = 100, background_color = (165.0, 255.0, 0.0, 0.5))
        ButtonAnswer.bind(on_press=self.ButtonAnswer_press)
        layout.add_widget(ButtonAnswer)


        ButtonAnswer.bind(on_press=self.ButtonAnswer_press)
        layout.add_widget(Labeler)

        return layout

    def ButtonZero_press(self, instance):
        global equation
        global Labeler
        equation += '0'
        Labeler.text = equation
    def ButtonEight_press(self, instance):
        global equation
        equation += '8'
        global Labeler
        Labeler.text = equation
    def ButtonFive_press(self, instance):
        global equation
        equation += '5'
        global Labeler
        Labeler.text = equation
    def ButtonTwo_press(self, instance):
        global equation
        equation += '2'
        global Labeler
        Labeler.text = equation
    def ButtonOne_press(self, instance):
        global equation
        equation += '1'
        global Labeler
        Labeler.text = equation
    def ButtonFour_press(self, instance):
        global equation
        equation += '4'
        global Labeler
        Labeler.text = equation
    def ButtonSeven_press(self, instance):
        global equation
        equation += '7'
        global Labeler
        Labeler.text = equation
    def ButtonSix_press(self, instance):
        global equation
        equation += '6'
        global Labeler
        Labeler.text = equation
    def ButtonThree_press(self, instance):
        global equation
        equation += '3'
        global Labeler
        Labeler.text = equation
    def ButtonNine_press(self, instance):
        global equation
        equation += '9'
        global Labeler
        Labeler.text = equation
    def ButtonMinus_press(self, instance):
        global equation
        equation += '-'
        global Labeler
        Labeler.text = equation
    def ButtonPlus_press(self, instance):
        global equation
        equation += '+'
        global Labeler
        Labeler.text = equation
    def ButtonDivision_press(self, instance):
        global equation
        equation += '/'
        global Labeler
        Labeler.text = equation
    def ButtonMultiplication_press(self, instance):
        global equation
        equation += '*'
        global Labeler
        Labeler.text = equation
    def ButtonAnswer_press(self, instance):
        global equation
        Labeler.text = str(eval(equation))
    

if __name__ == "__main__":
    MyCalculatorApp().run()