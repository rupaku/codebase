from kivy.app import App
from kivy.uix.label import Label

'''
Every Kivy application needs to subclass App and override build(). 
size_hint(width,height) of control, between 0 to 1,default 1
pos_hint to position the widget
instantiate your MainApp class and then call run().
'''
class mainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5}
                      )
        return label


if __name__ == '__main__':
    app = mainApp()
    app.run()
