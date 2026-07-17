import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QGraphicsOpacityEffect,QLabel,QPushButton,QLabel,QLineEdit
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt,QSize
import os
def resourcepath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


class mushcalc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mushroom calculator")
        self.setGeometry(0,0,500,600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        bg=QLabel(self)
        pixmap=QPixmap(resourcepath("templates/mushroomcalc.png"))
        bg.setPixmap(pixmap)
        bg.setScaledContents(True)
        bg.setGeometry(0,0,500,600)
    
        self.initUI()
        
     
        
        
    def initUI(self):
        
        
        
        self.display=QLineEdit(self)
        
        self.display.setGeometry(140,170,200,50)
        


        self.button1 =QPushButton(self)
        self.button1.setIcon(QIcon(resourcepath("templates/1button.png")))
        self.button1.setIconSize(QSize(80,79))
        self.button1.setGeometry(230,450,80,80)
        self.button1.setProperty("value","1")
        self.button1.clicked.connect(self.button_clicked)

        self.button2=QPushButton(self)
        self.button2.setIcon(QIcon(resourcepath("templates/2button.png")))
        self.button2.setIconSize(QSize(80,79))
        self.button2.setGeometry(165,450,80,80)
        self.button2.setProperty("value","2")
        self.button2.clicked.connect(self.button_clicked)

        self.button3=QPushButton(self)
        self.button3.setIcon(QIcon(resourcepath("templates/3button.png")))
        self.button3.setIconSize(QSize(80,79))
        self.button3.setGeometry(100,450,80,80)
        self.button3.setProperty("value","3")
        self.button3.clicked.connect(self.button_clicked)

        self.button4=QPushButton(self)
        self.button4.setIcon(QIcon(resourcepath("templates/4button.png")))
        self.button4.setIconSize(QSize(80,79))
        self.button4.setGeometry(230,395,80,80)
        self.button4.setProperty("value","4")
        self.button4.clicked.connect(self.button_clicked)

        self.button5=QPushButton(self)
        self.button5.setIcon(QIcon(resourcepath("templates/5button.png")))
        self.button5.setIconSize(QSize(80,79))
        self.button5.setGeometry(165,395,80,80)
        self.button5.setProperty("value","5")
        self.button5.clicked.connect(self.button_clicked)

        self.button6=QPushButton(self)
        self.button6.setIcon(QIcon(resourcepath("templates/6button.png")))
        self.button6.setIconSize(QSize(80,79))
        self.button6.setGeometry(100,395,80,80)
        self.button6.setProperty("value","6")
        self.button6.clicked.connect(self.button_clicked)

        self.button7=QPushButton(self)
        self.button7.setIcon(QIcon(resourcepath("templates/7button.png")))
        self.button7.setIconSize(QSize(80,79))
        self.button7.setGeometry(230,340,80,80)
        self.button7.setProperty("value","7")
        self.button7.clicked.connect(self.button_clicked)


        self.button8=QPushButton(self)
        self.button8.setIcon(QIcon(resourcepath("templates/8button.png")))
        self.button8.setIconSize(QSize(80,79))
        self.button8.setGeometry(165,340,80,80)
        self.button8.setProperty("value","8")
        self.button8.clicked.connect(self.button_clicked)
 


        self.button9=QPushButton(self)
        self.button9.setIcon(QIcon(resourcepath("templates/9button.png")))
        self.button9.setIconSize(QSize(80,79))
        self.button9.setGeometry(100,340,80,80)
        self.button9.setProperty("value","9")
        self.button9.clicked.connect(self.button_clicked)

        self.button0=QPushButton(self)
        self.button0.setIcon(QIcon(resourcepath("templates/0button.png")))
        self.button0.setIconSize(QSize(80,79))
        self.button0.setGeometry(100,505,80,80)
        self.button0.setProperty("value","0")
        self.button0.clicked.connect(self.button_clicked)


        self.buttonadd=QPushButton(self)
        self.buttonadd.setIcon(QIcon(resourcepath("templates/+button.png")))
        self.buttonadd.setIconSize(QSize(80,79))
        self.buttonadd.setGeometry(295,340,80,80)
        self.buttonadd.setProperty("value","+")
        self.buttonadd.clicked.connect(self.button_clicked)


        self.buttonminus=QPushButton(self)
        self.buttonminus.setIcon(QIcon(resourcepath("templates/-button.png")))
        self.buttonminus.setIconSize(QSize(80,79))
        self.buttonminus.setGeometry(295,395,80,80)
        self.buttonminus.setProperty("value","-")
        self.buttonminus.clicked.connect(self.button_clicked)


        self.buttonmul=QPushButton(self)
        self.buttonmul.setIcon(QIcon(resourcepath("templates/Xbutton.png")))
        self.buttonmul.setIconSize(QSize(80,79))
        self.buttonmul.setGeometry(295,450,80,80)
        self.buttonmul.setProperty("value","*")
        self.buttonmul.clicked.connect(self.button_clicked)


        self.buttondiv=QPushButton(self)
        self.buttondiv.setIcon(QIcon(resourcepath("templates/divisionbutton.png")))
        self.buttondiv.setIconSize(QSize(80,79))
        self.buttondiv.setGeometry(295,505,80,80)
        self.buttondiv.setProperty("value","/")
        self.buttondiv.clicked.connect(self.button_clicked)

        self.buttonc=QPushButton(self)
        self.buttonc.setIcon(QIcon(resourcepath("templates/clearbutton.png")))
        self.buttonc.setIconSize(QSize(80,79))
        self.buttonc.setGeometry(43,395,80,80)
        self.buttonc.clicked.connect(self.clear_button)


        self.buttone=QPushButton(self)
        self.buttone.setIcon(QIcon(resourcepath("templates/=button.png")))
        self.buttone.setIconSize(QSize(80,79))
        self.buttone.setGeometry(355,395,80,80)
        self.buttone.clicked.connect(self.equal_button)
        
    


        self.setStyleSheet("""QPushButton{
                           border:none;
                           padding:0px;
                           margin:0px
                           }
                           QLineEdit{
                           background-color:hsl(294,39%,72%);
                           border-radius:10px;
                           border-color:#e3c98d}
                           """)
        buttons=[self.button0,self.button1,self.button2,self.button3,self.button4,
                 self.button5,self.button6,
                 self.button7,self.button8,self.button9,self.buttonadd,self.buttonminus,
                 self.buttondiv,
                 self.buttonmul,self.buttonc,self.buttone]
        def add_hover_effect(button):
            click=QGraphicsOpacityEffect(button)
            button.setGraphicsEffect(click)
            click.setOpacity(1.0)
            button.enterEvent= lambda event: click.setOpacity(0.6)
            button.leaveEvent= lambda event: click.setOpacity(1.0) 

        for btn in buttons:
            
            btn.setFixedSize(70,69)
            add_hover_effect(btn)
            
    def mousePressEvent(self,event):
        if event.buttons()== Qt.LeftButton:
           self.dragPos=event.globalPos()-self.frameGeometry().topLeft()
           event.accept() 
           print("yfyf")
    def mouseMoveEvent(self, event):
        if event.buttons()== Qt.LeftButton:
           self.move(event.globalPos()-self.dragPos)
           event.accept()

    def button_clicked(self):
        button= self.sender()
        value=button.property("value")
        self.display.setText(self.display.text()+ value)

    def clear_button(self):
        self.display.setText(None)

    def equal_button(self):
        expression=self.display.text()
        try:
           result = eval(expression)
        except Exception as e:
           result = f"Error: {e}"
        self.display.setText(f"{result}")
        
def main():
    app=QApplication(sys.argv)
    window=mushcalc()
    window.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()