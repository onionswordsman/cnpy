import random
import json
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as gui

#class initialization (create the class mainwindow which inherits the properties of qtw.QWidget)

with open("chinese.json", "r") as cn:
        dictionaryj = json.load(cn)

print(type(dictionaryj))

thwj=[1,2]

class MainWindow(qtw.QWidget):
        #this is just def init
        def __init__(self):
                #super is the parent. youre putting the parent(qtw.QWidget)'s init into this class's init
                super().__init__()

                #set window size
                self.resize(1280, 720)
                self.setMinimumSize(1280, 720)
                self.setMaximumSize(1280, 720)
                
                #make the welcome image
                welcome = qtw.QLabel(self)
                pixmap = gui.QPixmap('image.png')
                welcome.setPixmap(pixmap)

                #set window title to Justin Title
                self.setWindowTitle("Justin Title")

                #set the layout to QVerticalBoxLayout
                self.setLayout(qtw.QVBoxLayout())

                #create marks
                marks = qtw.QLabel("This session:")
                marks.hide()
                

                #create a label called titleLabel which has the text justin label
                titleLabel = qtw.QLabel("pick an activity")
                
                #change font size of label
                titleLabel.setFont(gui.QFont("Helvetica", 18))
                
                #create an entry box
#                titleEntry = qtw.QLineEdit()
#                titleEntry.setObjectName("name_field")
#                titleEntry.setText("Your name")

                #create a button
                thisButton = qtw.QPushButton("Enter", clicked = lambda: pressed())
                thisButton.resize(70,30)

                #create a combo box (idiots at qt dont know what a dropdown selection is)
                actPick = qtw.QComboBox(self)
                #add items to combo box
                #multiple ways
                actPick.addItem("Translate Chinese to English", 1)
                actPick.addItem("Translate English to Chinese", 2)

                #make and then hide the return to menu button
                menuReturn = qtw.QPushButton("Reopen activity picker", clicked = lambda: menu_return())
                menuReturn.resize(70,30)
                menuReturn.hide()

                #create the activities
                EngtoCn = qtw.QGroupBox("English to Chinese")
                etcQuestionLabel = qtw.QLabel()
                etcQuestionEntry = qtw.QLineEdit()
                etcSubmit = qtw.QPushButton("Submit", clicked = lambda: submit_answer(etcQuestionEntry.text(), 1))
                etcSubmit.resize(70,30)
                xbox = qtw.QVBoxLayout()
                xbox.addWidget(etcQuestionLabel)
                xbox.addWidget(etcQuestionEntry)
                xbox.addWidget(etcSubmit)
                xbox.addStretch(1)
                EngtoCn.setLayout(xbox)
                EngtoCn.hide()

                CntoEng = qtw.QGroupBox("Chinese to English")
                cteQuestionLabel = qtw.QLabel()
                cteQuestionEntry = qtw.QLineEdit()
                cteSubmit = qtw.QPushButton("Submit", clicked = lambda: submit_answer(cteQuestionEntry.text(), 0))
                vbox = qtw.QVBoxLayout()
                vbox.addWidget(cteQuestionLabel)
                vbox.addWidget(cteQuestionEntry)
                vbox.addWidget(cteSubmit)
                vbox.addStretch(1)
                CntoEng.setLayout(vbox)
                CntoEng.hide()
                
                #add the widgets to the self's layout (you should call this after each widget is made, not all at once)
                self.layout().addWidget(welcome)
                self.layout().addWidget(marks)
                self.layout().addWidget(titleLabel)
#                self.layout().addWidget(titleEntry)
                self.layout().addWidget(actPick)
                self.layout().addWidget(thisButton)
                self.layout().addWidget(menuReturn)
                self.layout().addWidget(EngtoCn)
                self.layout().addWidget(CntoEng)

                
                #show this widget when the window opens
                self.show()

                def menu_return():
                        actPick.show()
                        titleLabel.show()
                        thisButton.show()

                def submit_answer(x, i):
                        #remember to show marks

                        correct = False

                        x = x.lower()
                        x = x.replace(" ","")
                        print(x)
                        if i != 1:
                                for z in answer:
                                        if x == z:
                                                correct = True
                        elif i == 1:
                                kill = ""
                                murder = kill.join(answer)
                                if murder == x:
                                        correct = True
                        if correct == True:
                                markText = marks.text() + u'\u2713'
                                marks.setText(markText)
                        elif correct != True:
                                markText = marks.text() + u'\u274C'
                                marks.setText(markText)
                        marks.show()
                        p = i
                        StartAct(p)

                def StartAct(x):
                        seld = random.choice(dictionaryj)
                        global answer
                        if x==0:
                                cteQuestionLabel.setText(f"Translate {seld['cn']} into English")
                                answer = seld["eng"]
                                cteQuestionEntry.clear()
                        elif x==1:
                                etcQuestionLabel.setText(f"Translate {seld['eng']} into Chinese")
                                answer = seld["cn"]
                                etcQuestionEntry.clear()
                                

                def startActivity(x):
                        print(str(x))
                        menuReturn.show()
                        welcome.hide()
                        titleLabel.hide()
                        thisButton.hide()
                        actPick.hide()

                        if x == 0:
                                CntoEng.show()
                                StartAct(0)
                                EngtoCn.hide()
                        elif x == 1:
                                EngtoCn.show()
                                StartAct(1)
                                CntoEng.hide()


                def pressed():
#                        titleLabel.setText(f"{titleEntry.text()}")
#                        titleEntry.setText("")       
#                        titleEntry.hide()
                        startActivity(actPick.currentIndex())
                

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
