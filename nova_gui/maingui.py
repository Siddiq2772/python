import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
import main

BtnTextFont = '30px'

class NovaInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.mic_on = True  # Track microphone position
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NOVA')
        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        self.setGeometry(0, 0, 1600, 1600)

        # Main layout
        self.main_layout = QVBoxLayout()

        # Top section with grid layout
        top_layout = QGridLayout()
        
        # SK logo (top-left corner)
        sk_label = QLabel('SK')
        sk_label.setStyleSheet("background-color: #ff6600; color: #ffffff; font-weight: bold; padding: 5px; border-radius:20px;")
        sk_label.setFixedSize(40, 40)
        sk_label.setAlignment(Qt.AlignCenter)

        # NOVA label (centered)
        self.nova_label = QLabel('NOVA')
        self.nova_label.setStyleSheet("color: #87CEEB; font-size: 50px; font-weight: bold;")
        self.nova_label.setAlignment(Qt.AlignVCenter)
        
        # Add widgets to the grid layout
        top_layout.addWidget(sk_label, 0, 0, Qt.AlignTop | Qt.AlignLeft)  # Top-left corner
        top_layout.addWidget(self.nova_label, 0, 1, Qt.AlignTop|Qt.AlignCenter)

        
        # Stretch settings for center and left side
        top_layout.setColumnStretch(0, 1)  
        top_layout.setColumnStretch(1, 5)

        # Microphone button
        self.mic_button = QPushButton()
        self.mic_button.setIcon(QIcon('C:\\Users\\siddi\\Desktop\\coding\\python\\nova_gui\\icons\\mic.png'))
        self.mic_button.setIconSize(QSize(100, 100))  # Smaller icon size
        self.mic_button.setFixedSize(100, 100)  # Smaller button size
        self.mic_button.setStyleSheet("background-color: #0088ff; border-radius: 50px;")

        # self.mic_button.clicked.connect(self.toggleMicPosition)  # Connect to toggle method

        # Bottom buttons layout
        self.bottom_layout = QHBoxLayout()

        history_button = QPushButton('Show Chat History')
        history_button.setStyleSheet(f"background-color: #333333; font-size:{BtnTextFont}; color: #87CEEB; padding: 5px;")
        history_button.setIcon(QIcon('C:\\Users\\siddi\\Desktop\\coding\\python\\nova_gui\\icons\\menu.png'))
        history_button.setIconSize(QSize(30, 30))

        self.text_mode_button = QPushButton()
        self.text_mode_button.setStyleSheet(f"background-color: #333333; font-size:{BtnTextFont}; color: #87CEEB; padding: 5px;")
        self.text_mode_button.setIcon(QIcon('C:\\Users\\siddi\\Desktop\\coding\\python\\nova_gui\\icons\\keyboard.png'))
        self.text_mode_button.setIconSize(QSize(50, 50))

        self.float_window_button = QPushButton()
        self.float_window_button.setStyleSheet(f"background-color: #333333;font-size:{BtnTextFont}; color: #87CEEB; padding: 5px;")
        self.float_window_button.setIcon(QIcon('C:\\Users\\siddi\\Desktop\\coding\\python\\nova_gui\\icons\\popup_open.png'))
        self.float_window_button.setIconSize(QSize(50, 50))

        self.bottom_layout.addWidget(history_button)
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.mic_button)
        self.bottom_layout.addStretch()  
        self.bottom_layout.addWidget(self.text_mode_button)
        self.bottom_layout.addWidget(self.float_window_button)

        # Add all sections to the main layout
        self.main_layout.addLayout(top_layout)

        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)

    # def toggleMicPosition(self):
    #     if self.mic_on:
    #         # Move mic button to the bottom
    #         self.main_layout.removeWidget(self.mic_button)
    #         self.bottom_layout.insertWidget(2, self.mic_button)
    #     else:
    #         # Move mic button back to center
    #         self.bottom_layout.removeWidget(self.mic_button)
    #         self.main_layout.insertWidget(2, self.mic_button, alignment=Qt.AlignCenter)
    #     self.mic_on = not self.mic_on


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NovaInterface()
    ex.show()
    sys.exit(app.exec_())
