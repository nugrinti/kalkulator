# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_matrix.ui'
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 151, 31))
        font = QFont()
        font.setFamilies([u"8514oem"])
        self.label.setFont(font)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 371, 201))
        self.pushButton_add_2 = QPushButton(Dialog)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setGeometry(QRect(120, 250, 81, 31))
        self.pushButton_add_3 = QPushButton(Dialog)
        self.pushButton_add_3.setObjectName(u"pushButton_add_3")
        self.pushButton_add_3.setGeometry(QRect(200, 250, 81, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"History Matriks", None))
        self.pushButton_add_2.setText(QCoreApplication.translate("Dialog", u"CLEAR", None))
        self.pushButton_add_3.setText(QCoreApplication.translate("Dialog", u"CLOSE", None))
    # retranslateUi

