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
deleteBtnText = '삭제'

driver = None

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):

        self.mainWindow = mainWindow

        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(492, 402)

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

        self.schoolText = QtWidgets.QLineEdit(self.centralwidget)
        self.schoolText.setGeometry(QtCore.QRect(150, 210, 121, 31))
        self.schoolText.setObjectName("schoolText")

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
        self.textBrowser.setGeometry(QtCore.QRect(30, 270, 221, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.articleDelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.articleDelBtn.setGeometry(QtCore.QRect(290, 220, 161, 41))
        self.articleDelBtn.setObjectName("articleDelBtn")
        self.articleDelBtn.clicked.connect(self.onClickArticleDelBtn)

        self.commentDelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.commentDelBtn.setGeometry(QtCore.QRect(290, 280, 161, 41))
        self.commentDelBtn.setObjectName("commentDelBtn")
        self.commentDelBtn.clicked.connect(self.onClickCommentDelBtn)

        self.schoolLabel = QtWidgets.QLabel(self.centralwidget)
        self.schoolLabel.setGeometry(QtCore.QRect(20, 210, 111, 31))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)

        self.schoolLabel.setFont(font)
        self.schoolLabel.setLineWidth(0)
        self.schoolLabel.setTextFormat(QtCore.Qt.RichText)
        self.schoolLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.schoolLabel.setObjectName("schoolLabel")

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
        self.mainLabel.setText(_translate("mainWindow", "에브리타임 클리너 V0.2"))
        self.idLabel.setText(_translate("mainWindow", "아이디"))
        self.pwLabel.setText(_translate("mainWindow", "패스워드"))
        self.delayEdit.setText(_translate("mainWindow", "0.5"))
        self.delayLabel.setText(_translate("mainWindow", "삭제 딜레이"))
        self.articleDelBtn.setText(_translate("mainWindow", "글 삭제"))
        self.commentDelBtn.setText(_translate("mainWindow", "댓글 삭제"))
        self.schoolLabel.setText(_translate("mainWindow", "학교코드"))

    def initializeUi(self):
        self.mainWindow.setWindowState(
            self.mainWindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        self.articleDelBtn.setEnabled(False)
        self.commentDelBtn.setEnabled(False)
        self.textBrowser.setText("학교 코드 (xxx.everytime.kr에서 xxx), 아이디, 비밀번호를 입력하여 로그인 해주세요.")

    def onClickHelpBtn(self):
        self.throwMessage('에브리타임 클리너 V0.2\n제작자: cyrojyro')

    def onClickLoginBtn(self):
        self.loginBtn.setEnabled(False)

        #사이트 접속
        try:
            global driver
            driver = webdriver.Chrome(chromedriver_dir)
        except:
            self.throwMessage('클리너를 사용하기 위해서는 구글 크롬과, C:\ 경로에 크롬과 버전이 일치하는 \'chromeDriver.exe 파일\'이 필요합니다.'
                            '\nhttps://chromedriver.chromium.org/downloads에서 \'chromeDriver.exe 파일\'을 다운로드 받으실 수 있습니다.')

        school = self.schoolText.text()
        try:
            driver.get('https://' + school + '.everytime.kr/login')
        except:
            pass

        # 로그인
        id = driver.find_element_by_name(idTextBoxName)
        id.clear()
        id.send_keys(self.idEdit.text())
        pw = driver.find_element_by_name(pwTextBoxName)
        pw.send_keys(self.pwEdit.text())
        submit = driver.find_element_by_class_name(submitBtnName)
        submit.click()
        self.mainWindow.activateWindow()
        self.textBrowser.setText("글 삭제/ 댓글 삭제 버튼을 눌러 삭제하세요. 인터넷 속도와 컴퓨터 성능에 따라 딜레이를 조절하세요.")
        self.idEdit.setEnabled(False)
        self.pwEdit.setEnabled(False)
        self.schoolText.setEnabled(False)
        self.articleDelBtn.setEnabled(True)
        self.commentDelBtn.setEnabled(True)

        try:
            alert = driver.switch_to.alert
            alert.accept()
            driver.close()
            self.throwMessage('로그인에 실패하였습니다.')
            self.loginBtn.setEnabled(True)
        except:
            pass

    def onClickArticleDelBtn(self):
        self.textBrowser.setText("글 삭제중...")
        self.articleDelBtn.setEnabled(False)
        self.commentDelBtn.setEnabled(False)

        delay = float(self.delayEdit.text())
        while True:
            school = self.schoolText.text()
            driver.get('https://' + school + '.everytime.kr/' + myArticleURL)
            time.sleep(delay)
            article = driver.find_element_by_class_name(articleName)
            article.click()
            time.sleep(delay)
            article = driver.find_element_by_class_name(articleName)
            status = article.find_element_by_tag_name('ul')
            li_list = status.find_elements_by_tag_name('li')
            for li in li_list:
                if li.text == deleteBtnText:
                    driver.execute_script("arguments[0].click();", li)
                    break

            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                self.mainWindow.activateWindow()
                self.textBrowser.setText("글 삭제 완료.")
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
            school = self.schoolText.text()
            driver.get('https://' + school + '.everytime.kr/' + myCommentURL)
            time.sleep(delay)
            article = driver.find_element_by_class_name(articleName)
            article.click()
            time.sleep(delay)
            comments = driver.find_elements_by_class_name(articleName)
            flag = False

            # 삭제 가능한 댓글 탐색
            for comment in comments:
                if flag:
                    break
                li_list = comment.find_elements_by_tag_name('li')
                for li in li_list:
                    if li.text == deleteBtnText:
                        driver.execute_script("arguments[0].click();", li)
                        flag = True
                        break

            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                self.mainWindow.activateWindow()
                self.textBrowser.setText("댓글 삭제 완료.")
                break

        self.mainWindow.activateWindow()
        self.articleDelBtn.setEnabled(True)
        self.commentDelBtn.setEnabled(True)


def exit_handler():
    if driver != None:
        driver.close()
