import kivy
kivy.require('2.3.0')

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.color = get_color_from_hex('#FFFFFF')
        
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#4CAF50'))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class AdCard(BoxLayout):
    title = StringProperty("")
    desc = StringProperty("")
    category = StringProperty("")
    type_ = StringProperty("")
    price = StringProperty("")
    location = StringProperty("")
    author = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(150)
        self.padding = dp(10)
        self.spacing = dp(5)
        
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#FFFFFF'))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
            Color(rgba=get_color_from_hex('#E0E0E0'))
            self.border = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        title_layout = BoxLayout(size_hint_y=None, height=dp(30))
        title_label = Label(
            text=self.title,
            font_size=dp(16),
            bold=True,
            color=get_color_from_hex('#000000'),
            halign='left',
            size_hint_x=0.7
        )
        title_label.bind(size=title_label.setter('text_size'))
        
        category_label = Label(
            text=self.category,
            font_size=dp(12),
            color=get_color_from_hex('#666666'),
            halign='right'
        )
        category_label.bind(size=category_label.setter('text_size'))
        
        title_layout.add_widget(title_label)
        title_layout.add_widget(category_label)
        self.add_widget(title_layout)
        
        desc_label = Label(
            text=self.desc,
            font_size=dp(14),
            color=get_color_from_hex('#333333'),
            halign='left',
            valign='top',
            size_hint_y=None,
            height=dp(60)
        )
        desc_label.bind(size=desc_label.setter('text_size'))
        self.add_widget(desc_label)
        
        info_layout = BoxLayout(size_hint_y=None, height=dp(30))
        
        if self.type_ == 'free':
            type_text = "БЕСПЛАТНО"
        else:
            type_text = f"ОБМЕН: {self.price}"
            
        type_label = Label(
            text=type_text,
            font_size=dp(14),
            bold=True,
            color=get_color_from_hex('#4CAF50')
        )
        
        loc_label = Label(
            text=self.location,
            font_size=dp(12),
            color=get_color_from_hex('#666666')
        )
        
        info_layout.add_widget(type_label)
        info_layout.add_widget(loc_label)
        self.add_widget(info_layout)
        
        author_label = Label(
            text=f"Автор: {self.author}",
            font_size=dp(12),
            color=get_color_from_hex('#999999')
        )
        self.add_widget(author_label)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.pos = [self.pos[0]-1, self.pos[1]-1]
        self.border.size = [self.size[0]+2, self.size[1]+2]
        
