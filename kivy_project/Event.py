'''
The framework responds to user keypresses, mouse events, and touch events.
'''

from kivy.app import App
from kivy.uix.button import Button

class MAinApp(App):
    def build(self):
        button=Button(text='hello from kivy',
                      size_hint=(.5,.5),
                      pos_hint={'center_x':.5,'center_y':.5})
        button.bind(on_press =self.on_press_button)
        return button

    def on_press_button(self,instance):
        print('you pressed the button!')

if __name__ == '__main__':
    app=MAinApp()
    app.run()