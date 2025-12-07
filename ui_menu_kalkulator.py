# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_kalkulator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 600)
        font = QFont()
        font.setFamilies([u"Consolas", u"Monospace", u"MS Shell Dlg 2"])
        font.setPointSize(9)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 951, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 941, 617))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)

        self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_name, 2, 3, 1, 1)

        self.btn_checkLower = QPushButton(self.gridLayoutWidget)
        self.btn_checkLower.setObjectName(u"btn_checkLower")

        self.gridLayout.addWidget(self.btn_checkLower, 12, 4, 1, 1)

        self.text_result = QLabel(self.gridLayoutWidget)
        self.text_result.setObjectName(u"text_result")

        self.gridLayout.addWidget(self.text_result, 15, 0, 1, 4)

        self.tableWidget_matrix = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_matrix.setObjectName(u"tableWidget_matrix")

        self.gridLayout.addWidget(self.tableWidget_matrix, 11, 0, 1, 4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)

        self.btn_clearOutput = QPushButton(self.gridLayoutWidget)
        self.btn_clearOutput.setObjectName(u"btn_clearOutput")

        self.gridLayout.addWidget(self.btn_clearOutput, 19, 4, 1, 1)

        self.btn_displayDiagonal = QPushButton(self.gridLayoutWidget)
        self.btn_displayDiagonal.setObjectName(u"btn_displayDiagonal")

        self.gridLayout.addWidget(self.btn_displayDiagonal, 10, 4, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)

        self.btn_checkIdentity_2 = QPushButton(self.gridLayoutWidget)
        self.btn_checkIdentity_2.setObjectName(u"btn_checkIdentity_2")

        self.gridLayout.addWidget(self.btn_checkIdentity_2, 5, 4, 1, 1)

        self.pushButton_evaluate = QPushButton(self.gridLayoutWidget)
        self.pushButton_evaluate.setObjectName(u"pushButton_evaluate")

        self.gridLayout.addWidget(self.pushButton_evaluate, 14, 3, 1, 1)

        self.spinBox_cols = QSpinBox(self.gridLayoutWidget)
        self.spinBox_cols.setObjectName(u"spinBox_cols")

        self.gridLayout.addWidget(self.spinBox_cols, 8, 3, 1, 1)

        self.comboBox_type = QComboBox(self.gridLayoutWidget)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.gridLayout.addWidget(self.comboBox_type, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 4)

        self.doubleSpinBox_scalar = QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_scalar.setObjectName(u"doubleSpinBox_scalar")

        self.gridLayout.addWidget(self.doubleSpinBox_scalar, 4, 3, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEdit_expression = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_expression.setObjectName(u"lineEdit_expression")

        self.gridLayout.addWidget(self.lineEdit_expression, 14, 1, 1, 2)

        self.btn_checkIdentity_3 = QPushButton(self.gridLayoutWidget)
        self.btn_checkIdentity_3.setObjectName(u"btn_checkIdentity_3")

        self.gridLayout.addWidget(self.btn_checkIdentity_3, 6, 4, 1, 1)

        self.btn_checkIdentity_4 = QPushButton(self.gridLayoutWidget)
        self.btn_checkIdentity_4.setObjectName(u"btn_checkIdentity_4")

        self.gridLayout.addWidget(self.btn_checkIdentity_4, 7, 4, 1, 1)

        self.btn_checkSparse = QPushButton(self.gridLayoutWidget)
        self.btn_checkSparse.setObjectName(u"btn_checkSparse")

        self.gridLayout.addWidget(self.btn_checkSparse, 15, 4, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setFamilies([u"Consolas", u"Monospace", u"MS Shell Dlg 2"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.btn_checkIdentity = QPushButton(self.gridLayoutWidget)
        self.btn_checkIdentity.setObjectName(u"btn_checkIdentity")

        self.gridLayout.addWidget(self.btn_checkIdentity, 13, 4, 1, 1)

        self.spinBox_rows = QSpinBox(self.gridLayoutWidget)
        self.spinBox_rows.setObjectName(u"spinBox_rows")

        self.gridLayout.addWidget(self.spinBox_rows, 8, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 14, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 4)

        self.btn_displayMatrix = QPushButton(self.gridLayoutWidget)
        self.btn_displayMatrix.setObjectName(u"btn_displayMatrix")

        self.gridLayout.addWidget(self.btn_displayMatrix, 8, 4, 1, 1)

        self.btn_checkZero = QPushButton(self.gridLayoutWidget)
        self.btn_checkZero.setObjectName(u"btn_checkZero")

        self.gridLayout.addWidget(self.btn_checkZero, 14, 4, 1, 1)

        self.spinBox_4 = QSpinBox(self.gridLayoutWidget)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout.addWidget(self.spinBox_4, 1, 1, 1, 1)

        self.listWidget_objects = QListWidget(self.gridLayoutWidget)
        self.listWidget_objects.setObjectName(u"listWidget_objects")

        self.gridLayout.addWidget(self.listWidget_objects, 13, 0, 1, 4)

        self.btn_checkUpper = QPushButton(self.gridLayoutWidget)
        self.btn_checkUpper.setObjectName(u"btn_checkUpper")

        self.gridLayout.addWidget(self.btn_checkUpper, 11, 4, 1, 1)

        self.textEdit_result = QTextEdit(self.gridLayoutWidget)
        self.textEdit_result.setObjectName(u"textEdit_result")

        self.gridLayout.addWidget(self.textEdit_result, 16, 0, 7, 4)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 8, 2, 1, 1)

        self.btn_checkIdentity_5 = QPushButton(self.gridLayoutWidget)
        self.btn_checkIdentity_5.setObjectName(u"btn_checkIdentity_5")

        self.gridLayout.addWidget(self.btn_checkIdentity_5, 4, 4, 1, 1)

        self.pushButton_add = QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout.addWidget(self.pushButton_add, 2, 4, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 941, 531))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_displayMatrix_5 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_5.setObjectName(u"btn_displayMatrix_5")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_5, 9, 1, 1, 1)

        self.btn_displayMatrix_11 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_11.setObjectName(u"btn_displayMatrix_11")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_11, 4, 1, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)

        self.btn_displayMatrix_4 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_4.setObjectName(u"btn_displayMatrix_4")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_4, 8, 1, 1, 1)

        self.text_result_3 = QLabel(self.gridLayoutWidget_2)
        self.text_result_3.setObjectName(u"text_result_3")

        self.gridLayout_2.addWidget(self.text_result_3, 9, 0, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.btn_displayMatrix_13 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_13.setObjectName(u"btn_displayMatrix_13")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_13, 6, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 7, 0, 1, 1)

        self.tableWidget_matrix_3 = QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget_matrix_3.setObjectName(u"tableWidget_matrix_3")

        self.gridLayout_2.addWidget(self.tableWidget_matrix_3, 8, 0, 1, 1)

        self.btn_displayMatrix_6 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_6.setObjectName(u"btn_displayMatrix_6")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_6, 10, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_2.addWidget(self.spinBox_2, 3, 1, 1, 1)

        self.btn_displayMatrix_3 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_3.setObjectName(u"btn_displayMatrix_3")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_3, 7, 1, 1, 1)

        self.btn_displayMatrix_12 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_12.setObjectName(u"btn_displayMatrix_12")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_12, 5, 1, 1, 1)

        self.spinBox = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.textEdit_result_3 = QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_result_3.setObjectName(u"textEdit_result_3")

        self.gridLayout_2.addWidget(self.textEdit_result_3, 10, 0, 1, 1)

        self.btn_displayMatrix_18 = QPushButton(self.gridLayoutWidget_2)
        self.btn_displayMatrix_18.setObjectName(u"btn_displayMatrix_18")

        self.gridLayout_2.addWidget(self.btn_displayMatrix_18, 11, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 941, 531))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.gridLayout_4.addWidget(self.label_27, 0, 0, 1, 2)

        self.btn_displayMatrix_7 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_7.setObjectName(u"btn_displayMatrix_7")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_7, 4, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_4.addWidget(self.spinBox_3, 1, 1, 1, 1)

        self.btn_displayMatrix_10 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_10.setObjectName(u"btn_displayMatrix_10")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_10, 5, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 3, 0, 1, 1)

        self.textEdit_result_4 = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_result_4.setObjectName(u"textEdit_result_4")

        self.gridLayout_4.addWidget(self.textEdit_result_4, 7, 1, 3, 1)

        self.btn_displayMatrix_9 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_9.setObjectName(u"btn_displayMatrix_9")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_9, 5, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 1, 0, 1, 1)

        self.text_result_4 = QLabel(self.gridLayoutWidget_3)
        self.text_result_4.setObjectName(u"text_result_4")

        self.gridLayout_4.addWidget(self.text_result_4, 7, 0, 3, 1)

        self.btn_displayMatrix_8 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_8.setObjectName(u"btn_displayMatrix_8")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_8, 4, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 2, 0, 1, 1)

        self.btn_displayMatrix_14 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_14.setObjectName(u"btn_displayMatrix_14")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_14, 1, 2, 1, 1)

        self.btn_displayMatrix_15 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_15.setObjectName(u"btn_displayMatrix_15")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_15, 2, 2, 1, 1)

        self.btn_displayMatrix_16 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_16.setObjectName(u"btn_displayMatrix_16")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_16, 3, 2, 1, 1)

        self.btn_displayMatrix_17 = QPushButton(self.gridLayoutWidget_3)
        self.btn_displayMatrix_17.setObjectName(u"btn_displayMatrix_17")

        self.gridLayout_4.addWidget(self.btn_displayMatrix_17, 4, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nama :", None))
        self.btn_checkLower.setText(QCoreApplication.translate("MainWindow", u"Check Lower Triangle", None))
        self.text_result.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baris (m) : ", None))
        self.btn_clearOutput.setText(QCoreApplication.translate("MainWindow", u"Clear Output", None))
        self.btn_displayDiagonal.setText(QCoreApplication.translate("MainWindow", u"Display Diagonal", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nilai :", None))
        self.btn_checkIdentity_2.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.pushButton_evaluate.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Matriks", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Skalar", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DAFTAR INPUT", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Jenis : ", None))
        self.btn_checkIdentity_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btn_checkIdentity_4.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.btn_checkSparse.setText(QCoreApplication.translate("MainWindow", u"Check Sparse", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">KALKULATOR MATRIKS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Jumlah input :", None))
        self.btn_checkIdentity.setText(QCoreApplication.translate("MainWindow", u"Check Identity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OPERASI :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Masukkan elemen matriks (m x n ) : ", None))
        self.btn_displayMatrix.setText(QCoreApplication.translate("MainWindow", u"Display Matrix", None))
        self.btn_checkZero.setText(QCoreApplication.translate("MainWindow", u"Check Zero", None))
        self.btn_checkUpper.setText(QCoreApplication.translate("MainWindow", u"Check Upper Traingle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kolom (n) :", None))
        self.btn_checkIdentity_5.setText(QCoreApplication.translate("MainWindow", u"Quiz", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OPTIONS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Matriks", None))
        self.btn_displayMatrix_5.setText(QCoreApplication.translate("MainWindow", u"Solve Crammer", None))
        self.btn_displayMatrix_11.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Jumlah Variabel :", None))
        self.btn_displayMatrix_4.setText(QCoreApplication.translate("MainWindow", u"Solve Invers Matrix", None))
        self.text_result_3.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">KALKULATOR SISTEM PERSAMAAN LINEAR</span></p></body></html>", None))
        self.btn_displayMatrix_13.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Input Sistem Persamaan Linear", None))
        self.btn_displayMatrix_6.setText(QCoreApplication.translate("MainWindow", u"Clear Output", None))
        self.btn_displayMatrix_3.setText(QCoreApplication.translate("MainWindow", u"Solve Gaussian", None))
        self.btn_displayMatrix_12.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Jumlah Persamaan : ", None))
        self.btn_displayMatrix_18.setText(QCoreApplication.translate("MainWindow", u"Quiz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sistem Persamaan Linear", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">KALKULATOR VEKTOR</span></p></body></html>", None))
        self.btn_displayMatrix_7.setText(QCoreApplication.translate("MainWindow", u"Cross Product", None))
        self.btn_displayMatrix_10.setText(QCoreApplication.translate("MainWindow", u"Sudut Antar Vektor", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Input Vektor B :", None))
        self.btn_displayMatrix_9.setText(QCoreApplication.translate("MainWindow", u"Clear Output", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Dimensi Vektor :", None))
        self.text_result_4.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.btn_displayMatrix_8.setText(QCoreApplication.translate("MainWindow", u"Dot Product", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Input Vektor A :", None))
        self.btn_displayMatrix_14.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.btn_displayMatrix_15.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btn_displayMatrix_16.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.btn_displayMatrix_17.setText(QCoreApplication.translate("MainWindow", u"Quiz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Vektor", None))
    # retranslateUi

