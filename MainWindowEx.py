from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
      pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonCalculate.clicked.connect(self.BMI_calculate)
        self.pushButtonClose.clicked.connect(self.thoat)
    def BMI_calculate(self):
        weight=float(self.lineEdit.text())
        height=float(self.lineEdit_2.text())
        height=height/100
        BMI=weight/(height*height)
        BMI=round(BMI,2)
        comment=""
        if BMI<16:
            comment="Severe Thinness"
        elif BMI<17:
            comment="Moderate Thinness"
        elif BMI<18.5:
            comment="Mild Thinness"
        elif BMI<25:
            comment="Normal"
        elif BMI<30:
            comment="Overweight"
        elif BMI<35:
            comment="Obese Class I"
        else:
            comment="Obese Class II"
        self.label_9.setText((str(BMI)))
        self.label_10.setText(comment)
    def show(self):
        self.MainWindow.show()
    def thoat(self):
        self.pushButtonClose.clicked.MainWindow.close()






