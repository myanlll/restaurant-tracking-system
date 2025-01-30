# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fiyatlar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(375, 326)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 0, 341, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 300, 341, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 200, 341, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 220, 340, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.push_kaydet = QPushButton(self.horizontalLayoutWidget_3)
        self.push_kaydet.setObjectName(u"push_kaydet")

        self.horizontalLayout_3.addWidget(self.push_kaydet)

        self.push_cikis = QPushButton(self.horizontalLayoutWidget_3)
        self.push_cikis.setObjectName(u"push_cikis")

        self.horizontalLayout_3.addWidget(self.push_cikis)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 341, 181))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_kiz = QLabel(self.horizontalLayoutWidget)
        self.label_kiz.setObjectName(u"label_kiz")

        self.verticalLayout.addWidget(self.label_kiz)

        self.label_ogl = QLabel(self.horizontalLayoutWidget)
        self.label_ogl.setObjectName(u"label_ogl")

        self.verticalLayout.addWidget(self.label_ogl)

        self.label_bur = QLabel(self.horizontalLayoutWidget)
        self.label_bur.setObjectName(u"label_bur")

        self.verticalLayout.addWidget(self.label_bur)

        self.label_piz = QLabel(self.horizontalLayoutWidget)
        self.label_piz.setObjectName(u"label_piz")

        self.verticalLayout.addWidget(self.label_piz)

        self.label_che = QLabel(self.horizontalLayoutWidget)
        self.label_che.setObjectName(u"label_che")

        self.verticalLayout.addWidget(self.label_che)

        self.label_ice = QLabel(self.horizontalLayoutWidget)
        self.label_ice.setObjectName(u"label_ice")

        self.verticalLayout.addWidget(self.label_ice)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lin_kiz = QLineEdit(self.horizontalLayoutWidget)
        self.lin_kiz.setObjectName(u"lin_kiz")

        self.verticalLayout_3.addWidget(self.lin_kiz)

        self.lin_ogl = QLineEdit(self.horizontalLayoutWidget)
        self.lin_ogl.setObjectName(u"lin_ogl")

        self.verticalLayout_3.addWidget(self.lin_ogl)

        self.lin_bur = QLineEdit(self.horizontalLayoutWidget)
        self.lin_bur.setObjectName(u"lin_bur")

        self.verticalLayout_3.addWidget(self.lin_bur)

        self.lin_piz = QLineEdit(self.horizontalLayoutWidget)
        self.lin_piz.setObjectName(u"lin_piz")

        self.verticalLayout_3.addWidget(self.lin_piz)

        self.lin_che = QLineEdit(self.horizontalLayoutWidget)
        self.lin_che.setObjectName(u"lin_che")

        self.verticalLayout_3.addWidget(self.lin_che)

        self.lin_ice = QLineEdit(self.horizontalLayoutWidget)
        self.lin_ice.setObjectName(u"lin_ice")

        self.verticalLayout_3.addWidget(self.lin_ice)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Fiyatlar", u"Fiyatlar", None))
        self.push_kaydet.setText(QCoreApplication.translate("Fiyatlar", u"Kaydet", None))
        self.push_cikis.setText(QCoreApplication.translate("Fiyatlar", u"\u00c7\u0131k\u0131\u015f", None))
        self.label_kiz.setText(QCoreApplication.translate("Fiyatlar", u"K\u0131zartma", None))
        self.label_ogl.setText(QCoreApplication.translate("Fiyatlar", u"\u00d6\u011fle Yeme\u011fi", None))
        self.label_bur.setText(QCoreApplication.translate("Fiyatlar", u"Burger", None))
        self.label_piz.setText(QCoreApplication.translate("Fiyatlar", u"Pizza", None))
        self.label_che.setText(QCoreApplication.translate("Fiyatlar", u"Cheese Burger", None))
        self.label_ice.setText(QCoreApplication.translate("Fiyatlar", u"\u0130\u00e7ecekler", None))
    # retranslateUi

