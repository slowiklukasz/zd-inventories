# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/lukas/PycharmProjects/zd_inventory/ui/zd_inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_inventory(object):
    def setupUi(self, dlg_inventory):
        dlg_inventory.setObjectName("dlg_inventory")
        dlg_inventory.resize(484, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlg_inventory.sizePolicy().hasHeightForWidth())
        dlg_inventory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        dlg_inventory.setFont(font)
        dlg_inventory.setModal(False)
        self.layoutWidget = QtWidgets.QWidget(dlg_inventory)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 715))
        self.layoutWidget.setObjectName("layoutWidget")
        self.lyt_main = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.lyt_main.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.lyt_main.setContentsMargins(10, 20, 10, 10)
        self.lyt_main.setSpacing(15)
        self.lyt_main.setObjectName("lyt_main")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.lbl_id = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_id.setFont(font)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.led_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.led_id.setEnabled(False)
        self.led_id.setObjectName("led_id")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.led_id)
        self.lbl_contractor = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_contractor.setFont(font)
        self.lbl_contractor.setObjectName("lbl_contractor")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_contractor)
        self.cmb_contractors = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_contractors.setObjectName("cmb_contractors")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmb_contractors)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.led_phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.led_phone.setEnabled(False)
        self.led_phone.setObjectName("led_phone")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.led_phone)
        self.led_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.led_email.setEnabled(False)
        self.led_email.setObjectName("led_email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.led_email)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lbl_hamm = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_hamm.setFont(font)
        self.lbl_hamm.setObjectName("lbl_hamm")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_hamm)
        self.cmb_hammers = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_hammers.setObjectName("cmb_hammers")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.setItemText(0, "brak")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.cmb_hammers.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cmb_hammers)
        self.lbl_container = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_container.setFont(font)
        self.lbl_container.setObjectName("lbl_container")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lbl_container)
        self.cmb_containers = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_containers.setObjectName("cmb_containers")
        self.cmb_containers.addItem("")
        self.cmb_containers.setItemText(0, "brak")
        self.cmb_containers.addItem("")
        self.cmb_containers.addItem("")
        self.cmb_containers.addItem("")
        self.cmb_containers.addItem("")
        self.cmb_containers.addItem("")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cmb_containers)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.lbl_error = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lbl_error)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.led_from = QtWidgets.QLineEdit(self.layoutWidget)
        self.led_from.setEnabled(True)
        self.led_from.setObjectName("led_from")
        self.horizontalLayout_4.addWidget(self.led_from)
        self.led_to = QtWidgets.QLineEdit(self.layoutWidget)
        self.led_to.setEnabled(True)
        self.led_to.setObjectName("led_to")
        self.horizontalLayout_4.addWidget(self.led_to)
        self.btn_add_tag = QtWidgets.QToolButton(self.layoutWidget)
        self.btn_add_tag.setEnabled(False)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.horizontalLayout_4.addWidget(self.btn_add_tag)
        self.formLayout.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lsv_tags = QtWidgets.QListView(self.layoutWidget)
        self.lsv_tags.setEnabled(True)
        self.lsv_tags.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lsv_tags.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lsv_tags.setObjectName("lsv_tags")
        self.verticalLayout.addWidget(self.lsv_tags)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_mod_tag = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_mod_tag.setAutoDefault(False)
        self.btn_mod_tag.setObjectName("btn_mod_tag")
        self.horizontalLayout_2.addWidget(self.btn_mod_tag)
        self.btn_del_tag = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_del_tag.setAutoDefault(False)
        self.btn_del_tag.setObjectName("btn_del_tag")
        self.horizontalLayout_2.addWidget(self.btn_del_tag)
        self.btn_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(15, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.lbl_date_from = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_date_from.setFont(font)
        self.lbl_date_from.setObjectName("lbl_date_from")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.lbl_date_from)
        self.dte_date_from = QtWidgets.QDateEdit(self.layoutWidget)
        self.dte_date_from.setObjectName("dte_date_from")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.dte_date_from)
        self.lbl_date_to = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_date_to.setFont(font)
        self.lbl_date_to.setObjectName("lbl_date_to")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.lbl_date_to)
        self.dte_date_to = QtWidgets.QDateEdit(self.layoutWidget)
        self.dte_date_to.setObjectName("dte_date_to")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.dte_date_to)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(20, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.lbl_note = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_note.setFont(font)
        self.lbl_note.setObjectName("lbl_note")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.lbl_note)
        self.ted_note = QtWidgets.QTextEdit(self.layoutWidget)
        self.ted_note.setObjectName("ted_note")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.ted_note)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.line_3)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.line_4)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.line_5)
        self.led_contract = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_contract.sizePolicy().hasHeightForWidth())
        self.led_contract.setSizePolicy(sizePolicy)
        self.led_contract.setPlaceholderText("")
        self.led_contract.setObjectName("led_contract")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.led_contract)
        self.lbl_contract = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_contract.setFont(font)
        self.lbl_contract.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_contract.setObjectName("lbl_contract")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_contract)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line)
        self.lyt_main.addLayout(self.formLayout)
        self.lyt_btn = QtWidgets.QHBoxLayout()
        self.lyt_btn.setObjectName("lyt_btn")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lyt_btn.addItem(spacerItem4)
        self.btn_modify = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_modify.setFont(font)
        self.btn_modify.setAutoDefault(False)
        self.btn_modify.setObjectName("btn_modify")
        self.lyt_btn.addWidget(self.btn_modify)
        self.btn_add = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setAutoDefault(False)
        self.btn_add.setObjectName("btn_add")
        self.lyt_btn.addWidget(self.btn_add)
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.lyt_btn.addWidget(self.btn_cancel)
        self.btn_return = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_return.setFont(font)
        self.btn_return.setAutoDefault(False)
        self.btn_return.setObjectName("btn_return")
        self.lyt_btn.addWidget(self.btn_return)
        self.lyt_main.addLayout(self.lyt_btn)

        self.retranslateUi(dlg_inventory)
        QtCore.QMetaObject.connectSlotsByName(dlg_inventory)

    def retranslateUi(self, dlg_inventory):
        _translate = QtCore.QCoreApplication.translate
        dlg_inventory.setWindowTitle(_translate("dlg_inventory", "Dialog"))
        self.lbl_id.setText(_translate("dlg_inventory", "Id"))
        self.lbl_contractor.setText(_translate("dlg_inventory", "U??ytkownik"))
        self.label_3.setText(_translate("dlg_inventory", "Telefon"))
        self.label_2.setText(_translate("dlg_inventory", "Email"))
        self.lbl_hamm.setText(_translate("dlg_inventory", "M??otek"))
        self.cmb_hammers.setItemText(1, _translate("dlg_inventory", "1"))
        self.cmb_hammers.setItemText(2, _translate("dlg_inventory", "2"))
        self.cmb_hammers.setItemText(3, _translate("dlg_inventory", "3"))
        self.cmb_hammers.setItemText(4, _translate("dlg_inventory", "4"))
        self.cmb_hammers.setItemText(5, _translate("dlg_inventory", "5"))
        self.cmb_hammers.setItemText(6, _translate("dlg_inventory", "6"))
        self.cmb_hammers.setItemText(7, _translate("dlg_inventory", "7"))
        self.cmb_hammers.setItemText(8, _translate("dlg_inventory", "8"))
        self.cmb_hammers.setItemText(9, _translate("dlg_inventory", "9"))
        self.lbl_container.setText(_translate("dlg_inventory", "Pojemnik"))
        self.cmb_containers.setItemText(1, _translate("dlg_inventory", "1"))
        self.cmb_containers.setItemText(2, _translate("dlg_inventory", "2"))
        self.cmb_containers.setItemText(3, _translate("dlg_inventory", "3"))
        self.cmb_containers.setItemText(4, _translate("dlg_inventory", "4"))
        self.cmb_containers.setItemText(5, _translate("dlg_inventory", "5"))
        self.label.setText(_translate("dlg_inventory", "Arbotagi"))
        self.led_from.setPlaceholderText(_translate("dlg_inventory", "Numery od"))
        self.led_to.setPlaceholderText(_translate("dlg_inventory", "Numery do"))
        self.btn_add_tag.setText(_translate("dlg_inventory", "+"))
        self.btn_mod_tag.setText(_translate("dlg_inventory", "Edytuj"))
        self.btn_del_tag.setText(_translate("dlg_inventory", "Usu??"))
        self.btn_clear.setText(_translate("dlg_inventory", "Wyczy????"))
        self.lbl_date_from.setText(_translate("dlg_inventory", "Data od"))
        self.lbl_date_to.setText(_translate("dlg_inventory", "Data do"))
        self.lbl_note.setText(_translate("dlg_inventory", "Dodatkowe\n"
"informacje"))
        self.lbl_contract.setText(_translate("dlg_inventory", "Umowa"))
        self.btn_modify.setText(_translate("dlg_inventory", "Zapisz"))
        self.btn_add.setText(_translate("dlg_inventory", "Dodaj"))
        self.btn_cancel.setText(_translate("dlg_inventory", "Anuluj"))
        self.btn_return.setText(_translate("dlg_inventory", "Przywr????"))
