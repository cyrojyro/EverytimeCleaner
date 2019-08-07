import time
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver

chromedriver_dir = r'C:\chromedriver.exe'
loginBtnName = 'button.login'
idTextBoxName = 'userid'
pwTextBoxName = 'password'
submitBtnName = 'submit'
myArticleURL = 'myarticle'
myCommentURL = "mycommentarticle"
articleName = 'article'
deleteBtn = 'li.del'

driver = None

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):

        self.mainWindow = mainWindow

        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(492, 400)

        font = QtGui.QFont()
        font.setFamily("맑은 고딕 Semilight")
        font.setBold(True)
        font.setWeight(75)

        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.idEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idEdit.setGeometry(QtCore.QRect(150, 110, 181, 31))
        self.idEdit.setObjectName("idEdit")

        self.pwEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pwEdit.setGeometry(QtCore.QRect(150, 160, 181, 31))
        self.pwEdit.setObjectName("pwEdit")

        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(360, 100, 101, 41))
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.onClickLoginBtn)

        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(360, 160, 101, 41))
        self.helpBtn.setObjectName("helpBtn")
        self.helpBtn.clicked.connect(self.onClickHelpBtn)

        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(40, 30, 351, 51))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)

        self.mainLabel.setFont(font)
        self.mainLabel.setLineWidth(0)
        self.mainLabel.setTextFormat(QtCore.Qt.RichText)
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")

        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(20, 110, 111, 31))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)

        self.idLabel.setFont(font)
        self.idLabel.setLineWidth(0)
        self.idLabel.setTextFormat(QtCore.Qt.RichText)
        self.idLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.idLabel.setObjectName("idLabel")

        self.pwLabel = QtWidgets.QLabel(self.centralwidget)
        self.pwLabel.setGeometry(QtCore.QRect(20, 160, 111, 31))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)

        self.pwLabel.setFont(font)
        self.pwLabel.setLineWidth(0)
        self.pwLabel.setTextFormat(QtCore.Qt.RichText)
        self.pwLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pwLabel.setObjectName("pwLabel")

        self.delayEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.delayEdit.setGeometry(QtCore.QRect(380, 340, 81, 31))
        self.delayEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.delayEdit.setObjectName("delayEdit")

        self.delayLabel = QtWidgets.QLabel(self.centralwidget)
        self.delayLabel.setGeometry(QtCore.QRect(260, 340, 111, 31))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.delayLabel.setFont(font)
        self.delayLabel.setLineWidth(0)
        self.delayLabel.setTextFormat(QtCore.Qt.RichText)
        self.delayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.delayLabel.setObjectName("delayLabel")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 220, 251, 101))
        self.textBrowser.setObjectName("textBrowser")

        self.articleDelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.articleDelBtn.setGeometry(QtCore.QRect(300, 220, 161, 41))
        self.articleDelBtn.setObjectName("articleDelBtn")
        self.articleDelBtn.clicked.connect(self.onClickArticleDelBtn)

        self.commentDelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.commentDelBtn.setGeometry(QtCore.QRect(300, 280, 161, 41))
        self.commentDelBtn.setObjectName("commentDelBtn")
        self.commentDelBtn.clicked.connect(self.onClickCommentDelBtn)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def throwMessage(self, message):
        helpMsg = QtWidgets.QMessageBox()
        helpMsg.setWindowTitle('도움말')
        helpMsg.setIcon(QtWidgets.QMessageBox.Information)
        helpMsg.setText(message)
        helpMsg.show()
        helpMsg.exec_()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "에브리타임 클리너"))
        self.helpBtn.setText(_translate("mainWindow", "도움말"))
        self.loginBtn.setText(_translate("mainWindow", "로그인"))
        self.mainLabel.setText(_translate("mainWindow", "에브리타임 클리너 V0.3"))
        self.idLabel.setText(_translate("mainWindow", "아이디"))
        self.pwLabel.setText(_translate("mainWindow", "패스워드"))
        self.delayEdit.setText(_translate("mainWindow", "0.3"))
        self.delayLabel.setText(_translate("mainWindow", "삭제 딜레이"))
        self.articleDelBtn.setText(_translate("mainWindow", "글 삭제"))
        self.commentDelBtn.setText(_translate("mainWindow", "댓글 삭제"))

    def initializeUi(self):
        self.mainWindow.setWindowState(
            self.mainWindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        self.articleDelBtn.setEnabled(False)
        self.commentDelBtn.setEnabled(False)
        self.textBrowser.setText("에브리타임 아이디, 비밀번호를 입력하여 로그인해주세요.")

    def onClickHelpBtn(self):
        self.throwMessage('에브리타임 클리너 V0.3\n제작자: cyrojyro\nURL: https://github.com/cyrojyro/Everytime-Cleaner')

    def onClickLoginBtn(self):
        self.loginBtn.setEnabled(False)

        #사이트 접속
        try:
            global driver
            driver = webdriver.Chrome(chromedriver_dir)
        except:
            self.throwMessage('클리너를 사용하기 위해서는 구글 크롬과, C:\ 경로에 크롬과 버전이 일치하는 \'chromeDriver.exe 파일\'이 필요합니다.'
                            '\nhttps://chromedriver.chromium.org/downloads에서 \'chromeDriver.exe 파일\'을 다운로드 받으실 수 있습니다.')

        driver.get('https://everytime.kr/login')
        idTextBox = driver.find_element_by_name(idTextBoxName)
        idTextBox.send_keys(self.idEdit.text())
        pwTextBox = driver.find_element_by_name(pwTextBoxName)
        pwTextBox.send_keys(self.pwEdit.text())
        submit = driver.find_element_by_class_name(submitBtnName)
        submit.click()
        self.mainWindow.activateWindow()

        #로그인 결과 핸들링
        loginSuccess = True
        try:
            alert = driver.switch_to.alert
            alert.accept()
            driver.close()
            self.throwMessage('로그인에 실패하였습니다.')
            loginSuccess = False
            self.idEdit.setEnabled(True)
            self.pwEdit.setEnabled(True)
            self.loginBtn.setEnabled(True)
        except:
            pass

        if loginSuccess:
            self.textBrowser.setText("글 삭제/ 댓글 삭제 버튼을 눌러 삭제하세요. 인터넷 속도와 컴퓨터 성능에 따라 딜레이를 조절하세요.")
            self.idEdit.setEnabled(False)
            self.pwEdit.setEnabled(False)
            self.articleDelBtn.setEnabled(True)
            self.commentDelBtn.setEnabled(True)

    def onClickArticleDelBtn(self):
        self.textBrowser.setText("글 삭제중...")
        self.articleDelBtn.setEnabled(False)
        self.commentDelBtn.setEnabled(False)

        delay = float(self.delayEdit.text())
        while True:
            driver.get('https://everytime.kr/' + myArticleURL)
            time.sleep(delay)
            article = driver.find_element_by_class_name(articleName)
            article.click()
            time.sleep(delay)

            #앞부터 삭제
            lis = driver.find_elements_by_css_selector(deleteBtn)
            if len(lis):
                driver.execute_script("arguments[0].click();", lis[0])

            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                self.mainWindow.activateWindow()
                self.textBrowser.setText("글 삭제 완료.\n삭제가 제대로 되지 않으면, 딜레이를 늘려 주세요.")
                break

        self.mainWindow.activateWindow()
        self.articleDelBtn.setEnabled(True)
        self.commentDelBtn.setEnabled(True)

    def onClickCommentDelBtn(self):
        self.textBrowser.setText("댓글 삭제중...")
        self.articleDelBtn.setEnabled(False)
        self.commentDelBtn.setEnabled(False)

        delay = float(self.delayEdit.text())
        while True:
            driver.get('https://everytime.kr/' + myCommentURL)
            time.sleep(delay)
            article = driver.find_element_by_class_name(articleName)
            article.click()
            time.sleep(delay)

            #뒤부터 삭제
            lis = driver.find_elements_by_css_selector(deleteBtn)
            if len(lis):
                driver.execute_script("arguments[0].click();", lis[-1])

            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                self.mainWindow.activateWindow()
                self.textBrowser.setText("댓글 삭제 완료.\n삭제가 제대로 되지 않으면, 딜레이를 늘려 주세요.")
                break

        self.mainWindow.activateWindow()
        self.articleDelBtn.setEnabled(True)
        self.commentDelBtn.setEnabled(True)


def exit_handler():
    if driver != None:
        driver.close()
