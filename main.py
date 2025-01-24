
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 460)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_item)
        self.horizontalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.clicked.connect(self.remove_item)
        self.horizontalLayout.addWidget(self.remove_btn)
        self.sort_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sort_btn.setObjectName("sort_btn")
        self.sort_btn.clicked.connect(self.sort_items)
        self.horizontalLayout.addWidget(self.sort_btn)
        self.edit_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit_item)
        self.horizontalLayout.addWidget(self.edit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.remove_btn.setText(_translate("MainWindow", "Remove"))
        self.sort_btn.setText(_translate("MainWindow", "Sort"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))

    def remove_item(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle('Remove Item')
        msgBox.setText('Are you sure you want to delete the item?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
        msgBox.buttonClicked.connect(self.msgHandler)
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.exec()
        


    def msgHandler(self, button):
        # ok button clicked:
        if button.text() == '&OK' :
            current_row = self.listWidget.currentRow()
            self.listWidget.takeItem(current_row)


    def add_item(self):
        currentIndex = self.listWidget.currentRow()
        data, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Add Item', 'Enter the new item to add on list', 
                                                  QtWidgets.QLineEdit.EchoMode.Normal)
        if data and ok : 
            self.listWidget.insertItem(currentIndex, data)

    def sort_items(self):
        self.listWidget.sortItems()

    def edit_item(self):
        currentIndex = self.listWidget.currentRow()
        data , ok = QtWidgets.QInputDialog.getText(MainWindow, 'Edit item', 'Enter new value',
                                                   QtWidgets.QLineEdit.EchoMode.Normal, self.listWidget.item(currentIndex).text())
        if data and ok : 
            self.listWidget.item(currentIndex).setText(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
