# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qchainage.ui'
#
# Created: Thu Apr  3 12:13:02 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_QChainageDialog(object):
    def setupUi(self, QChainageDialog):
        QChainageDialog.setObjectName(_fromUtf8("QChainageDialog"))
        QChainageDialog.setEnabled(True)
        QChainageDialog.resize(395, 286)
        QChainageDialog.setMinimumSize(QtCore.QSize(380, 200))
        self.gridLayout = QtGui.QGridLayout(QChainageDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(QChainageDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 354, 96))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.labelSelectLayer = QtGui.QLabel(self.widget)
        self.labelSelectLayer.setObjectName(_fromUtf8("labelSelectLayer"))
        self.verticalLayout_5.addWidget(self.labelSelectLayer)
        self.labelDistance = QtGui.QLabel(self.widget)
        self.labelDistance.setObjectName(_fromUtf8("labelDistance"))
        self.verticalLayout_5.addWidget(self.labelDistance)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectLayerComboBox = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectLayerComboBox.sizePolicy().hasHeightForWidth())
        self.selectLayerComboBox.setSizePolicy(sizePolicy)
        self.selectLayerComboBox.setObjectName(_fromUtf8("selectLayerComboBox"))
        self.verticalLayout.addWidget(self.selectLayerComboBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.distanceSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.distanceSpinBox.setDecimals(6)
        self.distanceSpinBox.setMaximum(9999.999999)
        self.distanceSpinBox.setProperty("value", 1.0)
        self.distanceSpinBox.setObjectName(_fromUtf8("distanceSpinBox"))
        self.horizontalLayout_2.addWidget(self.distanceSpinBox)
        self.labelUnit = QtGui.QLabel(self.widget)
        self.labelUnit.setObjectName(_fromUtf8("labelUnit"))
        self.horizontalLayout_2.addWidget(self.labelUnit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelLayerName = QtGui.QLabel(self.widget)
        self.labelLayerName.setObjectName(_fromUtf8("labelLayerName"))
        self.horizontalLayout_4.addWidget(self.labelLayerName)
        self.layerNameLine = QtGui.QLineEdit(self.widget)
        self.layerNameLine.setObjectName(_fromUtf8("layerNameLine"))
        self.horizontalLayout_4.addWidget(self.layerNameLine)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.autoLabelCheckBox = QtGui.QCheckBox(self.tab)
        self.autoLabelCheckBox.setEnabled(True)
        self.autoLabelCheckBox.setGeometry(QtCore.QRect(10, 120, 549, 20))
        self.autoLabelCheckBox.setChecked(True)
        self.autoLabelCheckBox.setObjectName(_fromUtf8("autoLabelCheckBox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(21, 21, 57, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectOnlyRadioBtn = QtGui.QRadioButton(self.tab_2)
        self.selectOnlyRadioBtn.setEnabled(True)
        self.selectOnlyRadioBtn.setGeometry(QtCore.QRect(84, 47, 165, 20))
        self.selectOnlyRadioBtn.setCheckable(True)
        self.selectOnlyRadioBtn.setChecked(False)
        self.selectOnlyRadioBtn.setObjectName(_fromUtf8("selectOnlyRadioBtn"))
        self.selectAllRadioBtn = QtGui.QRadioButton(self.tab_2)
        self.selectAllRadioBtn.setEnabled(True)
        self.selectAllRadioBtn.setGeometry(QtCore.QRect(84, 21, 151, 20))
        self.selectAllRadioBtn.setCheckable(True)
        self.selectAllRadioBtn.setObjectName(_fromUtf8("selectAllRadioBtn"))
        self.startSpinBox = QtGui.QDoubleSpinBox(self.tab_2)
        self.startSpinBox.setEnabled(False)
        self.startSpinBox.setGeometry(QtCore.QRect(140, 80, 83, 26))
        self.startSpinBox.setDecimals(3)
        self.startSpinBox.setMaximum(9999.99)
        self.startSpinBox.setObjectName(_fromUtf8("startSpinBox"))
        self.checkBoxStartFrom = QtGui.QCheckBox(self.tab_2)
        self.checkBoxStartFrom.setGeometry(QtCore.QRect(43, 80, 91, 20))
        self.checkBoxStartFrom.setObjectName(_fromUtf8("checkBoxStartFrom"))
        self.endSpinBox = QtGui.QDoubleSpinBox(self.tab_2)
        self.endSpinBox.setEnabled(False)
        self.endSpinBox.setGeometry(QtCore.QRect(120, 120, 106, 26))
        self.endSpinBox.setDecimals(3)
        self.endSpinBox.setMaximum(9999.99)
        self.endSpinBox.setObjectName(_fromUtf8("endSpinBox"))
        self.checkBoxEndAt = QtGui.QCheckBox(self.tab_2)
        self.checkBoxEndAt.setGeometry(QtCore.QRect(46, 120, 68, 20))
        self.checkBoxEndAt.setObjectName(_fromUtf8("checkBoxEndAt"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QChainageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(QChainageDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QChainageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QChainageDialog.reject)
        QtCore.QObject.connect(self.checkBoxStartFrom, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.startSpinBox.setEnabled)
        QtCore.QObject.connect(self.checkBoxEndAt, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.endSpinBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(QChainageDialog)

    def retranslateUi(self, QChainageDialog):
        QChainageDialog.setWindowTitle(_translate("QChainageDialog", "Dialog", None))
        self.labelSelectLayer.setText(_translate("QChainageDialog", "Select Layer to chainage", None))
        self.labelDistance.setText(_translate("QChainageDialog", "Chainage every", None))
        self.labelUnit.setText(_translate("QChainageDialog", "Units", None))
        self.labelLayerName.setText(_translate("QChainageDialog", "Name of output Layer", None))
        self.autoLabelCheckBox.setText(_translate("QChainageDialog", "Automatically Label the Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QChainageDialog", "Basic", None))
        self.label.setText(_translate("QChainageDialog", "Chainage", None))
        self.selectOnlyRadioBtn.setText(_translate("QChainageDialog", "only selected Features", None))
        self.selectAllRadioBtn.setText(_translate("QChainageDialog", "all Features in Layer", None))
        self.checkBoxStartFrom.setText(_translate("QChainageDialog", "Start from", None))
        self.checkBoxEndAt.setText(_translate("QChainageDialog", "End at", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QChainageDialog", "Advanced", None))

