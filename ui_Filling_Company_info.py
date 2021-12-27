# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Filling Company infoXrZWaG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1023, 755)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1061, 761))
        self.tabWidget.setStyleSheet(u"background-color: rgb(155, 204, 255);\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 291, 101))
        self.label.setStyleSheet(u"font: 24pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 210, 191, 31))
        self.label_2.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 260, 191, 51))
        self.label_3.setStyleSheet(u"font: 16pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 540, 161, 51))
        self.pushButton.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(330, 210, 161, 41))
        self.lineEdit.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(330, 270, 161, 41))
        self.lineEdit_2.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(360, 540, 161, 51))
        self.pushButton_3.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 9):
            self.tableWidget.setRowCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(660, 100, 211, 301))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 20, 331, 101))
        self.label_6.setStyleSheet(u"font: 26pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.tableWidget_2.rowCount() < 9):
            self.tableWidget_2.setRowCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem21)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(670, 110, 261, 371))
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 140, 531, 301))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(290, 240, 141, 61))
        self.pushButton_4.setStyleSheet(u"color: White;\n"
"font: 16pt \"Microsoft JhengHei\";\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 20, 151, 31))
        self.label_8.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 240, 141, 61))
        self.pushButton_2.setStyleSheet(u"color: White;\n"
"background-color: #008CBA ;\n"
"border-radius: 12px;\n"
"font: 14pt \"Microsoft JhengHei\";")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 80, 141, 41))
        self.label_9.setStyleSheet(u"font: 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(320, 90, 171, 41))
        self.lineEdit_7.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(320, 20, 171, 41))
        self.lineEdit_6.setStyleSheet(u"background: #fff;\n"
"    width: 100px;\n"
"    height: 100px;\n"
"    border-radius: 20px;")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Information ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Departments", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Department", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Department ID", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Update", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Department", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Dep_ID", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Department", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Job Description", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Job Title", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Job ID", None));
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Update", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Job title", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Job_ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Job", None))
    # retranslateUi

