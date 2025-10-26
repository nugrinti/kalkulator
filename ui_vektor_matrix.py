# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_vektor.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 10, 151, 31))
        font = QFont()
        font.setFamilies([u"8514oem"])
        self.label_2.setFont(font)
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 40, 371, 201))
        self.pushButton_add_5 = QPushButton(Dialog)
        self.pushButton_add_5.setObjectName(u"pushButton_add_5")
        self.pushButton_add_5.setGeometry(QRect(200, 250, 81, 31))
        self.pushButton_add_4 = QPushButton(Dialog)
        self.pushButton_add_4.setObjectName(u"pushButton_add_4")
        self.pushButton_add_4.setGeometry(QRect(120, 250, 81, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"History Vektor", None))
        self.pushButton_add_5.setText(QCoreApplication.translate("Dialog", u"CLOSE", None))
        self.pushButton_add_4.setText(QCoreApplication.translate("Dialog", u"CLEAR", None))
    # retranslateUi

