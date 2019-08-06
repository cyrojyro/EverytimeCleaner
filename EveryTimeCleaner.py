import sys
from EveryTimeGUI import *
import atexit

if __name__ == "__main__":
    atexit.register(exit_handler)
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.initializeUi()
    mainWindow.show()
    sys.exit(app.exec_())
