# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
# pyuic5 -x untitled.ui -o test.py
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(800, 640)
        MainWindow.setMaximumSize(800, 640)
        MainWindow.setStyleSheet("background-color: #07151E;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # Stack widget to hold multiple pages
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 30, 400, 561))
        self.stackedWidget.setStyleSheet("background-color: white; border-radius: 25px; color: #0085FF; ")
        self.stackedWidget.setObjectName("stackedWidget")

        # Page 1: Sign Up
        self.page_sign_up = QtWidgets.QWidget()
        self.page_sign_up.setObjectName("page_sign_up")
        # self.page_sign_up.setStyleSheet("border: 2px solid #0085FF;")
        
        self.label = QtWidgets.QLabel(self.page_sign_up)
        self.label.setGeometry(QtCore.QRect(150, 30, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.page_sign_up)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.page_sign_up)
        self.label_3.setGeometry(QtCore.QRect(210, 80, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_3.setObjectName("label_3")
        
        self.lineEdit = QtWidgets.QLineEdit(self.page_sign_up)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 131, 41))
        self.lineEdit.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_sign_up)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 110, 131, 41))
        self.lineEdit_2.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_sign_up)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 190, 291, 41))
        self.lineEdit_3.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.label_4 = QtWidgets.QLabel(self.page_sign_up)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_sign_up)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 270, 291, 41))
        self.lineEdit_4.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_sign_up)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 350, 291, 41))
        self.lineEdit_5.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.label_5 = QtWidgets.QLabel(self.page_sign_up)
        self.label_5.setGeometry(QtCore.QRect(50, 240, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.page_sign_up)
        self.label_6.setGeometry(QtCore.QRect(50, 320, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_6.setObjectName("label_6")
        
        self.radioButton = QtWidgets.QRadioButton(self.page_sign_up)
        self.radioButton.setGeometry(QtCore.QRect(50, 430, 95, 20))
        self.radioButton.setObjectName("radioButton")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_sign_up)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 430, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.label_7 = QtWidgets.QLabel(self.page_sign_up)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_7.setObjectName("label_7")
        
        self.pushButton = QtWidgets.QPushButton(self.page_sign_up)
        self.pushButton.setGeometry(QtCore.QRect(40, 480, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{background: lightblue; border-radius: 20px;}"
                                      "QPushButton#pushButton:hover{background: skyblue;}"
                                      "QPushButton#pushButton:pressed{background: blue;}")
        self.pushButton.setObjectName("pushButton")
        
        self.label_8 = QtWidgets.QLabel(self.page_sign_up)
        self.label_8.setGeometry(QtCore.QRect(70, 530, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.page_sign_up)
        self.label_9.setGeometry(QtCore.QRect(250, 530, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: blue")
        self.label_9.setObjectName("label_9")
        
        self.stackedWidget.addWidget(self.page_sign_up)

        # Page 2: Login
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")

        self.label_login = QtWidgets.QLabel(self.page_login)
        self.label_login.setGeometry(QtCore.QRect(150, 30, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        
        self.label_email_login = QtWidgets.QLabel(self.page_login)
        self.label_email_login.setGeometry(QtCore.QRect(50, 80, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_email_login.setFont(font)
        self.label_email_login.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_email_login.setObjectName("label_email_login")
        
        self.lineEdit_email_login = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_email_login.setGeometry(QtCore.QRect(40, 110, 291, 41))
        self.lineEdit_email_login.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_email_login.setObjectName("lineEdit_email_login")
        
        self.label_password_login = QtWidgets.QLabel(self.page_login)
        self.label_password_login.setGeometry(QtCore.QRect(50, 160, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_password_login.setFont(font)
        self.label_password_login.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_password_login.setObjectName("label_password_login")
        
        self.lineEdit_password_login = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_password_login.setGeometry(QtCore.QRect(40, 190, 291, 41))
        self.lineEdit_password_login.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_login.setObjectName("lineEdit_password_login")
        
        self.label_forgot_password = QtWidgets.QLabel(self.page_login)
        self.label_forgot_password.setGeometry(QtCore.QRect(40, 240, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_forgot_password.setFont(font)
        self.label_forgot_password.setStyleSheet("color: blue")
        self.label_forgot_password.setObjectName("label_forgot_password")

        self.pushButton_login = QtWidgets.QPushButton(self.page_login)
        self.pushButton_login.setGeometry(QtCore.QRect(40, 300, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton#pushButton_login{background: lightblue; border-radius: 20px;}"
                                            "QPushButton#pushButton_login:hover{background: skyblue;}"
                                            "QPushButton#pushButton_login:pressed{background: blue;}")
        self.pushButton_login.setObjectName("pushButton_login")

        self.label_no_account = QtWidgets.QLabel(self.page_login)
        self.label_no_account.setGeometry(QtCore.QRect(40, 340, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_no_account.setFont(font)
        self.label_no_account.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_no_account.setObjectName("label_forgot_password")

        self.label_signUp = QtWidgets.QLabel("Sign Up",self.page_login)
        self.label_signUp.setGeometry(QtCore.QRect(200, 340, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_signUp.setFont(font)
        self.label_signUp.setStyleSheet("color: blue")
        self.label_signUp.setObjectName("label_forgot_password")

        
       
        
        self.stackedWidget.addWidget(self.page_login)

        # Page 3: Forgot Password
        self.page_forgot_password = QtWidgets.QWidget()
        self.page_forgot_password.setObjectName("page_forgot_password")

        self.label_forgot = QtWidgets.QLabel(self.page_forgot_password)
        self.label_forgot.setGeometry(QtCore.QRect(110, 30, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_forgot.setFont(font)
        self.label_forgot.setObjectName("label_forgot")
        
        self.label_email_forgot = QtWidgets.QLabel(self.page_forgot_password)
        self.label_email_forgot.setGeometry(QtCore.QRect(50, 80, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_email_forgot.setFont(font)
        self.label_email_forgot.setStyleSheet("color: rgb(160, 160, 160)")
        self.label_email_forgot.setObjectName("label_email_forgot")
        
        self.lineEdit_email_forgot = QtWidgets.QLineEdit(self.page_forgot_password)
        self.lineEdit_email_forgot.setGeometry(QtCore.QRect(40, 110, 291, 41))
        self.lineEdit_email_forgot.setStyleSheet("border: 1px solid rgb(155, 155, 155); border-radius: 10px;")
        self.lineEdit_email_forgot.setObjectName("lineEdit_email_forgot")
        
        self.pushButton_reset_password = QtWidgets.QPushButton(self.page_forgot_password)
        self.pushButton_reset_password.setGeometry(QtCore.QRect(40, 180, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_reset_password.setFont(font)
        self.pushButton_reset_password.setStyleSheet("QPushButton#pushButton_reset_password{background: lightblue; border-radius: 20px;}"
                                                     "QPushButton#pushButton_reset_password:hover{background: skyblue;}"
                                                     "QPushButton#pushButton_reset_password:pressed{background: blue;}")
        self.pushButton_reset_password.setObjectName("pushButton_reset_password")
        
        self.stackedWidget.addWidget(self.page_forgot_password)

        # Set the main widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Adding a status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect signals and slots
        self.label_9.mousePressEvent = self.go_to_login
        self.label_signUp.mousePressEvent = self.go_to_SignUp_from_login
        self.label_forgot_password.mousePressEvent = self.go_to_forgot_password
        self.pushButton_reset_password.clicked.connect(self.go_to_login_from_forgot)
        self.pushButton.clicked.connect(self.sign_up)

        # Add text to UI elements
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "First Name"))
        self.label_3.setText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "Email Address"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Confirm Password"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.label_7.setText(_translate("MainWindow", "What's your Gender?"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.label_8.setText(_translate("MainWindow", "Already have an account?"))
        self.label_9.setText(_translate("MainWindow", "Login"))
        
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_email_login.setText(_translate("MainWindow", "Email Address"))
        self.label_password_login.setText(_translate("MainWindow", "Password"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_forgot_password.setText(_translate("MainWindow", "Forgot Password?"))
        self.label_no_account.setText(_translate("MainWindow", "Don't Have a account?"))
        self.label_signUp.setText(_translate("MainWindow", "Sign up"))

        self.label_forgot.setText(_translate("MainWindow", "Forgot Password"))
        self.label_email_forgot.setText(_translate("MainWindow", "Enter your email address"))
        self.pushButton_reset_password.setText(_translate("MainWindow", "Reset Password"))


    def go_to_SignUp_from_login(self,event):
        """Switch back to Login page from Forgot Password page"""
        self.stackedWidget.setCurrentIndex(0)

    def go_to_login(self, event):
        """Switch to Login page"""
        self.stackedWidget.setCurrentIndex(1)

    def go_to_forgot_password(self, event):
        """Switch to Forgot Password page"""
        self.stackedWidget.setCurrentIndex(2)

    def go_to_login_from_forgot(self,event):
        """Switch back to Login page from Forgot Password page"""
        self.stackedWidget.setCurrentIndex(1)

    

    def sign_up(self):
        """Handle sign-up logic"""
        print("Sign Up Clicked")
        # Add sign-up logic here


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
