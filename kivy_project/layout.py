'''
BoxLayout
FloatLayout
GridLayout

padding: You can specify the padding in pixels between the layout and its children in one of three ways:
A four-argument list: [padding_left, padding_top, padding_right, padding_bottom]
A two-argument list: [padding_horizontal, padding_vertical]
A singular argument: padding=10
spacing: You can add space between the children widgets with this argument.
orientation: You can change the default orientation of the BoxLayout from horizontal to vertical.
'''

import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red=[1,0,0,1]
green=[0,1,0,1]
blue=[0,0,1,1]
purple=[1,0,1,1]

class LayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors=[red,blue,green,purple]
        for i in range(5):
            btn=Button(text="Button #%s" % (i+1),
                       background_color=random.choice(colors))
            layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    app=LayoutExample()
    app.run()