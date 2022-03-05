import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QComboBox
from convert import BinaryToBinary, BinaryToHex, BinaryToDenary, DenaryToDenary, DenaryToBinary, DenaryToHex, HexToHex, HexToDenary, HexToBinary, BinaryAddition
from abc import ABC,  abstractmethod
#above imports modules needed for the code to run without converting .ui to .py and subroutines from convert.py (cli interface)
#below classes are used for the dictionary and where the code runs afterwards 
class Converter(ABC):
    
    
    @abstractmethod
    def convert(self, input):
        pass
    
class BinaryHex(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = BinaryToHex(str(input)) #calls the binarytohex function in convert.py and returns value
        return returnvalue

class BinaryDenary(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = BinaryToDenary(str(input))
        return returnvalue
    
class DenaryBinary(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = DenaryToBinary(str(input))
        return returnvalue
    
class DenaryHex(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = DenaryToHex(str(input))
        return returnvalue
    
class HexBinary(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = HexToBinary(str(input))
        return returnvalue
    
class HexDenary(Converter):
    
    def __init__ (self):
        pass
    
    def convert(self, input):
        returnvalue = HexToDenary(str(input))
        return returnvalue
    
class MainWindow(QMainWindow): #class for the main converter window
    
    
    def __init__ (self):
        super (MainWindow, self).__init__()
        loadUi("gui3.ui",self)
        self.binaryadditionbutton.clicked.connect(self.gotoScreen2) #code executes gotoScreen2() when binaryadditionbutton is pressed
        self.Submitbutton.clicked.connect(self.pressed) #code executes pressed() when submitbutton is clicked
        
  
    def gotoScreen2(self):
        widget.setCurrentIndex(widget.currentIndex()+1) #changes index by 1 to change page
        
    
    def pressed(self): #different choices for the code depending on what is selected in the comboboxes choice1 and choice2
        
        input = int(self.choice1.currentIndex())
        output = int(self.choice2.currentIndex())
        if input == output: 
            self.outputbox.setText("Select where to convert from and where to convert to")
        elif int(self.choice1.currentIndex()) == 0 and int(self.choice2.currentIndex()) != 0:
            self.outputbox.setText("Select where to convert from")
        elif int(self.choice1.currentIndex()) != 0 and int(self.choice2.currentIndex()) == 0:
            self.outputbox.setText("Select where to convert to")
        elif int(self.choice1.currentIndex()) == 0 and int(self.choice2.currentIndex()) == 0:
            self.outputbox.setText("Select where to convert from and where to convert to")
        else: 
            key = str(input) + str(output)

            #go into dict to see if you have a converter based upon input and output
            convertdict = {}
            convertdict["12"] = BinaryDenary()
            convertdict["13"] = BinaryHex()
            convertdict["21"] = DenaryBinary()
            convertdict["23"] = DenaryHex()
            convertdict["31"] = HexBinary()
            convertdict["32"] = HexDenary()

            
            converter = convertdict[key]
            output1 = converter.convert(self.userentry.toPlainText())
            self.outputbox.setText(str(output1))
            
class Screen2(QDialog): #code for binary addition screen
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("gui32.ui",self)
        self.backbutton.clicked.connect(self.gotoScreen1) #code executes go to screen1() when backbutton is clicked
        self.addbutton.clicked.connect(self.pressed) #code executes pressed() when addbutton is clicked
    
    def gotoScreen1(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def pressed(self): #named the same for simpilicity
        result, overflow = BinaryAddition(self.input1.toPlainText(), self.input2.toPlainText())
        if result == 1: 
            self.outputboxadd.append("Invalid input, try again") #numbers relate to the first value returned by BinaryAddition()
        elif result == 2: 
            self.outputboxadd.append("8 bits are required")
        elif result == 3:
            self.outputboxadd.append("Invalid input, try again")
        elif result == 4: 
             self.outputboxadd.append("8 bits are required")
        else:
            self.outputboxadd.setText(str(result))
            self.outputboxadd.append(str(int(result, 2)))
        if overflow == 1:
            self.outputboxadd.append("there was an overflow") #numbers relate to the second balue returned by BinaryAddition()
        else:
            self.outputboxadd.append("")
        

    


# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
screen2=Screen2()
widget.resize(600,300) #sets starting size of the windows 
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.show()
#makes sure window is shown







try:
    sys.exit(app.exec_()) #pretty sure this runs all the time
except:
    print ("Exiting") #prints exiting when the program stops executing
    
