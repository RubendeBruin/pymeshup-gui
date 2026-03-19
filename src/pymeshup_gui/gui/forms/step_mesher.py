# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step_mesher.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbSave = QPushButton(self.groupBox_3)
        self.pbSave.setObjectName(u"pbSave")

        self.verticalLayout.addWidget(self.pbSave)

        self.pbBatch = QPushButton(self.groupBox_3)
        self.pbBatch.setObjectName(u"pbBatch")

        self.verticalLayout.addWidget(self.pbBatch)


        self.gridLayout_2.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.view3d = QWidget(self.centralwidget)
        self.view3d.setObjectName(u"view3d")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view3d.sizePolicy().hasHeightForWidth())
        self.view3d.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.view3d, 0, 1, 6, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pbLoad = QPushButton(self.groupBox)
        self.pbLoad.setObjectName(u"pbLoad")

        self.gridLayout_4.addWidget(self.pbLoad, 3, 2, 1, 1)

        self.leScale = QLineEdit(self.groupBox)
        self.leScale.setObjectName(u"leScale")

        self.gridLayout_4.addWidget(self.leScale, 3, 1, 1, 1)

        self.lbMessage_2 = QLabel(self.groupBox)
        self.lbMessage_2.setObjectName(u"lbMessage_2")

        self.gridLayout_4.addWidget(self.lbMessage_2, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.lbInfo = QLabel(self.groupBox)
        self.lbInfo.setObjectName(u"lbInfo")

        self.gridLayout_4.addWidget(self.lbInfo, 7, 0, 1, 4)

        self.pbBrowse = QPushButton(self.groupBox)
        self.pbBrowse.setObjectName(u"pbBrowse")

        self.gridLayout_4.addWidget(self.pbBrowse, 2, 3, 1, 1)

        self.leFilename = QLineEdit(self.groupBox)
        self.leFilename.setObjectName(u"leFilename")

        self.gridLayout_4.addWidget(self.leFilename, 2, 0, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.lbFeedback = QLabel(self.centralwidget)
        self.lbFeedback.setObjectName(u"lbFeedback")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbFeedback.sizePolicy().hasHeightForWidth())
        self.lbFeedback.setSizePolicy(sizePolicy2)
        self.lbFeedback.setFrameShape(QFrame.Shape.Box)
        self.lbFeedback.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbFeedback, 5, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.dsLinTol = QDoubleSpinBox(self.groupBox_2)
        self.dsLinTol.setObjectName(u"dsLinTol")
        self.dsLinTol.setDecimals(3)
        self.dsLinTol.setMinimum(0.000000000000000)
        self.dsLinTol.setMaximum(10000.000000000000000)
        self.dsLinTol.setSingleStep(0.010000000000000)
        self.dsLinTol.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.dsLinTol, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.dsAngTol = QDoubleSpinBox(self.groupBox_2)
        self.dsAngTol.setObjectName(u"dsAngTol")
        self.dsAngTol.setDecimals(3)
        self.dsAngTol.setSingleStep(1.000000000000000)
        self.dsAngTol.setValue(5.000000000000000)

        self.gridLayout.addWidget(self.dsAngTol, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.chAutoApply = QCheckBox(self.groupBox_2)
        self.chAutoApply.setObjectName(u"chAutoApply")
        self.chAutoApply.setChecked(True)

        self.gridLayout.addWidget(self.chAutoApply, 2, 0, 1, 1)

        self.pbApply = QPushButton(self.groupBox_2)
        self.pbApply.setObjectName(u"pbApply")

        self.gridLayout.addWidget(self.pbApply, 2, 1, 1, 1)

        self.lbInfoMesh = QLabel(self.groupBox_2)
        self.lbInfoMesh.setObjectName(u"lbInfoMesh")

        self.gridLayout.addWidget(self.lbInfoMesh, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout_2.addWidget(self.groupBox_4, 4, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rbWireframe = QRadioButton(self.groupBox_5)
        self.rbWireframe.setObjectName(u"rbWireframe")
        self.rbWireframe.setChecked(True)

        self.verticalLayout_3.addWidget(self.rbWireframe)

        self.rbSolid = QRadioButton(self.groupBox_5)
        self.rbSolid.setObjectName(u"rbSolid")

        self.verticalLayout_3.addWidget(self.rbSolid)


        self.gridLayout_2.addWidget(self.groupBox_5, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1109, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.leFilename, self.pbBrowse)
        QWidget.setTabOrder(self.pbBrowse, self.leScale)
        QWidget.setTabOrder(self.leScale, self.pbLoad)
        QWidget.setTabOrder(self.pbLoad, self.dsLinTol)
        QWidget.setTabOrder(self.dsLinTol, self.dsAngTol)
        QWidget.setTabOrder(self.dsAngTol, self.chAutoApply)
        QWidget.setTabOrder(self.chAutoApply, self.pbApply)
        QWidget.setTabOrder(self.pbApply, self.pbSave)
        QWidget.setTabOrder(self.pbSave, self.pbBatch)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pbSave.setText(QCoreApplication.translate("MainWindow", u"Save this mesh as .stl", None))
        self.pbBatch.setText(QCoreApplication.translate("MainWindow", u"Batch process all STEP files in this folder using these settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pbLoad.setText(QCoreApplication.translate("MainWindow", u"(re)load", None))
        self.leScale.setText(QCoreApplication.translate("MainWindow", u".001", None))
        self.lbMessage_2.setText(QCoreApplication.translate("MainWindow", u"scale", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"step file", None))
        self.lbInfo.setText(QCoreApplication.translate("MainWindow", u"info", None))
        self.pbBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lbFeedback.setText(QCoreApplication.translate("MainWindow", u"Ready...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Meshing", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Linear tolerance", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"[m]", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Angular tolerance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"[deg]", None))
        self.chAutoApply.setText(QCoreApplication.translate("MainWindow", u"auto apply", None))
        self.pbApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.lbInfoMesh.setText(QCoreApplication.translate("MainWindow", u"info", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A: all, F, focus on selection<br/>Middle mouse to rotate<br/>Hold shift to pan</p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.rbWireframe.setText(QCoreApplication.translate("MainWindow", u"Wireframe", None))
        self.rbSolid.setText(QCoreApplication.translate("MainWindow", u"Solid", None))
    # retranslateUi

