# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'address.ui'
#
# Created: Wed May 28 18:05:47 2014
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

class Ui_Address(object):
    def setupUi(self, Address):
        Address.setObjectName(_fromUtf8("Address"))
        Address.resize(500, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Address.setWindowIcon(icon)
        Address.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Address)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_17 = QtGui.QLabel(Address)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 14, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Address)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBoxGorodRayon = QtGui.QComboBox(Address)
        self.comboBoxGorodRayon.setEditable(True)
        self.comboBoxGorodRayon.setObjectName(_fromUtf8("comboBoxGorodRayon"))
        self.gridLayout_2.addWidget(self.comboBoxGorodRayon, 6, 2, 1, 1)
        self.label_6 = QtGui.QLabel(Address)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Address)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label = QtGui.QLabel(Address)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Address)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Address)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBoxRayon = QtGui.QComboBox(Address)
        self.comboBoxRayon.setEditable(True)
        self.comboBoxRayon.setObjectName(_fromUtf8("comboBoxRayon"))
        self.gridLayout_2.addWidget(self.comboBoxRayon, 4, 2, 1, 1)
        self.comboBoxRegion = QtGui.QComboBox(Address)
        self.comboBoxRegion.setObjectName(_fromUtf8("comboBoxRegion"))
        self.gridLayout_2.addWidget(self.comboBoxRegion, 0, 2, 1, 1)
        self.comboBoxTRayon = QtGui.QComboBox(Address)
        self.comboBoxTRayon.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTRayon.setObjectName(_fromUtf8("comboBoxTRayon"))
        self.gridLayout_2.addWidget(self.comboBoxTRayon, 4, 1, 1, 1)
        self.comboBoxMo = QtGui.QComboBox(Address)
        self.comboBoxMo.setEditable(True)
        self.comboBoxMo.setObjectName(_fromUtf8("comboBoxMo"))
        self.gridLayout_2.addWidget(self.comboBoxMo, 5, 2, 1, 1)
        self.comboBoxTGorodRayon = QtGui.QComboBox(Address)
        self.comboBoxTGorodRayon.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTGorodRayon.setObjectName(_fromUtf8("comboBoxTGorodRayon"))
        self.gridLayout_2.addWidget(self.comboBoxTGorodRayon, 6, 1, 1, 1)
        self.comboBoxTMo = QtGui.QComboBox(Address)
        self.comboBoxTMo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTMo.setObjectName(_fromUtf8("comboBoxTMo"))
        self.gridLayout_2.addWidget(self.comboBoxTMo, 5, 1, 1, 1)
        self.comboBoxTKorpus = QtGui.QComboBox(Address)
        self.comboBoxTKorpus.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTKorpus.setObjectName(_fromUtf8("comboBoxTKorpus"))
        self.gridLayout_2.addWidget(self.comboBoxTKorpus, 11, 1, 1, 1)
        self.comboBoxTStroenie = QtGui.QComboBox(Address)
        self.comboBoxTStroenie.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTStroenie.setObjectName(_fromUtf8("comboBoxTStroenie"))
        self.gridLayout_2.addWidget(self.comboBoxTStroenie, 12, 1, 1, 1)
        self.lineEditKLADR = QtGui.QLineEdit(Address)
        self.lineEditKLADR.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditKLADR.setReadOnly(True)
        self.lineEditKLADR.setObjectName(_fromUtf8("lineEditKLADR"))
        self.gridLayout_2.addWidget(self.lineEditKLADR, 1, 2, 1, 1)
        self.comboBoxSelsovet = QtGui.QComboBox(Address)
        self.comboBoxSelsovet.setEditable(True)
        self.comboBoxSelsovet.setObjectName(_fromUtf8("comboBoxSelsovet"))
        self.gridLayout_2.addWidget(self.comboBoxSelsovet, 7, 2, 1, 1)
        self.comboBoxTUlica = QtGui.QComboBox(Address)
        self.comboBoxTUlica.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTUlica.setObjectName(_fromUtf8("comboBoxTUlica"))
        self.gridLayout_2.addWidget(self.comboBoxTUlica, 9, 1, 1, 1)
        self.lineEditOKATO = QtGui.QLineEdit(Address)
        self.lineEditOKATO.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditOKATO.setInputMask(_fromUtf8(""))
        self.lineEditOKATO.setText(_fromUtf8(""))
        self.lineEditOKATO.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditOKATO.setReadOnly(True)
        self.lineEditOKATO.setPlaceholderText(_fromUtf8(""))
        self.lineEditOKATO.setObjectName(_fromUtf8("lineEditOKATO"))
        self.gridLayout_2.addWidget(self.lineEditOKATO, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Address)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.comboBoxTSelsovet = QtGui.QComboBox(Address)
        self.comboBoxTSelsovet.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTSelsovet.setObjectName(_fromUtf8("comboBoxTSelsovet"))
        self.gridLayout_2.addWidget(self.comboBoxTSelsovet, 7, 1, 1, 1)
        self.comboBoxTNaselenPunkt = QtGui.QComboBox(Address)
        self.comboBoxTNaselenPunkt.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTNaselenPunkt.setObjectName(_fromUtf8("comboBoxTNaselenPunkt"))
        self.gridLayout_2.addWidget(self.comboBoxTNaselenPunkt, 8, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Address)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_11 = QtGui.QLabel(Address)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 10, 0, 1, 1)
        self.pushButtonKladr = QtGui.QPushButton(Address)
        self.pushButtonKladr.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonKladr.setIcon(icon1)
        self.pushButtonKladr.setAutoDefault(False)
        self.pushButtonKladr.setObjectName(_fromUtf8("pushButtonKladr"))
        self.gridLayout_2.addWidget(self.pushButtonKladr, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Address)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEditIndeks = QtGui.QLineEdit(Address)
        self.lineEditIndeks.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditIndeks.setReadOnly(True)
        self.lineEditIndeks.setObjectName(_fromUtf8("lineEditIndeks"))
        self.gridLayout_2.addWidget(self.lineEditIndeks, 3, 2, 1, 1)
        self.comboBoxUlica = QtGui.QComboBox(Address)
        self.comboBoxUlica.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.comboBoxUlica.setEditable(True)
        self.comboBoxUlica.setObjectName(_fromUtf8("comboBoxUlica"))
        self.gridLayout_2.addWidget(self.comboBoxUlica, 9, 2, 1, 1)
        self.label_12 = QtGui.QLabel(Address)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 11, 0, 1, 1)
        self.comboBoxNaselenPunkt = QtGui.QComboBox(Address)
        self.comboBoxNaselenPunkt.setEditable(True)
        self.comboBoxNaselenPunkt.setObjectName(_fromUtf8("comboBoxNaselenPunkt"))
        self.gridLayout_2.addWidget(self.comboBoxNaselenPunkt, 8, 2, 1, 1)
        self.comboBoxDom = QtGui.QComboBox(Address)
        self.comboBoxDom.setEditable(True)
        self.comboBoxDom.setObjectName(_fromUtf8("comboBoxDom"))
        self.gridLayout_2.addWidget(self.comboBoxDom, 10, 2, 1, 1)
        self.comboBoxTDom = QtGui.QComboBox(Address)
        self.comboBoxTDom.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTDom.setObjectName(_fromUtf8("comboBoxTDom"))
        self.gridLayout_2.addWidget(self.comboBoxTDom, 10, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Address)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 9, 0, 1, 1)
        self.comboBoxKorpus = QtGui.QComboBox(Address)
        self.comboBoxKorpus.setEditable(True)
        self.comboBoxKorpus.setObjectName(_fromUtf8("comboBoxKorpus"))
        self.gridLayout_2.addWidget(self.comboBoxKorpus, 11, 2, 1, 1)
        self.label_13 = QtGui.QLabel(Address)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 12, 0, 1, 1)
        self.comboBoxStroenie = QtGui.QComboBox(Address)
        self.comboBoxStroenie.setEditable(True)
        self.comboBoxStroenie.setObjectName(_fromUtf8("comboBoxStroenie"))
        self.gridLayout_2.addWidget(self.comboBoxStroenie, 12, 2, 1, 1)
        self.label_14 = QtGui.QLabel(Address)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 13, 0, 1, 1)
        self.comboBoxTKvartira = QtGui.QComboBox(Address)
        self.comboBoxTKvartira.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBoxTKvartira.setObjectName(_fromUtf8("comboBoxTKvartira"))
        self.gridLayout_2.addWidget(self.comboBoxTKvartira, 13, 1, 1, 1)
        self.comboBoxKvartira = QtGui.QComboBox(Address)
        self.comboBoxKvartira.setEditable(True)
        self.comboBoxKvartira.setObjectName(_fromUtf8("comboBoxKvartira"))
        self.gridLayout_2.addWidget(self.comboBoxKvartira, 13, 2, 1, 1)
        self.comboBoxDocument = QtGui.QComboBox(Address)
        self.comboBoxDocument.setObjectName(_fromUtf8("comboBoxDocument"))
        self.gridLayout_2.addWidget(self.comboBoxDocument, 14, 2, 1, 1)
        self.pushButtonDocument = QtGui.QPushButton(Address)
        self.pushButtonDocument.setEnabled(True)
        self.pushButtonDocument.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/folders.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDocument.setIcon(icon2)
        self.pushButtonDocument.setObjectName(_fromUtf8("pushButtonDocument"))
        self.gridLayout_2.addWidget(self.pushButtonDocument, 14, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_15 = QtGui.QLabel(Address)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.textEditInoe = QtGui.QTextEdit(Address)
        self.textEditInoe.setObjectName(_fromUtf8("textEditInoe"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textEditInoe)
        self.label_16 = QtGui.QLabel(Address)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.textEditOpisanie = QtGui.QTextEdit(Address)
        self.textEditOpisanie.setObjectName(_fromUtf8("textEditOpisanie"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.textEditOpisanie)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonCreateDesc = QtGui.QPushButton(Address)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/format_indent_more.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCreateDesc.setIcon(icon3)
        self.pushButtonCreateDesc.setDefault(True)
        self.pushButtonCreateDesc.setObjectName(_fromUtf8("pushButtonCreateDesc"))
        self.horizontalLayout.addWidget(self.pushButtonCreateDesc)
        self.pushButtonRefresh = QtGui.QPushButton(Address)
        self.pushButtonRefresh.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon4)
        self.pushButtonRefresh.setAutoDefault(False)
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.horizontalLayout.addWidget(self.pushButtonRefresh)
        self.pushButtonOk = QtGui.QPushButton(Address)
        self.pushButtonOk.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOk.setIcon(icon5)
        self.pushButtonOk.setAutoDefault(False)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonClose = QtGui.QPushButton(Address)
        self.pushButtonClose.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon6)
        self.pushButtonClose.setAutoDefault(False)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Address)
        QtCore.QMetaObject.connectSlotsByName(Address)
        Address.setTabOrder(self.comboBoxRegion, self.pushButtonKladr)
        Address.setTabOrder(self.pushButtonKladr, self.lineEditKLADR)
        Address.setTabOrder(self.lineEditKLADR, self.lineEditOKATO)
        Address.setTabOrder(self.lineEditOKATO, self.lineEditIndeks)
        Address.setTabOrder(self.lineEditIndeks, self.comboBoxTRayon)
        Address.setTabOrder(self.comboBoxTRayon, self.comboBoxRayon)
        Address.setTabOrder(self.comboBoxRayon, self.comboBoxTMo)
        Address.setTabOrder(self.comboBoxTMo, self.comboBoxMo)
        Address.setTabOrder(self.comboBoxMo, self.comboBoxTGorodRayon)
        Address.setTabOrder(self.comboBoxTGorodRayon, self.comboBoxGorodRayon)
        Address.setTabOrder(self.comboBoxGorodRayon, self.comboBoxTSelsovet)
        Address.setTabOrder(self.comboBoxTSelsovet, self.comboBoxSelsovet)
        Address.setTabOrder(self.comboBoxSelsovet, self.comboBoxTNaselenPunkt)
        Address.setTabOrder(self.comboBoxTNaselenPunkt, self.comboBoxNaselenPunkt)
        Address.setTabOrder(self.comboBoxNaselenPunkt, self.comboBoxTUlica)
        Address.setTabOrder(self.comboBoxTUlica, self.comboBoxUlica)
        Address.setTabOrder(self.comboBoxUlica, self.comboBoxTDom)
        Address.setTabOrder(self.comboBoxTDom, self.comboBoxDom)
        Address.setTabOrder(self.comboBoxDom, self.comboBoxTKorpus)
        Address.setTabOrder(self.comboBoxTKorpus, self.comboBoxKorpus)
        Address.setTabOrder(self.comboBoxKorpus, self.comboBoxTStroenie)
        Address.setTabOrder(self.comboBoxTStroenie, self.comboBoxStroenie)
        Address.setTabOrder(self.comboBoxStroenie, self.comboBoxTKvartira)
        Address.setTabOrder(self.comboBoxTKvartira, self.comboBoxKvartira)
        Address.setTabOrder(self.comboBoxKvartira, self.pushButtonDocument)
        Address.setTabOrder(self.pushButtonDocument, self.comboBoxDocument)
        Address.setTabOrder(self.comboBoxDocument, self.textEditInoe)
        Address.setTabOrder(self.textEditInoe, self.textEditOpisanie)
        Address.setTabOrder(self.textEditOpisanie, self.pushButtonCreateDesc)
        Address.setTabOrder(self.pushButtonCreateDesc, self.pushButtonRefresh)
        Address.setTabOrder(self.pushButtonRefresh, self.pushButtonOk)
        Address.setTabOrder(self.pushButtonOk, self.pushButtonClose)

    def retranslateUi(self, Address):
        Address.setWindowTitle(_translate("Address", "Адрес или местоположение", None))
        self.label_17.setWhatsThis(_translate("Address", "<html><head/><body><p><br/></p></body></html>", None))
        self.label_17.setText(_translate("Address", "<html><head/><body><p align=\"right\">Документ</p></body></html>", None))
        self.label_4.setText(_translate("Address", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Регион</span></p></body></html>", None))
        self.label_6.setText(_translate("Address", "<html><head/><body><p align=\"right\">МО</p></body></html>", None))
        self.label_7.setText(_translate("Address", "<html><head/><body><p align=\"right\">Городской район</p></body></html>", None))
        self.label.setText(_translate("Address", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">ОКАТО</span></p></body></html>", None))
        self.label_2.setText(_translate("Address", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">КЛАДР</span></p></body></html>", None))
        self.label_5.setText(_translate("Address", "<html><head/><body><p align=\"right\">Район</p></body></html>", None))
        self.label_3.setText(_translate("Address", "<html><head/><body><p align=\"right\">Почтовый индекс</p></body></html>", None))
        self.label_8.setText(_translate("Address", "<html><head/><body><p align=\"right\">Сельсовет</p></body></html>", None))
        self.label_11.setText(_translate("Address", "<html><head/><body><p align=\"right\">Дом</p></body></html>", None))
        self.pushButtonKladr.setText(_translate("Address", "КЛАДР", None))
        self.label_9.setText(_translate("Address", "<html><head/><body><p align=\"right\">Населенный пункт</p></body></html>", None))
        self.label_12.setText(_translate("Address", "<html><head/><body><p align=\"right\">Корпус</p></body></html>", None))
        self.label_10.setText(_translate("Address", "<html><head/><body><p align=\"right\">Улица</p></body></html>", None))
        self.label_13.setText(_translate("Address", "<html><head/><body><p align=\"right\">Строение</p></body></html>", None))
        self.label_14.setText(_translate("Address", "<html><head/><body><p align=\"right\">Квартира</p></body></html>", None))
        self.comboBoxDocument.setWhatsThis(_translate("Address", "<html><head/><body><p>Реквизиты акта органа государственной власти или органа местного самоуправления, уполномоченного присваивать адреса земельным участкам</p></body></html>", None))
        self.pushButtonDocument.setWhatsThis(_translate("Address", "<html><head/><body><p>Кнопка вызова диалога редактирования справочника документов</p></body></html>", None))
        self.label_15.setText(_translate("Address", "<html><head/><body><p align=\"right\">Иное</p></body></html>", None))
        self.label_16.setText(_translate("Address", "<html><head/><body><p align=\"right\"><span style=\" font-weight:400;\">Описание</span></p></body></html>", None))
        self.pushButtonCreateDesc.setText(_translate("Address", "Сформировать", None))
        self.pushButtonRefresh.setText(_translate("Address", "Обновить", None))
        self.pushButtonOk.setText(_translate("Address", "OK", None))
        self.pushButtonClose.setText(_translate("Address", "Отмена", None))

import resources_rc
