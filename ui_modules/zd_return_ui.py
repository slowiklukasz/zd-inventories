# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/lukas/PycharmProjects/zd_inventory/ui/zd_return.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_return(object):
    def setupUi(self, dlg_return):
        dlg_return.setObjectName("dlg_return")
        dlg_return.resize(429, 656)
        self.layoutWidget = QtWidgets.QWidget(dlg_return)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 641))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_equipment = QtWidgets.QFrame(self.layoutWidget)
        self.frame_equipment.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_equipment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_equipment.setObjectName("frame_equipment")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_equipment)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.chk_equipment = QtWidgets.QCheckBox(self.frame_equipment)
        self.chk_equipment.setChecked(True)
        self.chk_equipment.setObjectName("chk_equipment")
        self.verticalLayout_4.addWidget(self.chk_equipment)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, -1, 20, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cmb_container = QtWidgets.QComboBox(self.frame_equipment)
        self.cmb_container.setObjectName("cmb_container")
        self.cmb_container.addItem("")
        self.cmb_container.addItem("")
        self.gridLayout_2.addWidget(self.cmb_container, 1, 1, 1, 1)
        self.lbl_container = QtWidgets.QLabel(self.frame_equipment)
        self.lbl_container.setObjectName("lbl_container")
        self.gridLayout_2.addWidget(self.lbl_container, 1, 0, 1, 1)
        self.cmb_hammer = QtWidgets.QComboBox(self.frame_equipment)
        self.cmb_hammer.setObjectName("cmb_hammer")
        self.cmb_hammer.addItem("")
        self.cmb_hammer.addItem("")
        self.gridLayout_2.addWidget(self.cmb_hammer, 0, 1, 1, 1)
        self.lbl_hammer = QtWidgets.QLabel(self.frame_equipment)
        self.lbl_hammer.setObjectName("lbl_hammer")
        self.gridLayout_2.addWidget(self.lbl_hammer, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 7)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.frame_equipment)
        self.frame_tags = QtWidgets.QFrame(self.layoutWidget)
        self.frame_tags.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_tags.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tags.setObjectName("frame_tags")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tags)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.chk_tags = QtWidgets.QCheckBox(self.frame_tags)
        self.chk_tags.setEnabled(True)
        self.chk_tags.setChecked(False)
        self.chk_tags.setObjectName("chk_tags")
        self.verticalLayout_5.addWidget(self.chk_tags)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.led_from = QtWidgets.QLineEdit(self.frame_tags)
        self.led_from.setEnabled(False)
        self.led_from.setObjectName("led_from")
        self.horizontalLayout_4.addWidget(self.led_from)
        self.led_to = QtWidgets.QLineEdit(self.frame_tags)
        self.led_to.setEnabled(False)
        self.led_to.setObjectName("led_to")
        self.horizontalLayout_4.addWidget(self.led_to)
        self.btn_add_tag = QtWidgets.QPushButton(self.frame_tags)
        self.btn_add_tag.setEnabled(False)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.horizontalLayout_4.addWidget(self.btn_add_tag)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.lbl_error = QtWidgets.QLabel(self.frame_tags)
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        self.verticalLayout_5.addWidget(self.lbl_error)
        self.lbl_returned = QtWidgets.QLabel(self.frame_tags)
        self.lbl_returned.setEnabled(False)
        self.lbl_returned.setObjectName("lbl_returned")
        self.verticalLayout_5.addWidget(self.lbl_returned)
        self.lsv_returned = QtWidgets.QListView(self.frame_tags)
        self.lsv_returned.setEnabled(True)
        self.lsv_returned.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lsv_returned.setObjectName("lsv_returned")
        self.verticalLayout_5.addWidget(self.lsv_returned)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_mod_tag = QtWidgets.QPushButton(self.frame_tags)
        self.btn_mod_tag.setEnabled(False)
        self.btn_mod_tag.setAutoDefault(False)
        self.btn_mod_tag.setObjectName("btn_mod_tag")
        self.horizontalLayout_2.addWidget(self.btn_mod_tag)
        self.btn_del_tag = QtWidgets.QPushButton(self.frame_tags)
        self.btn_del_tag.setEnabled(False)
        self.btn_del_tag.setAutoDefault(False)
        self.btn_del_tag.setObjectName("btn_del_tag")
        self.horizontalLayout_2.addWidget(self.btn_del_tag)
        self.btn_clear = QtWidgets.QPushButton(self.frame_tags)
        self.btn_clear.setEnabled(False)
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_tags)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save.setAutoDefault(False)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cancel.setAutoDefault(True)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(dlg_return)
        QtCore.QMetaObject.connectSlotsByName(dlg_return)

    def retranslateUi(self, dlg_return):
        _translate = QtCore.QCoreApplication.translate
        dlg_return.setWindowTitle(_translate("dlg_return", "Dialog"))
        self.chk_equipment.setText(_translate("dlg_return", "ZWROT SPRZĘTU"))
        self.cmb_container.setItemText(0, _translate("dlg_return", "ZWROT"))
        self.cmb_container.setItemText(1, _translate("dlg_return", "ZNISZCZENIE/ZGUBIENIE"))
        self.lbl_container.setText(_translate("dlg_return", "Podajnik nr ..."))
        self.cmb_hammer.setItemText(0, _translate("dlg_return", "ZWROT"))
        self.cmb_hammer.setItemText(1, _translate("dlg_return", "ZNISZCZENIE/ZGUBIENIE"))
        self.lbl_hammer.setText(_translate("dlg_return", "Młot nr..."))
        self.chk_tags.setText(_translate("dlg_return", "ZWROT NUMERÓW"))
        self.led_from.setPlaceholderText(_translate("dlg_return", "Numery od"))
        self.led_to.setPlaceholderText(_translate("dlg_return", "Numery do"))
        self.btn_add_tag.setText(_translate("dlg_return", "Dodaj"))
        self.lbl_returned.setText(_translate("dlg_return", "Zwrócone numery:"))
        self.btn_mod_tag.setText(_translate("dlg_return", "Edytuj"))
        self.btn_del_tag.setText(_translate("dlg_return", "Usuń"))
        self.btn_clear.setText(_translate("dlg_return", "Wyczyść"))
        self.btn_save.setText(_translate("dlg_return", "Zapisz"))
        self.btn_cancel.setText(_translate("dlg_return", "Anuluj"))
