# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ISAT_to_VOC_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(600, 251)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_save_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_save_root.setObjectName("pushButton_save_root")
        self.gridLayout.addWidget(self.pushButton_save_root, 3, 1, 1, 1)
        self.lineEdit_label_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_label_root.setEnabled(True)
        self.lineEdit_label_root.setReadOnly(True)
        self.lineEdit_label_root.setObjectName("lineEdit_label_root")
        self.gridLayout.addWidget(self.lineEdit_label_root, 2, 0, 1, 1)
        self.pushButton_label_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_label_root.setObjectName("pushButton_label_root")
        self.gridLayout.addWidget(self.pushButton_label_root, 2, 1, 1, 1)
        self.lineEdit_save_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_save_root.setEnabled(True)
        self.lineEdit_save_root.setReadOnly(True)
        self.lineEdit_save_root.setObjectName("lineEdit_save_root")
        self.gridLayout.addWidget(self.lineEdit_save_root, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox_is_instance = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_is_instance.setToolTip("")
        self.checkBox_is_instance.setAccessibleName("")
        self.checkBox_is_instance.setAccessibleDescription("")
        self.checkBox_is_instance.setObjectName("checkBox_is_instance")
        self.horizontalLayout_2.addWidget(self.checkBox_is_instance)
        self.checkBox_keep_crowd = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_keep_crowd.setObjectName("checkBox_keep_crowd")
        self.horizontalLayout_2.addWidget(self.checkBox_keep_crowd)
        self.verticalLayout.addWidget(self.widget_3)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/关闭_close-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/校验_check-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apply.setIcon(icon1)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ISAT to VOC png"))
        self.pushButton_save_root.setText(_translate("Dialog", "Save root"))
        self.lineEdit_label_root.setPlaceholderText(_translate("Dialog", "ISAT jsons root"))
        self.pushButton_label_root.setText(_translate("Dialog", "Label root"))
        self.lineEdit_save_root.setPlaceholderText(_translate("Dialog", "png save root"))
        self.checkBox_is_instance.setText(_translate("Dialog", "Is instance"))
        self.checkBox_keep_crowd.setText(_translate("Dialog", "Keep crowd"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Convert ISAT annotations to VOC png."))
        self.pushButton_cancel.setText(_translate("Dialog", "cancel"))
        self.pushButton_apply.setText(_translate("Dialog", "convert"))
import icons_rc
