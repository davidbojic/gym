import kivy.utils
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class TreningWindow(Screen):
    pass


class KalkulatorWindow(Screen):
    pass


class WatchWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class GymApp(App):
    pass


GymApp().run()
