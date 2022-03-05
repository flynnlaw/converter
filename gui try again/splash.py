import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen, QMainWindow
from PyQt5.QtCore import QTimer

  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("key") 
#        self.setGeometry(100, 100, 350, 500) 
        self.resize(350, 500) 
        
        self.UiComponents() 
        self.show() 
  

    def UiComponents(self): 
        lockButton = QPushButton(self) 
        lockButton.setGeometry(60, 200, 100, 70) 
        lockButton.setStyleSheet("border-radius : 10; border : 1px solid white; background-color : #3A3535") 
        lockButton.setIcon(QIcon('im.png'))              # ! 'lock.png'
        size = QSize(40, 40) 
        lockButton.setIconSize(size)
        lockButton.clicked.connect(self.clickme) 
        

    def clickme(self): 
        print("pressed") 
  

App = QApplication(sys.argv) 

# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
import time
splash = QSplashScreen()
splash.setPixmap(QPixmap('images/splash_.jpg').scaled(366, 568))
splash.show()
splash.showMessage('<h1 style="color:white;">Welcome to use this PyQt5-SplashScreen</h1>', 
                   Qt.AlignTop | Qt.AlignHCenter, Qt.white)    
time.sleep(5)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
window = Window()
splash.finish(window)     # +++

sys.exit(App.exec()) 
