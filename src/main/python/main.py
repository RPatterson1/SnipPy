from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QPushButton



import sys

def say_hello():
 print("Button clicked, Hello!")

def main():


    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    # window = QMainWindow()
    # window.resize(250, 150)
    # window.show()

    button = QPushButton("Download")
    button.resize(250, 150)
    button.clicked.connect(say_hello)
    button.show()



    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)



if __name__ == '__main__':
    main()
