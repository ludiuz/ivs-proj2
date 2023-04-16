import PySimpleGUI as sg
from core import Engine

class Calculator:
    def __init__(self):
        self.result = ''
        self.window = sg.Window('Calculator', self._create_layout())

    def _create_layout(self):
        return [
            [sg.Text('', size=(15, 2), font=('Helvetica', 18), text_color='black', key='input')],
            [sg.Text('', size=(14, 2), font=('Helvetica', 12), text_color='black', key='imres')],
            [sg.Button('c', size=(7, 2)), sg.Button('odm', size=(7, 2))],
            [sg.Button('7', size=(7, 2)), sg.Button('8', size=(7, 2)), sg.Button('9', size=(7, 2)), sg.Button('/', size=(7, 2))],
            [sg.Button('4', size=(7, 2)), sg.Button('5', size=(7, 2)), sg.Button('6', size=(7, 2)), sg.Button('*', size=(7, 2))],
            [sg.Button('1', size=(7, 2)), sg.Button('2', size=(7, 2)), sg.Button('3', size=(7, 2)), sg.Button('-', size=(7, 2))],
            [sg.Button('.', size=(7, 2)), sg.Button('0', size=(7, 2)), sg.Button('=', size=(7, 2)), sg.Button('+', size=(7, 2))],
        ]

    def run(self):
        engine = Engine()
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Quit'):
                break
            if event == 'c':
                self.result = ''
                self.window['input'].update(self.result)
                self.window['imres'].update(self.result)
            elif event == 'odm':
                self.result = '(' + self.result + ')**(1/2)'
                self.window['input'].update(self.result)
            elif event == '=':
                Answer = engine.validate(self.result)
                Answer = str(round(float(Answer),3))
                self.window['input'].Update(Answer)
                self.result = Answer
            else:
                self.result += event
                self.window['input'].update(self.result)
            try:
                ans = round(float(eval(self.result)), 3)
                self.window['imres'].update(str(ans))
            except:
                self.window['imres'].update("Can't calculate...")

        self.window.close()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
