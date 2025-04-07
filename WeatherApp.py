import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()
        self.city_label = QLabel('Enter City Name:')
        layout.addWidget(self.city_label)
        self.city_input = QLineEdit()
        layout.addWidget(self.city_input)
        self.get_weather_button = QPushButton('Get Weather')
        self.get_weather_button.clicked.connect(self.fetch_weather)
        layout.addWidget(self.get_weather_button)
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    def fetch_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, 'Input Error', 'Please enter a city name.')
            return
        api_key = '7179776f06f52298cb5d5cf3d62e65e7'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get('cod') != 200:
                QMessageBox.warning(self, 'Error', data.get('message', 'Unknown error'))
                return
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            self.result_label.setText(f'Temperature: {temp}°C\nCondition: {weather.capitalize()}')
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Error', f'Failed to fetch weather data: {e}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
