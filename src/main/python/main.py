import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction
from PIL import ImageGrab
import pyautogui
#QTLayouts? For more widgets/arranging...
#We'll need this simply for the buttons...

# NOTES:
## PRIORITY: We can use XCLIP and OS interaction to copy to clipboard...
## Is there a way we can do this without saving the file??
# Explains cart. coords; https://pyautogui.readthedocs.io/en/latest/mouse.html
# Better mouse events... https://doc.qt.io/qt-5/qml-qtquick-mousearea.html


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("SnipPy")

        label = QLabel("THIS IS nice!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

        #Toolbar created for tidyness. 
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Action", self)
        button_exit = QAction("Exit", self)

        button_action.setStatusTip("ig Action")
        #button_exit.setStatusTip("Exitaroo")

        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_exit.triggered.connect(self.exitBtnClick)

        toolbar.addAction(button_action)
        toolbar.addAction(button_exit)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        #Get everything out of the way...
        self.hide()

    def rectangleTopLeft(self,s):
        selection = (300, 300, 550, 550)
        im = ImageGrab.grab(selection)
        im.save("scrnsht.png")
        im.close()
        #OS.system allows for cmds - we will need this
        #Magic code... Saves the image to system clipboard
        os.system('xclip -sel clip test.jpeg')


    def exitBtnClick(self, s):
        sys.exit()

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

#Remember... Main windows can have docking, qWidgets can be seperate.
#We want docking

# Start the event loop.
app.exec_()

# from fbs_runtime.application_context.PyQt5 import ApplicationContext
# from PyQt5.QtWidgets import QMainWindow

# import sys

# if __name__ == '__main__':
#     appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
#     window = QMainWindow()
#     window.resize(250, 150)
#     window.show()
#     exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
#     sys.exit(exit_code)
