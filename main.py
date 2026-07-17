import sys
from PyQt5.QtWidgets import QApplication,QMainWindow ,QLabel,QPushButton,QGridLayout,QWidget,QLineEdit
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,600)
        bg=QLabel(self)
        pixmap=QPixmap("templates/mushroomcalc.png")
        bg.setPixmap(pixmap)
        bg.setScaledContents(True)
        bg.setGeometry(0,0,500,600)
        
       
        self.initUI()
    def initUI(self):
        centralwidget= QWidget()
        self.setCentralWidget(centralwidget)
        
        button1=QPushButton(centralwidget)
        button1.setIcon(QIcon("templates/1button.png"))
        button1.setIconSize(QSize(70,69))
        button2=QPushButton(centralwidget)
        button2.setIcon(QIcon("templates/2button.png"))
        button2.setIconSize(QSize(70,69))
        button3=QPushButton(centralwidget)
        button3.setIcon(QIcon("templates/3button.png"))
        button3.setIconSize(QSize(40,39))
        button4=QPushButton(centralwidget)
        button4.setIcon(QIcon("templates/4button.png"))
        button4.setIconSize(QSize(70,69))
        button5=QPushButton(centralwidget)
        button5.setIcon(QIcon("templates/5button.png"))
        button5.setIconSize(QSize(70,69))
        button6=QPushButton(centralwidget)
        button6.setIcon(QIcon("templates/6button.png"))
        button6.setIconSize(QSize(70,69))
        button7=QPushButton(centralwidget)
        button7.setIcon(QIcon("templates/7button.png"))
        button7.setIconSize(QSize(70,69))
        button8=QPushButton(centralwidget)
        button8.setIcon(QIcon("templates/8button.png"))
        button8.setIconSize(QSize(70,69))
        button9=QPushButton(centralwidget)
        button9.setIcon(QIcon("templates/9button.png"))
        button9.setIconSize(QSize(70,69))
        button0=QPushButton(centralwidget)
        button0.setIcon(QIcon("templates/0button.png"))
        button0.setIconSize(QSize(70,69))
        buttonadd=QPushButton(centralwidget)
        buttonadd.setIcon(QIcon("templates/+button.png"))
        buttonadd.setIconSize(QSize(70,69))
        buttonminus=QPushButton(centralwidget)
        buttonminus.setIcon(QIcon("templates/-button.png"))
        buttonminus.setIconSize(QSize(70,69))
        buttonmul=QPushButton(centralwidget)
        buttonmul.setIcon(QIcon("templates/Xbutton.png"))
        buttonmul.setIconSize(QSize(70,69))
        buttondiv=QPushButton(centralwidget)
        buttondiv.setIcon(QIcon("templates/divisionbutton.png"))
        buttondiv.setIconSize(QSize(70,69))
        buttonc=QPushButton(centralwidget)
        buttonc.setIcon(QIcon("templates/clearbutton.png"))
        buttonc.setIconSize(QSize(70,69))
        buttone=QPushButton(centralwidget)
        buttone.setIcon(QIcon("templates/=button.png"))
        buttone.setIconSize(QSize(70,69))
        buttons=[button0,button1,button2,button3,button4,button5,button6,button7,button8,button9,buttonadd,buttonminus,buttondiv,buttonmul,buttonc,buttone]
        for btn in buttons:
            btn.setFixedSize(70,69)
        buttonwidget=QWidget(centralwidget)
        buttonwidget.setGeometry(75,290,284,280)
        grid=QGridLayout(buttonwidget)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        grid.setContentsMargins(0,0,0,0)

        grid.addWidget(button9,0,0)
        grid.addWidget(button8,0,1)
        grid.addWidget(button7,0,2)
        grid.addWidget(buttonadd,0,3)
        grid.addWidget(button6,1,0)
        grid.addWidget(button5,1,1)
        grid.addWidget(button4,1,2)
        grid.addWidget(buttonminus,1,3)
        grid.addWidget(button3,2,0)
        grid.addWidget(button2,2,1)
        grid.addWidget(button1,2,2)
        grid.addWidget(buttonmul,2,3)
        grid.addWidget(button0,3,0)
        grid.addWidget(buttonc,3,1)
        grid.addWidget(buttone,3,2)
        grid.addWidget(buttondiv,3,3)
        
        
        self.setStyleSheet("""QPushButton{
                           border:none;
                           padding:0px;
                           margin:0px
                           }
                           """)

def main():
    app=QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())  

if __name__=="__main__":
    main()


