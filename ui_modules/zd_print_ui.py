# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/lukas/PycharmProjects/zd_inventory/ui/zd_print.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_print(object):
    def setupUi(self, dlg_print):
        dlg_print.setObjectName("dlg_print")
        dlg_print.resize(578, 129)
        self.widget = QtWidgets.QWidget(dlg_print)
        self.widget.setGeometry(QtCore.QRect(10, 20, 561, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_template = QtWidgets.QLabel(self.widget)
        self.lbl_template.setObjectName("lbl_template")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_template)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.led_template = QtWidgets.QLineEdit(self.widget)
        self.led_template.setObjectName("led_template")
        self.horizontalLayout_4.addWidget(self.led_template)
        self.btn_template = QtWidgets.QToolButton(self.widget)
        self.btn_template.setObjectName("btn_template")
        self.horizontalLayout_4.addWidget(self.btn_template)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.lbl_agreement = QtWidgets.QLabel(self.widget)
        self.lbl_agreement.setObjectName("lbl_agreement")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_agreement)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.led_agreement = QtWidgets.QLineEdit(self.widget)
        self.led_agreement.setObjectName("led_agreement")
        self.horizontalLayout_3.addWidget(self.led_agreement)
        self.btn_agreement = QtWidgets.QToolButton(self.widget)
        self.btn_agreement.setObjectName("btn_agreement")
        self.horizontalLayout_3.addWidget(self.btn_agreement)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(self.widget)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dlg_print)
        QtCore.QMetaObject.connectSlotsByName(dlg_print)

    def retranslateUi(self, dlg_print):
        _translate = QtCore.QCoreApplication.translate
        dlg_print.setWindowTitle(_translate("dlg_print", "Dialog"))
        self.lbl_template.setText(_translate("dlg_print", "Szablon"))
        self.btn_template.setText(_translate("dlg_print", "..."))
        self.lbl_agreement.setText(_translate("dlg_print", "Umowa"))
        self.btn_agreement.setText(_translate("dlg_print", "..."))
        self.btn_save.setText(_translate("dlg_print", "Zapisz"))
        self.btn_cancel.setText(_translate("dlg_print", "Anuluj"))
