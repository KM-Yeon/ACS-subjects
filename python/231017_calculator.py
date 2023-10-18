import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import QFile
from ui_231017_calculator import Ui_MainWindow


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()


    def init_ui(self):
        self.ui.btn0.clicked.connect(self.num_0)
        self.ui.btn1.clicked.connect(self.num_1)
        self.ui.btn2.clicked.connect(self.num_2)
        self.ui.btn3.clicked.connect(self.num_3)
        self.ui.btn4.clicked.connect(self.num_4)
        self.ui.btn5.clicked.connect(self.num_5)
        self.ui.btn6.clicked.connect(self.num_6)
        self.ui.btn7.clicked.connect(self.num_7)
        self.ui.btn8.clicked.connect(self.num_8)
        self.ui.btn9.clicked.connect(self.num_9)
        
        self.ui.btn_add.clicked.connect(self.btn_add)
        self.ui.btn_sub.clicked.connect(self.btn_sub)
        self.ui.btn_mul.clicked.connect(self.btn_mul)
        self.ui.btn_div.clicked.connect(self.btn_div)
        
        self.ui.btn_point.clicked.connect(self.btn_point)
        self.ui.cancel.clicked.connect(self.btn_cancel)
        self.ui.btn_ent.clicked.connect(self.btn_ent)

        self.show()
        
        
    def num_0(self):
        self.calculator("0")
        
    def num_1(self):
        self.calculator("1")
        
    def num_2(self):
        self.calculator("2")
        
    def num_3(self):
        self.calculator("3")
        
    def num_4(self):
        self.calculator("4")
        
    def num_5(self):
        self.calculator("5")
        
    def num_6(self):
        self.calculator("6")
        
    def num_7(self):
        self.calculator("7")
        
    def num_8(self):
        self.calculator("8")
        
    def num_9(self):
        self.calculator("9")

    def btn_add(self):
        sc = self.ui.btn_add.text()
        self.calculator(sc)
        
    def btn_sub(self):
        sc = self.ui.btn_sub.text()
        self.calculator(sc)
        
    def btn_mul(self):
        sc = "*"
        self.calculator(sc)
        
    def btn_div(self):
        sc = self.ui.btn_div.text()
        self.calculator(sc)
        
    def btn_ent(self):
        sc = self.ui.btn_ent.text()
        self.calculator(sc)
        
    def btn_point(self):
        sc = self.ui.btn_point.text()
        self.calculator(sc)
        
    def btn_cancel(self):
        result = self.ui.ledit.text()[:-1]
        self.ui.ledit.setText(result)
        
    def calculator(self, var):
        exist_text = self.ui.ledit.text()
        
        if var == "=":
            try:
                answer = eval(exist_text)
                self.ui.ledit.setText(str(answer))
            except ZeroDivisionError as e:
                print(e)      
            
        else:
            self.ui.ledit.setText(exist_text + var)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalculatorApp()
    ex.show()
    sys.exit(app.exec())