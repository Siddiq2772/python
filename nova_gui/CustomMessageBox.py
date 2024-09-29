from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore

class CustomMessageBox(QDialog):
    def __init__(self, text="",x=200,y=200,B1="ok",B2="cancel", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Message Box")
        
        # Layouts
        self.layout = QVBoxLayout()
        self.buttom_layout = QHBoxLayout()

        # Label
        self.label = QLabel(text)
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to center
        
        # Set the dialog's style
        self.setStyleSheet(
            "background-color:#0F1C25;\n"
            "color:white;\n"
            "padding:5px;\n"
            "border:2px solid #0085FF;\n"
            "font-size: 20px;"
        )
        
        # Set size and geometry of the dialog
        self.setGeometry(QtCore.QRect(500, 300, x, y))
        
        # Add the label to the layout
        self.layout.addWidget(self.label)
        
        # Buttons
        b1 = QPushButton(B1)
        b2 = QPushButton(B2)
        
        # Set button styles
        button_style = """
            QPushButton {
                font-size: 20px;
                background-color:#0F1C25;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: lightblue;
                color:#0F1C25;
            }
            QPushButton:pressed {
                background-color: #0F1C25;
                color: white;
            }
        """
        b1.setStyleSheet(button_style)
        b2.setStyleSheet(button_style)
        
        # Add buttons to the button layout
        self.buttom_layout.addWidget(b1)
        self.buttom_layout.addWidget(b2)
        
        # Connect button actions (optional)
        b1.clicked.connect(self.accept)  # Close the dialog on OK
        b2.clicked.connect(self.reject)  # Close the dialog on Cancel
        
        # Add the button layout to the main layout
        self.layout.addLayout(self.buttom_layout)
        
        # Set the final layout
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        # Main window button
        button = QPushButton("Show Custom Message Box")
        button.clicked.connect(self.show_custom_message_box)
        self.setCentralWidget(button)
#  controuctor impelment karne ke leye
    def show_custom_message_box(self):
        custom_msg_box = CustomMessageBox('''
        Welcome To NOVA

    NOVA is an Al which can control your
    Desktop on the basis of your command
            ''',
            600,600,"ok","cancel",self)
        custom_msg_box.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
