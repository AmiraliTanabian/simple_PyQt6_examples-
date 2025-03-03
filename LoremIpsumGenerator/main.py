from PyQt6.QtGui import QCursor
from PyQt6.QtCore import QSize, QRect, QMetaObject, QCoreApplication, Qt
from PyQt6.QtWidgets import (QPushButton, QLabel, QHBoxLayout, QTextEdit, QApplication, QWidget, QMainWindow,
                    QSpinBox, QComboBox, QMessageBox)
from lorem_text import lorem
from pyperclip import copy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 467)
        MainWindow.setMinimumSize(QSize(483, 467))
        MainWindow.setMaximumSize(QSize(483, 467))
        MainWindow.setStyleSheet("background:rgb(61, 56, 70)")
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(parent=self.centralwidget)
        self.label.setGeometry(QRect(130, 20, 230, 19))
        self.label.setStyleSheet("color:white;font-weight:bold;font-size:20px;")
        self.label.setObjectName("label")
        self.textEdit = QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QRect(10, 110, 450, 301))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QRect(280, 420, 88, 27))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background:rgb(246, 97, 81)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.exit_btn)
        self.pushButton_3 = QPushButton(parent=self.centralwidget)
        self.pushButton_3.clicked.connect(self.copy_btn)
        self.pushButton_3.setGeometry(QRect(370, 420, 88, 27))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color:White;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QRect(10, 71, 450, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QSpinBox(parent=self.widget)
        self.spinBox.setStyleSheet("color:White;")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.comboBox = QComboBox(parent=self.widget)
        self.comboBox.currentIndexChanged.connect(self.comboChanged)
        self.comboBox.setStyleSheet("color:White;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Sentence', 'Word', 'Paragraph'])
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QPushButton(parent=self.widget)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("color:White;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.finally_func)
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lorem Ipsum Generator"))
        self.label.setText(_translate("MainWindow", "Lorem Ipsum Generator"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_3.setText(_translate("MainWindow", "Copy"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sentence"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Word"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Paragraph"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))

    def sentence_generator(self):
        result = lorem.sentence()
        self.textEdit.setText(result)

    def word_generator(self):
        number = self.spinBox.value()
        result = lorem.words(number)
        self.textEdit.setText(result)

    def paragraph_generator(self):
        number = self.spinBox.value()
        result = lorem.paragraphs(number)
        self.textEdit.setText(result)

    def finally_func(self):
        status_by_functions = {
            'Paragraph' : self.paragraph_generator,
            'Word':self.word_generator,
            'Sentence':self.sentence_generator
        }

        # Run function
        status_by_functions[self.comboBox.currentText()]()

    def exit_btn(self):
        MainWindow.close()

    def copy_btn(self):
        current_text = self.textEdit.toPlainText()
        copy(current_text)

        # show result msg
        msgBox = QMessageBox(parent=MainWindow)
        msgBox.setText("Text copied!")
        msgBox.setWindowTitle('Copied!')
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.exec()
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

    def comboChanged(self):
        if self.comboBox.currentText() == 'Sentence':
            self.spinBox.clear()
            self.spinBox.setDisabled(True)

        else:
            self.spinBox.setEnabled(True)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
