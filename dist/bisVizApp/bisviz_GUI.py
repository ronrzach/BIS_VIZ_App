from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from bisviz_interface import bisviz

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        layout = BoxLayout(orientation='vertical', padding=20)
        logo = Image(source='logo.png', size_hint=(1, 0.5))
        layout.add_widget(logo)

        sDate_box = BoxLayout(orientation='horizontal')
        sDate_label = MDLabel(text='Enter Start Date : ')
        sDate_box.add_widget(sDate_label)
        self.sDate_input = MDTextField()
        sDate_box.add_widget(self.sDate_input)
        layout.add_widget(sDate_box)

        sTime_box = BoxLayout(orientation='horizontal')
        sTime_label = MDLabel(text='Enter Start Time : ')
        sTime_box.add_widget(sTime_label)
        self.sTime_input = MDTextField()
        sTime_box.add_widget(self.sTime_input)
        layout.add_widget(sTime_box)

        eDate_box = BoxLayout(orientation='horizontal')
        eDate_label = MDLabel(text='Enter End Date : ')
        eDate_box.add_widget(eDate_label)
        self.eDate_input = MDTextField()
        eDate_box.add_widget(self.eDate_input)
        layout.add_widget(eDate_box)

        eTime_box = BoxLayout(orientation='horizontal')
        eTime_label = MDLabel(text='Enter End Time : ')
        eTime_box.add_widget(eTime_label)
        self.eTime_input = MDTextField()
        eTime_box.add_widget(self.eTime_input)
        layout.add_widget(eTime_box)

        bis_thresh_box = BoxLayout(orientation='horizontal')
        bis_thresh_label = MDLabel(text='Enter BIS Threshold Value : ')
        bis_thresh_box.add_widget(bis_thresh_label)
        self.bis_thresh_input = MDTextField()
        bis_thresh_box.add_widget(self.bis_thresh_input)
        layout.add_widget(bis_thresh_box)

        time_thresh_box = BoxLayout(orientation='horizontal')
        time_thresh_label = MDLabel(text='Enter Time Threshold Value : ')
        time_thresh_box.add_widget(time_thresh_label)
        self.time_thresh_input = MDTextField()
        time_thresh_box.add_widget(self.time_thresh_input)
        layout.add_widget(time_thresh_box)

        csv_spa_box = BoxLayout(orientation='horizontal')
        csv_spa_label = MDLabel(text='CSV or SPA : ')
        csv_spa_box.add_widget(csv_spa_label)
        self.csv_spa_input = MDTextField()
        csv_spa_box.add_widget(self.csv_spa_input)
        layout.add_widget(csv_spa_box)

        button = Button(text='Choose File')
        button.bind(on_press=self.choose_file)
        layout.add_widget(button)
        self.file_manager = MDFileManager()
        self.file_manager.exit_manager = self.exit_manager
        self.file_manager.select_path = self.select_path
        return layout

    def choose_file(self, instance):
        self.file_manager.show('/')

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.file_path = path
        bisviz(self.sDate_input.text, self.sTime_input.text, self.eDate_input.text, self.eTime_input.text, self.bis_thresh_input.text, self.time_thresh_input.text, self.file_path, self.csv_spa_input.text)
        self.exit_manager()

MyApp().run()