# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagesetup.ui'
#
# Created: Tue Sep 29 09:32:49 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 353)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.firstTemplate = QtGui.QComboBox(Form)
        self.firstTemplate.setObjectName("firstTemplate")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstTemplate)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.size = QtGui.QComboBox(Form)
        self.size.setObjectName("size")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.size)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.height = QtGui.QLineEdit(Form)
        self.height.setObjectName("height")
        self.horizontalLayout_3.addWidget(self.height)
        self.height_unit_2 = QtGui.QComboBox(Form)
        self.height_unit_2.setObjectName("height_unit_2")
        self.horizontalLayout_3.addWidget(self.height_unit_2)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.width = QtGui.QLineEdit(Form)
        self.width.setObjectName("width")
        self.horizontalLayout_4.addWidget(self.width)
        self.width_unit_2 = QtGui.QComboBox(Form)
        self.width_unit_2.setObjectName("width_unit_2")
        self.horizontalLayout_4.addWidget(self.width_unit_2)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.margin_top = QtGui.QLineEdit(Form)
        self.margin_top.setObjectName("margin_top")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.margin_top)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.margin_bottom = QtGui.QLineEdit(Form)
        self.margin_bottom.setObjectName("margin_bottom")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.margin_bottom)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.margin_left = QtGui.QLineEdit(Form)
        self.margin_left.setObjectName("margin_left")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.margin_left)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.margin_right = QtGui.QLineEdit(Form)
        self.margin_right.setObjectName("margin_right")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.margin_right)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.spacing_header = QtGui.QLineEdit(Form)
        self.spacing_header.setObjectName("spacing_header")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.spacing_header)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spacing_footer = QtGui.QLineEdit(Form)
        self.spacing_footer.setObjectName("spacing_footer")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.spacing_footer)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.margin_gutter = QtGui.QLineEdit(Form)
        self.margin_gutter.setObjectName("margin_gutter")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.margin_gutter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "First Page Template:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Page Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Top Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Bottom Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Left Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Right Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Header Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Footer Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Gutter Margin:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
