from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import sys, os
import webbrowser
import random
import string



def ressource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(ressource_path("main.ui"))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.Handel_Buttons()
       
    def Handel_Buttons(self):
        self.generate_passwords.clicked.connect(self.output)
        self.copy.clicked.connect(self.copy_output)
        self.clear.clicked.connect(self.clearr)
        self.linkedin.clicked.connect(self.linked_in)
        self.github.clicked.connect(self.git_hub)
        

    def randompassword(self):

        intValidator1 = QIntValidator(8, 96)
        intValidator2 = QIntValidator(1, 96)

        if self.chars_input.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Empty input! Please enter a number between 8 and 96!")
            msg.exec_()

        elif int(self.chars_input.text()) % 4 != 0:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Wrong input! Characters length must equals to or greater than 8"+"\n"+"and a multiplier of 4 such as 8, 12, 16 ect.")
            msg.exec_()

        elif self.chars_input.text().isnumeric() != True:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Wrong input! Input must be a digit! Please enter a number between 8 and 96.")
            msg.exec_()

        elif intValidator1.validate(self.chars_input.text(), 0)[0] != QIntValidator.Acceptable:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Wrong input! Characters length must be a number between 8 and 96!"+"\n"+"Please enter a number between 8 and 96.")
            msg.exec_()

        elif self.pwdNbr_input.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Empty input! Please enter a number between 1 and 96!")
            msg.exec_()

        elif self.pwdNbr_input.text().isnumeric() != True:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Wrong input! Input must be a digit! Please enter a number between 1 and 96!")
            msg.exec_()

        elif intValidator2.validate(self.pwdNbr_input.text(), 0)[0] != QIntValidator.Acceptable:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Wrong input! Minimum password(s) to generate is 1"+"\n"+"and the maximum is 96."+"\n"+"Please enter a number between 1 and 96!")
            msg.exec_()

        else: 

            punc = "!#($%&*+}-/<=)>?@[\]^{|"

            uchars = int(self.chars_input.text()) / 4

            lchars = int(self.chars_input.text()) / 4

            dchars = int(self.chars_input.text()) / 4

            schars = int(self.chars_input.text()) / 4

            str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''

            for _ in range(int(uchars)):
                str_uchars += random.SystemRandom().choice(string.ascii_uppercase)

            for _ in range(int(lchars)):
                str_uchars += random.SystemRandom().choice(string.ascii_lowercase)

            for _ in range(int(dchars)):
                str_uchars += random.SystemRandom().choice(string.digits)

            for _ in range(int(schars)):
                str_uchars += random.SystemRandom().choice(punc)

            random_str = str_uchars + str_lchars + str_dchars + str_schars

            random_str = ''.join(random.sample(random_str, len(random_str)))

            l = list(random_str)

            random.shuffle(l)

            result = ''.join(l)

            return str(result)

    def output(self):
        
        n=0
        if self.randompassword():
            while n < int(self.pwdNbr_input.text()):
                self.paStr = self.randompassword() + '\n'
                n=n+1
                self.passwords_output.append(self.paStr)
           
    def copy_output(self):
        QApplication.clipboard().setText(self.passwords_output.toPlainText())
        msg = QMessageBox()
        msg.setWindowIcon(QIcon('directory/padlock.ico'))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("P-GEN")
        msg.setText("Passwords has been copied!")
        msg.exec_()

    def clearr(self):
        self.passwords_output.clear()
        self.chars_input.clear()
        self.pwdNbr_input.clear()
        msg = QMessageBox()
        msg.setWindowIcon(QIcon('directory/padlock.ico'))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("P-GEN")
        msg.setText("Passwords and Inputs are cleared!")
        msg.exec_()

    def linked_in(self):
        self.url='https://linkedin.com/in/cyber-services'
        webbrowser.open_new_tab(self.url)

    def git_hub(self):
        self.url='https://github.com/IT-Support-L2'
        webbrowser.open_new_tab(self.url)

    def save_file(self): 
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            file = open(f'{fileName}', 'w')
            file.write(self.passwords_output.toPlainText())
            file.close()

            msg = QMessageBox()
            msg.setWindowIcon(QIcon('directory/padlock.ico'))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("P-GEN")
            msg.setText("Passwords has been Exported!")
            msg.exec_()           

def main():
    
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
    
if __name__=='__main__':
    main()    
