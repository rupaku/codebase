from kivy.app import App
from kivy.uix.image import Image

class mainApp(App):
    def build(self):
        img=Image(source='./demo.jpg',
                  size_hint=(1, .5),
                  pos_hint={'center_x':.5, 'center_y':.5})

        return img

if __name__ == '__main__':
    app=mainApp()
    app.run()