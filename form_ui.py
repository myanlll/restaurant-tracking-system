# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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

class Ui_RestoranTakip(object):
    def setupUi(self, RestoranTakip):
        if not RestoranTakip.objectName():
            RestoranTakip.setObjectName(u"RestoranTakip")
        RestoranTakip.resize(980, 362)
        self.line = QFrame(RestoranTakip)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 230, 941, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(RestoranTakip)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 10, 941, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget_3 = QWidget(RestoranTakip)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(620, 28, 342, 201))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.sonuc = QLineEdit(self.verticalLayoutWidget_3)
        self.sonuc.setObjectName(u"sonuc")
        self.sonuc.setEnabled(False)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.sonuc.setFont(font)
        self.sonuc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.sonuc)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pMod = QPushButton(self.verticalLayoutWidget_3)
        self.pMod.setObjectName(u"pMod")

        self.horizontalLayout_23.addWidget(self.pMod)

        self.pWipe = QPushButton(self.verticalLayoutWidget_3)
        self.pWipe.setObjectName(u"pWipe")

        self.horizontalLayout_23.addWidget(self.pWipe)

        self.pPN = QPushButton(self.verticalLayoutWidget_3)
        self.pPN.setObjectName(u"pPN")

        self.horizontalLayout_23.addWidget(self.pPN)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.p1divX = QPushButton(self.verticalLayoutWidget_3)
        self.p1divX.setObjectName(u"p1divX")

        self.horizontalLayout_24.addWidget(self.p1divX)

        self.pxSq = QPushButton(self.verticalLayoutWidget_3)
        self.pxSq.setObjectName(u"pxSq")

        self.horizontalLayout_24.addWidget(self.pxSq)

        self.pRootSq = QPushButton(self.verticalLayoutWidget_3)
        self.pRootSq.setObjectName(u"pRootSq")

        self.horizontalLayout_24.addWidget(self.pRootSq)

        self.pdiv = QPushButton(self.verticalLayoutWidget_3)
        self.pdiv.setObjectName(u"pdiv")

        self.horizontalLayout_24.addWidget(self.pdiv)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.p7 = QPushButton(self.verticalLayoutWidget_3)
        self.p7.setObjectName(u"p7")

        self.horizontalLayout_27.addWidget(self.p7)

        self.p8 = QPushButton(self.verticalLayoutWidget_3)
        self.p8.setObjectName(u"p8")

        self.horizontalLayout_27.addWidget(self.p8)

        self.p9 = QPushButton(self.verticalLayoutWidget_3)
        self.p9.setObjectName(u"p9")

        self.horizontalLayout_27.addWidget(self.p9)

        self.pX = QPushButton(self.verticalLayoutWidget_3)
        self.pX.setObjectName(u"pX")

        self.horizontalLayout_27.addWidget(self.pX)


        self.verticalLayout_9.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.p4 = QPushButton(self.verticalLayoutWidget_3)
        self.p4.setObjectName(u"p4")

        self.horizontalLayout_26.addWidget(self.p4)

        self.p5 = QPushButton(self.verticalLayoutWidget_3)
        self.p5.setObjectName(u"p5")

        self.horizontalLayout_26.addWidget(self.p5)

        self.p6 = QPushButton(self.verticalLayoutWidget_3)
        self.p6.setObjectName(u"p6")

        self.horizontalLayout_26.addWidget(self.p6)

        self.pMin = QPushButton(self.verticalLayoutWidget_3)
        self.pMin.setObjectName(u"pMin")

        self.horizontalLayout_26.addWidget(self.pMin)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.p1 = QPushButton(self.verticalLayoutWidget_3)
        self.p1.setObjectName(u"p1")

        self.horizontalLayout_25.addWidget(self.p1)

        self.p2 = QPushButton(self.verticalLayoutWidget_3)
        self.p2.setObjectName(u"p2")

        self.horizontalLayout_25.addWidget(self.p2)

        self.p3 = QPushButton(self.verticalLayoutWidget_3)
        self.p3.setObjectName(u"p3")

        self.horizontalLayout_25.addWidget(self.p3)

        self.pPos = QPushButton(self.verticalLayoutWidget_3)
        self.pPos.setObjectName(u"pPos")

        self.horizontalLayout_25.addWidget(self.pPos)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pdot = QPushButton(self.verticalLayoutWidget_3)
        self.pdot.setObjectName(u"pdot")

        self.horizontalLayout_28.addWidget(self.pdot)

        self.p0 = QPushButton(self.verticalLayoutWidget_3)
        self.p0.setObjectName(u"p0")

        self.horizontalLayout_28.addWidget(self.p0)

        self.pDel = QPushButton(self.verticalLayoutWidget_3)
        self.pDel.setObjectName(u"pDel")

        self.horizontalLayout_28.addWidget(self.pDel)

        self.pequals = QPushButton(self.verticalLayoutWidget_3)
        self.pequals.setObjectName(u"pequals")

        self.horizontalLayout_28.addWidget(self.pequals)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.horizontalLayoutWidget = QWidget(RestoranTakip)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 241, 201))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_sip = QLabel(self.horizontalLayoutWidget)
        self.label_sip.setObjectName(u"label_sip")

        self.verticalLayout.addWidget(self.label_sip)

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
        self.lin_sip = QLineEdit(self.horizontalLayoutWidget)
        self.lin_sip.setObjectName(u"lin_sip")

        self.verticalLayout_3.addWidget(self.lin_sip)

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

        self.horizontalLayoutWidget_2 = QWidget(RestoranTakip)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(340, 30, 261, 201))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_fiy = QLabel(self.horizontalLayoutWidget_2)
        self.label_fiy.setObjectName(u"label_fiy")

        self.verticalLayout_2.addWidget(self.label_fiy)

        self.label_ser = QLabel(self.horizontalLayoutWidget_2)
        self.label_ser.setObjectName(u"label_ser")

        self.verticalLayout_2.addWidget(self.label_ser)

        self.label_kdv = QLabel(self.horizontalLayoutWidget_2)
        self.label_kdv.setObjectName(u"label_kdv")

        self.verticalLayout_2.addWidget(self.label_kdv)

        self.label_alt = QLabel(self.horizontalLayoutWidget_2)
        self.label_alt.setObjectName(u"label_alt")

        self.verticalLayout_2.addWidget(self.label_alt)

        self.label_top = QLabel(self.horizontalLayoutWidget_2)
        self.label_top.setObjectName(u"label_top")

        self.verticalLayout_2.addWidget(self.label_top)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lin_fiy = QLineEdit(self.horizontalLayoutWidget_2)
        self.lin_fiy.setObjectName(u"lin_fiy")

        self.verticalLayout_4.addWidget(self.lin_fiy)

        self.lin_ser = QLineEdit(self.horizontalLayoutWidget_2)
        self.lin_ser.setObjectName(u"lin_ser")

        self.verticalLayout_4.addWidget(self.lin_ser)

        self.lin_kdv = QLineEdit(self.horizontalLayoutWidget_2)
        self.lin_kdv.setObjectName(u"lin_kdv")

        self.verticalLayout_4.addWidget(self.lin_kdv)

        self.lin_alt = QLineEdit(self.horizontalLayoutWidget_2)
        self.lin_alt.setObjectName(u"lin_alt")

        self.verticalLayout_4.addWidget(self.lin_alt)

        self.lin_top = QLineEdit(self.horizontalLayoutWidget_2)
        self.lin_top.setObjectName(u"lin_top")

        self.verticalLayout_4.addWidget(self.lin_top)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayoutWidget_3 = QWidget(RestoranTakip)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(320, 250, 340, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.push_fiyat = QPushButton(self.horizontalLayoutWidget_3)
        self.push_fiyat.setObjectName(u"push_fiyat")

        self.horizontalLayout_3.addWidget(self.push_fiyat)

        self.push_toplam = QPushButton(self.horizontalLayoutWidget_3)
        self.push_toplam.setObjectName(u"push_toplam")

        self.horizontalLayout_3.addWidget(self.push_toplam)

        self.push_sifirla = QPushButton(self.horizontalLayoutWidget_3)
        self.push_sifirla.setObjectName(u"push_sifirla")

        self.horizontalLayout_3.addWidget(self.push_sifirla)

        self.push_cikis = QPushButton(self.horizontalLayoutWidget_3)
        self.push_cikis.setObjectName(u"push_cikis")

        self.horizontalLayout_3.addWidget(self.push_cikis)

        self.line_3 = QFrame(RestoranTakip)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(320, 330, 341, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_4 = QWidget(RestoranTakip)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(270, 60, 51, 171))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.eksi = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi.setObjectName(u"eksi")

        self.verticalLayout_6.addWidget(self.eksi)

        self.eksi_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi_2.setObjectName(u"eksi_2")

        self.verticalLayout_6.addWidget(self.eksi_2)

        self.eksi_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi_3.setObjectName(u"eksi_3")

        self.verticalLayout_6.addWidget(self.eksi_3)

        self.eksi_4 = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi_4.setObjectName(u"eksi_4")

        self.verticalLayout_6.addWidget(self.eksi_4)

        self.eksi_5 = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi_5.setObjectName(u"eksi_5")

        self.verticalLayout_6.addWidget(self.eksi_5)

        self.eksi_6 = QPushButton(self.horizontalLayoutWidget_4)
        self.eksi_6.setObjectName(u"eksi_6")

        self.verticalLayout_6.addWidget(self.eksi_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.arti = QPushButton(self.horizontalLayoutWidget_4)
        self.arti.setObjectName(u"arti")

        self.verticalLayout_5.addWidget(self.arti)

        self.arti_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.arti_2.setObjectName(u"arti_2")

        self.verticalLayout_5.addWidget(self.arti_2)

        self.arti_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.arti_3.setObjectName(u"arti_3")

        self.verticalLayout_5.addWidget(self.arti_3)

        self.arti_4 = QPushButton(self.horizontalLayoutWidget_4)
        self.arti_4.setObjectName(u"arti_4")

        self.verticalLayout_5.addWidget(self.arti_4)

        self.arti_5 = QPushButton(self.horizontalLayoutWidget_4)
        self.arti_5.setObjectName(u"arti_5")

        self.verticalLayout_5.addWidget(self.arti_5)

        self.arti_6 = QPushButton(self.horizontalLayoutWidget_4)
        self.arti_6.setObjectName(u"arti_6")

        self.verticalLayout_5.addWidget(self.arti_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.retranslateUi(RestoranTakip)

        QMetaObject.connectSlotsByName(RestoranTakip)
    # setupUi

    def retranslateUi(self, RestoranTakip):
        RestoranTakip.setWindowTitle(QCoreApplication.translate("RestoranTakip", u"RestoranTakip", None))
        self.sonuc.setText("")
        self.pMod.setText(QCoreApplication.translate("RestoranTakip", u"%", None))
        self.pWipe.setText(QCoreApplication.translate("RestoranTakip", u"Temizle", None))
        self.pPN.setText(QCoreApplication.translate("RestoranTakip", u"+/-", None))
        self.p1divX.setText(QCoreApplication.translate("RestoranTakip", u"1/X", None))
        self.pxSq.setText(QCoreApplication.translate("RestoranTakip", u"X^2", None))
        self.pRootSq.setText(QCoreApplication.translate("RestoranTakip", u"2|x", None))
        self.pdiv.setText(QCoreApplication.translate("RestoranTakip", u"/", None))
        self.p7.setText(QCoreApplication.translate("RestoranTakip", u"7", None))
        self.p8.setText(QCoreApplication.translate("RestoranTakip", u"8", None))
        self.p9.setText(QCoreApplication.translate("RestoranTakip", u"9", None))
        self.pX.setText(QCoreApplication.translate("RestoranTakip", u"X", None))
        self.p4.setText(QCoreApplication.translate("RestoranTakip", u"4", None))
        self.p5.setText(QCoreApplication.translate("RestoranTakip", u"5", None))
        self.p6.setText(QCoreApplication.translate("RestoranTakip", u"6", None))
        self.pMin.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.p1.setText(QCoreApplication.translate("RestoranTakip", u"1", None))
        self.p2.setText(QCoreApplication.translate("RestoranTakip", u"2", None))
        self.p3.setText(QCoreApplication.translate("RestoranTakip", u"3", None))
        self.pPos.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.pdot.setText(QCoreApplication.translate("RestoranTakip", u".", None))
        self.p0.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.pDel.setText(QCoreApplication.translate("RestoranTakip", u"DEL", None))
        self.pequals.setText(QCoreApplication.translate("RestoranTakip", u"=", None))
        self.label_sip.setText(QCoreApplication.translate("RestoranTakip", u"Sipari\u015f No", None))
        self.label_kiz.setText(QCoreApplication.translate("RestoranTakip", u"K\u0131zartma", None))
        self.label_ogl.setText(QCoreApplication.translate("RestoranTakip", u"\u00d6\u011fle Yeme\u011fi", None))
        self.label_bur.setText(QCoreApplication.translate("RestoranTakip", u"Burger", None))
        self.label_piz.setText(QCoreApplication.translate("RestoranTakip", u"Pizza", None))
        self.label_che.setText(QCoreApplication.translate("RestoranTakip", u"Cheese Burger", None))
        self.label_ice.setText(QCoreApplication.translate("RestoranTakip", u"\u0130\u00e7ecekler", None))
        self.lin_kiz.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.lin_ogl.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.lin_bur.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.lin_piz.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.lin_che.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.lin_ice.setText(QCoreApplication.translate("RestoranTakip", u"0", None))
        self.label_fiy.setText(QCoreApplication.translate("RestoranTakip", u"Fiyat", None))
        self.label_ser.setText(QCoreApplication.translate("RestoranTakip", u"Servis Hizmeti", None))
        self.label_kdv.setText(QCoreApplication.translate("RestoranTakip", u"%18 KDV", None))
        self.label_alt.setText(QCoreApplication.translate("RestoranTakip", u"Alt Toplam", None))
        self.label_top.setText(QCoreApplication.translate("RestoranTakip", u"Toplam", None))
        self.push_fiyat.setText(QCoreApplication.translate("RestoranTakip", u"Fiyatlar", None))
        self.push_toplam.setText(QCoreApplication.translate("RestoranTakip", u"Toplam", None))
        self.push_sifirla.setText(QCoreApplication.translate("RestoranTakip", u"S\u0131f\u0131rla", None))
        self.push_cikis.setText(QCoreApplication.translate("RestoranTakip", u"\u00c7\u0131k\u0131\u015f", None))
        self.eksi.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.eksi_2.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.eksi_3.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.eksi_4.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.eksi_5.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.eksi_6.setText(QCoreApplication.translate("RestoranTakip", u"-", None))
        self.arti.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.arti_2.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.arti_3.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.arti_4.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.arti_5.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
        self.arti_6.setText(QCoreApplication.translate("RestoranTakip", u"+", None))
    # retranslateUi

