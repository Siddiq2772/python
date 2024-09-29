import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QTextEdit, QGridLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


BtnTextFont = '30px'

# Chat Bubble Item Class
class ChatBubbleItem(QListWidgetItem):
    def __init__(self, text, is_sent):
        super().__init__()
        self.is_sent = is_sent
        self.setText(text)

# Chat Window Class
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Chat display area
        self.chat_list = QListWidget()
        self.chat_list.setSpacing(10)
        self.chat_list.setWordWrap(True)
        layout.addWidget(self.chat_list)

        # Input area
        input_layout = QHBoxLayout()
        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(50)
        input_layout.addWidget(self.message_input)

        send_button = QPushButton("Send",)
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

        # Styling for chat
        self.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                color: white;
                font-size:20px;           
                border: none;
            }
            QTextEdit {
                background-color: #333333;
                color: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                font-size:20px;           
                padding: 5px;
            }
            QPushButton {
                background-color: #25D366;
                color: white;
                border: none;
                border-radius: 10px;
                font-size:20px;           
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #128C7E;
            }
        """)

    def send_message(self):
        message = self.message_input.toPlainText().strip()
        if message:
            self.add_message(message, True)
            self.message_input.clear()
            # Simulate a received message
            self.add_message("This is a received message", False)

    def add_message(self, message, is_sent):
        item = ChatBubbleItem(message, is_sent)
        self.chat_list.addItem(item)
        bubble_widget = self.create_bubble_widget(message, is_sent)
        item.setSizeHint(bubble_widget.sizeHint())
        self.chat_list.setItemWidget(item, bubble_widget)
        self.chat_list.scrollToBottom()

    def create_bubble_widget(self, message, is_sent):
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Chat bubble text
        bubble = QLabel(message)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(int(self.chat_list.width() * 0.7))
        bubble.setStyleSheet(f"""
            background-color: {'#00a884' if is_sent else '#333333'};
            color: white;
            font-size:20px;  
            border-radius: 10px;
            padding: 10px;
        """)

        # Align based on sender/receiver
        if is_sent:
            layout.addStretch()  # Align sent messages to the right
        layout.addWidget(bubble)
        if not is_sent:
            layout.addStretch()  # Align received messages to the left

        layout.setContentsMargins(10, 5, 10, 5)
        widget.setLayout(layout)
        return widget

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Update width of chat bubbles on window resize
        for i in range(self.chat_list.count()):
            item = self.chat_list.item(i)
            widget = self.chat_list.itemWidget(item)
            if widget:
                bubble = widget.findChild(QLabel)
                if bubble:
                    bubble.setMaximumWidth(int(self.chat_list.width() * 0.7))
                    item.setSizeHint(widget.sizeHint())
        self.chat_list.scrollToBottom()


# NovaInterface with chat integration
class NovaInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NOVA')
        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        self.setGeometry(0, 0, 800, 1000)

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
        # Add widgets to the grid layout
        top_layout.addWidget(sk_label, 0, 0, Qt.AlignTop | Qt.AlignLeft)  # Top-left corner
        top_layout.addWidget(self.nova_label, 0, 1, Qt.AlignTop | Qt.AlignCenter)

         # Stretch settings for center and left side
        top_layout.setColumnStretch(0, 1)  
        top_layout.setColumnStretch(1, 5)

        # Microphone button
        self.mic_button = QPushButton()
        self.mic_button.setIcon(QIcon('C:\\Users\\siddi\\Desktop\\coding\\python\\nova_gui\\icons\\mic.png'))
        self.mic_button.setIconSize(QSize(100, 100))  # Smaller icon size
        self.mic_button.setFixedSize(100, 100)  # Smaller button size
        self.mic_button.setStyleSheet("background-color: #0088ff; border-radius: 50px;")

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

        # Add the chat window in the middle
        self.chat_window = ChatWindow()
        self.main_layout.addWidget(self.chat_window)

        self.main_layout.addLayout(self.bottom_layout)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NovaInterface()
    ex.show()
    sys.exit(app.exec_())
