from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow.setStyleSheet("background-color:#0F1C25;\n")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Stack of pages
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 70, 681, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        
        # Sign Up Page
        self.page_signup = QtWidgets.QWidget()
        self.page_signup.setObjectName("page_signup")
        self.setupSignupPage()
        self.stackedWidget.addWidget(self.page_signup)
        
        # Login Page
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.setupLoginPage()
        self.stackedWidget.addWidget(self.page_login)
        
        # Initial Page
        self.stackedWidget.setCurrentWidget(self.page_signup)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Event Listeners
        self.pushButton_signup.clicked.connect(self.signup)
        self.pushButton_login_page.clicked.connect(self.login)
        self.label_goto_signup.mousePressEvent = self.gotoSignupPage  # Clickable label
        self.label_goto_login.mousePressEvent = self.gotoLoginPage    # Clickable label

        # Implementing text box event handlers
        self.lineEdit_first_name.textChanged.connect(self.onTextChanged)
        self.lineEdit_last_name.textChanged.connect(self.onTextChanged)
        self.lineEdit_Gmail.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_password.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_confirm_password.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_login_Gmail.textChanged.connect(self.onLoginChanged)
        
        # Implementing radio button event handlers
        self.radioButton_male.toggled.connect(self.onGenderSelected)
        self.radioButton_female.toggled.connect(self.onGenderSelected)

    def setupSignupPage(self):
        self.frame_signup = QtWidgets.QFrame(self.page_signup)
        self.frame_signup.setGeometry(QtCore.QRect(0, 0, 681, 521))
        self.frame_signup.setStyleSheet("border: 5px solid #0085FF;\n"
                                        "border-radius:10px;\n"
                                        "color: white;")
        self.frame_signup.setObjectName("frame_signup")
        
        self.lineEdit_first_name = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(60, 80, 261, 41))
        self.lineEdit_first_name.setStyleSheet("border:no;\n"
                                               "border-bottom: 3px solid #0085FF;\n"
                                               " font-size: 20px;")
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        
        self.lineEdit_last_name = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(360, 80, 271, 41))
        self.lineEdit_last_name.setStyleSheet("border:no;\n"
                                              "border-bottom: 3px solid #0085FF;\n"
                                              " font-size: 20px;")
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        
        self.lineEdit_Gmail = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_Gmail.setGeometry(QtCore.QRect(60, 170, 531, 41))
        self.lineEdit_Gmail.setStyleSheet("border:no;\n"
                                          "border-bottom: 3px solid #0085FF;\n"
                                          " font-size: 20px;")
        self.lineEdit_Gmail.setObjectName("lineEdit_Gmail")
        
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_password.setGeometry(QtCore.QRect(60, 260, 531, 41))
        self.lineEdit_password.setStyleSheet("border:no;\n"
                                             "border-bottom: 3px solid #0085FF;\n"
                                             " font-size: 20px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.label_warning = QtWidgets.QLabel(self.frame_signup)
        self.label_warning.setGeometry(QtCore.QRect(60, 390, 400, 20))
        self.label_warning.setStyleSheet("border:no;\n"
                                             "color:red;\n"
                                             " font-size: 15px;")
        
        
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(60, 340, 531, 41))
        self.lineEdit_confirm_password.setStyleSheet("border:no;\n"
                                                     "border-bottom: 3px solid #0085FF;\n"
                                                     " font-size: 20px;")
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        
        self.radioButton_male = QtWidgets.QRadioButton(self.frame_signup)
        self.radioButton_male.setGeometry(QtCore.QRect(190, 410, 95, 20))
        self.radioButton_male.setStyleSheet("border:no;\n"
                                            "color:#0085FF;\n"
                                            " font-size: 20px;")
        self.radioButton_male.setChecked(True)
        self.radioButton_male.setObjectName("radioButton_male")
        
        self.radioButton_female = QtWidgets.QRadioButton(self.frame_signup)
        self.radioButton_female.setGeometry(QtCore.QRect(310, 410, 95, 20))
        self.radioButton_female.setStyleSheet("border:no;\n"
                                              "color:#0085FF;\n"
                                              " font-size: 20px;")
        self.radioButton_female.setObjectName("radioButton_female")
        
        self.pushButton_signup = QtWidgets.QPushButton(self.frame_signup)
        self.pushButton_signup.setGeometry(QtCore.QRect(230, 450, 171, 51))
        self.pushButton_signup.setStyleSheet("QPushButton#pushButton_signup{\n"
                                             " font-size: 20px;\n"
                                             "background-color:#0085FF;\n"
                                             "border-radius:20px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#pushButton_signup:hover{\n"
                                             "background-color:lightblue;\n"
                                             "color:#0085FF;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#pushButton_signup:pressed{\n"
                                             "background-color:#0085FF;\n"
                                             "color:white;\n"
                                             "\n"
                                             "}")
        self.pushButton_signup.setObjectName("pushButton_signup")
        
        # "Already have an account?" Label
        self.label_goto_login = QtWidgets.QLabel(self.frame_signup)
        self.label_goto_login.setGeometry(QtCore.QRect(480, 450, 171, 51))
        self.label_goto_login.setStyleSheet("color: #0085FF;\n"
                                            "font-size: 16px;\n"
                                            "border: none;\n"
                                            "text-decoration: underline;")
        self.label_goto_login.setObjectName("label_goto_login")
    
    def setupLoginPage(self):
        self.frame_login = QtWidgets.QFrame(self.page_login)
        self.frame_login.setGeometry(QtCore.QRect(0, 0, 681, 521))
        self.frame_login.setStyleSheet("border: 5px solid #0085FF;\n"
                                       "border-radius:10px;\n"
                                       "color: white;")
        self.frame_login.setObjectName("frame_login")
        
        self.lineEdit_login_Gmail = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_login_Gmail.setGeometry(QtCore.QRect(60, 140, 531, 41))
        self.lineEdit_login_Gmail.setStyleSheet("border:no;\n"
                                                "border-bottom: 3px solid #0085FF;\n"
                                                " font-size: 20px;")
        self.lineEdit_login_Gmail.setObjectName("lineEdit_login_Gmail")
        
        self.label_login_warning = QtWidgets.QLabel(self.frame_login)
        self.label_login_warning.setGeometry(QtCore.QRect(60, 390, 400, 20))
        self.label_login_warning.setStyleSheet("border:no;\n"
                                             "color:red;\n"
                                             " font-size: 15px;")
        
        self.lineEdit_login_password = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_login_password.setGeometry(QtCore.QRect(60, 220, 531, 41))
        self.lineEdit_login_password.setStyleSheet("border:no;\n"
                                                   "border-bottom: 3px solid #0085FF;\n"
                                                   " font-size: 20px;")
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        
        self.pushButton_login_page = QtWidgets.QPushButton(self.frame_login)
        self.pushButton_login_page.setGeometry(QtCore.QRect(230, 300, 171, 51))
        self.pushButton_login_page.setStyleSheet("QPushButton#pushButton_login_page{\n"
                                                 " font-size: 20px;\n"
                                                 "background-color:#0085FF;\n"
                                                 "border-radius:20px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton#pushButton_login_page:hover{\n"
                                                 "background-color:lightblue;\n"
                                                 "color:#0085FF;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton#pushButton_login_page:pressed{\n"
                                                 "background-color:#0085FF;\n"
                                                 "color:white;\n"
                                                 "\n"
                                                 "}")
        self.pushButton_login_page.setObjectName("pushButton_login_page")
        
        # "Don't have an account?" Label
        self.label_goto_signup = QtWidgets.QLabel(self.frame_login)
        self.label_goto_signup.setGeometry(QtCore.QRect(480, 300, 171, 51))
        self.label_goto_signup.setStyleSheet("color: #0085FF;\n"
                                             "font-size: 16px;\n"
                                             "border: none;\n"
                                             "text-decoration: underline;")
        self.label_goto_signup.setObjectName("label_goto_signup")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.lineEdit_last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.lineEdit_Gmail.setPlaceholderText(_translate("MainWindow", "Gmail"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_confirm_password.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.radioButton_male.setText(_translate("MainWindow", "Male"))
        self.radioButton_female.setText(_translate("MainWindow", "Female"))
        self.pushButton_signup.setText(_translate("MainWindow", "Sign Up"))
        self.label_goto_login.setText(_translate("MainWindow", "Already have an account?"))
        
        
        self.lineEdit_login_Gmail.setPlaceholderText(_translate("MainWindow", "Gmail"))
        self.lineEdit_login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_login_page.setText(_translate("MainWindow", "Login"))
        self.label_goto_signup.setText(_translate("MainWindow", "Don't have an account?"))
    
    def signup(self):
        # Retrieve values from the sign-up form fields
        first_name = self.lineEdit_first_name.text()
        last_name = self.lineEdit_last_name.text()
        Gmail = self.lineEdit_Gmail.text()
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()
        gender = "Male" if self.radioButton_male.isChecked() else "Female"

        # Print the retrieved values
        print("Sign Up Details:")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Gmail: {Gmail}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")
        print(f"Gender: {gender}")

    def login(self):
    # Retrieve values from the login form fields
        Gmail = self.lineEdit_login_Gmail.text()
        password = self.lineEdit_login_password.text()

        # Print the retrieved values
        print("Login Details:")
        print(f"Gmail: {Gmail}")
        print(f"Password: {password}")


    def gotoSignupPage(self, event):
        self.stackedWidget.setCurrentWidget(self.page_signup)

    def gotoLoginPage(self, event):
        self.stackedWidget.setCurrentWidget(self.page_login)

    def onLoginChanged(self):
        Gmail = self.lineEdit_login_Gmail.text()
        _translate = QtCore.QCoreApplication.translate
        if(not Gmail.endswith("@gmail.com")):
            self.label_login_warning.setText(_translate("MainWindow", "⚠️Invalid Gmail ID"))
            self.pushButton_signup.setEnabled(False)

    def onPasswordChanged(self):
        # You can handle text changes here
        password = self.lineEdit_password.text()
        Gmail = self.lineEdit_Gmail.text()
        _translate = QtCore.QCoreApplication.translate
        confirm_password = self.lineEdit_confirm_password.text()
        if(password!=confirm_password and len(password)<=len(confirm_password)):
            self.label_warning.setText(_translate("MainWindow", "⚠️Password and Confirm Password Should be same"))
        elif(not Gmail.endswith("@gmail.com")):
            self.label_warning.setText(_translate("MainWindow", "⚠️Invalid Gmail ID"))
        else:
             self.label_warning.setText(_translate("MainWindow", ""))

    def onTextChanged(self):
        # You can handle text changes here
        print("Text Changed in one of the fields")

    def onGenderSelected(self):
        selected_gender = "Male" if self.radioButton_male.isChecked() else "Female"
        print(f"Selected Gender: {selected_gender}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
