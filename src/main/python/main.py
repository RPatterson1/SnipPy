import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction

#QTLayouts? For more widgets/arranging...
#We'll need this simply for the buttons...

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

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        #Get everything out of the way...
        self.hide()

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
