# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweetFormLast.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(511, 655)
        Dialog.setBaseSize(QtCore.QSize(100, 200))
        self.theme = QtWidgets.QLineEdit(Dialog)
        self.theme.setGeometry(QtCore.QRect(10, 20, 491, 31))
        self.theme.setObjectName("theme")
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(320, 100, 161, 31))
        self.find.setObjectName("find")
        self.fromD = QtWidgets.QDateEdit(Dialog)
        self.fromD.setGeometry(QtCore.QRect(370, 70, 110, 22))
        self.fromD.setObjectName("fromD")
        self.toD = QtWidgets.QDateEdit(Dialog)
        self.toD.setGeometry(QtCore.QRect(220, 70, 110, 22))
        self.toD.setObjectName("toD")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 21, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 70, 21, 21))
        self.label_2.setObjectName("label_2")
        self.isUseData = QtWidgets.QRadioButton(Dialog)
        self.isUseData.setGeometry(QtCore.QRect(30, 60, 161, 41))
        self.isUseData.setObjectName("isUseData")
        self.countTweets = QtWidgets.QLineEdit(Dialog)
        self.countTweets.setGeometry(QtCore.QRect(160, 100, 141, 31))
        self.countTweets.setObjectName("countTweets")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableRes = QtWidgets.QTableWidget(Dialog)
        self.tableRes.setGeometry(QtCore.QRect(10, 350, 491, 291))
        self.tableRes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableRes.setAutoFillBackground(False)
        self.tableRes.setFrameShape(QtWidgets.QFrame.Box)
        self.tableRes.setAlternatingRowColors(True)
        self.tableRes.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableRes.setShowGrid(False)
        self.tableRes.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableRes.setWordWrap(True)
        self.tableRes.setCornerButtonEnabled(True)
        self.tableRes.setRowCount(15)
        self.tableRes.setColumnCount(3)
        self.tableRes.setObjectName("tableRes")
        item = QtWidgets.QTableWidgetItem()
        self.tableRes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRes.setItem(0, 2, item)
        self.tableRes.horizontalHeader().setVisible(True)
        self.tableRes.horizontalHeader().setCascadingSectionResizes(False)
        self.tableRes.horizontalHeader().setHighlightSections(True)
        self.tableRes.horizontalHeader().setSortIndicatorShown(False)
        self.tableRes.horizontalHeader().setStretchLastSection(True)
        self.tableRes.verticalHeader().setVisible(False)
        self.tableRes.verticalHeader().setHighlightSections(True)
        self.tableRes.verticalHeader().setSortIndicatorShown(False)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.graph = QtWidgets.QLabel(Dialog)
        self.graph.setGeometry(QtCore.QRect(210, 145, 320, 190))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(10)
        self.graph.setFont(font)
        self.graph.setTextFormat(QtCore.Qt.AutoText)
        self.graph.setObjectName("graph")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.theme.setText(_translate("Dialog", " Введдите интресующую тему"))
        self.find.setText(_translate("Dialog", "Найти"))
        self.label.setText(_translate("Dialog", "От"))
        self.label_2.setText(_translate("Dialog", "До"))
        self.isUseData.setText(_translate("Dialog", "Получить данные за месяц"))
        self.label_3.setText(_translate("Dialog", "Количество твитов:"))
        __sortingEnabled = self.tableRes.isSortingEnabled()
        self.tableRes.setSortingEnabled(False)
        self.tableRes.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Dialog", "Процент положительных и"))
        self.label_5.setText(_translate("Dialog", "отрициательных мнений"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
