import kivy
kivy.require('2.3.0')
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

# Импортируем наши модули
from database import Database
from screens import LoginScreen, MainScreen, AddAdScreen, ProfileScreen

# Устанавливаем размер окна
Window.size = (400, 700)

class TradeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = None
        self.username = None
        self.db = Database()  # Создаем единственный экземпляр БД
    
    def build(self):
        self.title = "Trade App - Обмен вещами"
        
        # Создаем менеджер экранов
        sm = ScreenManager()
        
        # Создаем экраны, передавая им БД и ссылку на приложение
        sm.add_widget(LoginScreen(
            name='login', 
            db=self.db, 
            app_instance=self
        ))
        sm.add_widget(MainScreen(
            name='main', 
            db=self.db, 
            app_instance=self
        ))
        sm.add_widget(AddAdScreen(
            name='add_ad', 
            db=self.db, 
            app_instance=self
        ))
        sm.add_widget(ProfileScreen(
            name='profile', 
            db=self.db, 
            app_instance=self
        ))
        
        return sm
    
    def on_stop(self):
        """Закрываем БД при выходе из приложения"""
        self.db.close()

def main():
    print("=" * 50)
    print("TRADE APP - Приложение для обмена вещами")
    print("=" * 50)
    print("\nИнструкция:")
    print("1. Нажмите 'РЕГИСТРАЦИЯ ПО QR-КОДУ' для создания аккаунта")
    print("2. Или используйте 'ТЕСТОВЫЙ ПОЛЬЗОВАТЕЛЬ' для быстрого старта")
    print("3. В главном меню можно просматривать объявления")
    print("4. Нажмите '+' для добавления своего объявления")
    print("5. В профиле видны ваши объявления и информация\n")
    
    # Создаем папку для данных если нет
    if not os.path.exists('user_data'):
        os.makedirs('user_data')
    
    # Запускаем приложение
    TradeApp().run()

if __name__ == '__main__':
    main()
