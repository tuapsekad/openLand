# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillareaupdate.ui'
#
# Created: Tue May 13 13:00:02 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fillAreaUpdate(object):
    def setupUi(self, fillAreaUpdate):
        fillAreaUpdate.setObjectName(_fromUtf8("fillAreaUpdate"))
        fillAreaUpdate.resize(393, 176)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fillAreaUpdate.sizePolicy().hasHeightForWidth())
        fillAreaUpdate.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/fillareaupdate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fillAreaUpdate.setWindowIcon(icon)
        fillAreaUpdate.setSizeGripEnabled(True)
        fillAreaUpdate.setModal(True)
        self.gridLayout = QtGui.QGridLayout(fillAreaUpdate)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(fillAreaUpdate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(fillAreaUpdate)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(fillAreaUpdate)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButtonCancel = QtGui.QPushButton(fillAreaUpdate)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon1)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.gridLayout.addWidget(self.pushButtonCancel, 3, 1, 1, 1)
        self.pushButtonOk = QtGui.QPushButton(fillAreaUpdate)
        self.pushButtonOk.setIcon(icon)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.gridLayout.addWidget(self.pushButtonOk, 3, 0, 1, 1)
        self.spinBoxRoundInaccuracy = QtGui.QSpinBox(fillAreaUpdate)
        self.spinBoxRoundInaccuracy.setObjectName(_fromUtf8("spinBoxRoundInaccuracy"))
        self.gridLayout.addWidget(self.spinBoxRoundInaccuracy, 2, 1, 1, 1)
        self.lineEditSelectedCount = QtGui.QLineEdit(fillAreaUpdate)
        self.lineEditSelectedCount.setReadOnly(True)
        self.lineEditSelectedCount.setObjectName(_fromUtf8("lineEditSelectedCount"))
        self.gridLayout.addWidget(self.lineEditSelectedCount, 0, 1, 1, 1)
        self.spinBoxRoundArea = QtGui.QSpinBox(fillAreaUpdate)
        self.spinBoxRoundArea.setProperty("value", 2)
        self.spinBoxRoundArea.setObjectName(_fromUtf8("spinBoxRoundArea"))
        self.gridLayout.addWidget(self.spinBoxRoundArea, 1, 1, 1, 1)

        self.retranslateUi(fillAreaUpdate)
        QtCore.QMetaObject.connectSlotsByName(fillAreaUpdate)
        fillAreaUpdate.setTabOrder(self.lineEditSelectedCount, self.spinBoxRoundArea)
        fillAreaUpdate.setTabOrder(self.spinBoxRoundArea, self.spinBoxRoundInaccuracy)
        fillAreaUpdate.setTabOrder(self.spinBoxRoundInaccuracy, self.pushButtonOk)
        fillAreaUpdate.setTabOrder(self.pushButtonOk, self.pushButtonCancel)

    def retranslateUi(self, fillAreaUpdate):
        fillAreaUpdate.setWindowTitle(_translate("fillAreaUpdate", "Расчёт уточненных площадей", None))
        self.label.setText(_translate("fillAreaUpdate", "<html><head/><body><p align=\"right\">Количество выбранных контуров</p></body></html>", None))
        self.label_3.setText(_translate("fillAreaUpdate", "<html><head/><body><p align=\"right\">Количество знаков после запятой<br/><span style=\" text-decoration: underline;\">для площади</span> отдельного контура</p></body></html>", None))
        self.label_2.setText(_translate("fillAreaUpdate", "<html><head/><body><p align=\"right\">Количество знаков после запятой<br/><span style=\" text-decoration: underline;\">для погрешности</span> вычисления площади<br/>отдельного контура</p></body></html>", None))
        self.pushButtonCancel.setText(_translate("fillAreaUpdate", "Закрыть", None))
        self.pushButtonOk.setText(_translate("fillAreaUpdate", "Расчитать уточненную площадь", None))

import resources_rc
