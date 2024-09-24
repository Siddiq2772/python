import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, 
                             QVBoxLayout, QHBoxLayout, QSplitter, QTextEdit, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class ChatGPTApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT-style App")
        self.setGeometry(100, 100, 1000, 600)
        self.current_theme = "light"
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # Sidebar
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar.setMinimumWidth(200)
        sidebar.setMaximumWidth(300)

        logo_label = QLabel("ChatGPT")
        logo_label.setFont(QFont("Arial", 16, QFont.Bold))
        sidebar_layout.addWidget(logo_label)

        new_chat_btn = QPushButton("+ New chat")
        sidebar_layout.addWidget(new_chat_btn)

        history_label = QLabel("Today")
        history_label.setFont(QFont("Arial", 12))
        sidebar_layout.addWidget(history_label)

        history_items = ["Modernize Tkinter Login Page", "Simple Login Page Python"]
        for item in history_items:
            btn = QPushButton(item)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch(1)

        self.theme_btn = QPushButton("Switch to Dark Theme")
        self.theme_btn.clicked.connect(self.toggle_theme)
        sidebar_layout.addWidget(self.theme_btn)

        # Chat Area
        chat_widget = QWidget()
        chat_layout = QVBoxLayout(chat_widget)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        chat_layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()
        self.message_entry = QLineEdit()
        self.add_hint(self.message_entry, "💬 Type your message here")
        input_layout.addWidget(self.message_entry)

        mic_button = QPushButton("🎤")
        input_layout.addWidget(mic_button)

        send_button = QPushButton("Send")
        input_layout.addWidget(send_button)

        chat_layout.addLayout(input_layout)

        splitter.addWidget(sidebar)
        splitter.addWidget(chat_widget)

        self.apply_theme(self.current_theme)

    def add_hint(self, entry, hint):
        entry.setPlaceholderText(hint)

    def apply_theme(self, theme):
        if theme == "dark":
            bg_color = QColor(32, 33, 35)
            fg_color = QColor(255, 255, 255)
            btn_color = QColor(64, 65, 79)
        else:
            bg_color = QColor(240, 240, 240)
            fg_color = QColor(0, 0, 0)
            btn_color = QColor(208, 208, 208)

        palette = QPalette()
        palette.setColor(QPalette.Window, bg_color)
        palette.setColor(QPalette.WindowText, fg_color)
        palette.setColor(QPalette.Base, bg_color)
        palette.setColor(QPalette.Text, fg_color)
        palette.setColor(QPalette.Button, btn_color)
        palette.setColor(QPalette.ButtonText, fg_color)
        self.setPalette(palette)

        self.chat_display.setStyleSheet(f"background-color: {bg_color.name()}; color: {fg_color.name()};")

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
            self.theme_btn.setText("Switch to Dark Theme")
        else:
            self.current_theme = "dark"
            self.theme_btn.setText("Switch to Light Theme")
        self.apply_theme(self.current_theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatGPTApp()
    window.show()
    sys.exit(app.exec_())