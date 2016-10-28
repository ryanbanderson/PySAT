
from PyQt4 import QtCore, QtGui
from pysat_function import pysat_func

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


class regression_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()

    def regression_train(self, MainWindow):
        self.regression_train = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression_train.setFont(font)
        self.regression_train.setObjectName(_fromUtf8("regression_train"))
        self.regression_vlayout = QtGui.QVBoxLayout(self.regression_train)
        self.regression_vlayout.setObjectName(_fromUtf8("regression_vlayout"))
        # choose data
        self.regression_choosedata_hlayout = QtGui.QHBoxLayout()
        self.regression_choosedata_hlayout.setObjectName(_fromUtf8("regression_choosedata_hlayout"))
        self.regression_train_choosedata_label = QtGui.QLabel(self.regression_train)
        self.regression_train_choosedata_label.setObjectName(_fromUtf8("regression_train_choosedata_label"))
        self.regression_train_choosedata_label.setText(_translate("regression_train", "Choose data:", None))
        self.regression_choosedata_hlayout.addWidget(self.regression_train_choosedata_label)
        datachoices = self.pysat_fun.datakeys
        if datachoices == []:
            datachoices = ['No data has been loaded!']
        self.regression_choosedata = make_combobox(datachoices)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName(_fromUtf8("regression_choosedata"))
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        # choose variables
        self.regression_choosevars_hlayout = QtGui.QHBoxLayout()
        self.regression_choosevars_hlayout.setObjectName(_fromUtf8("regression_choosevars_hlayout"))
        self.regression_train_choosex_label = QtGui.QLabel(self.regression_train)
        self.regression_train_choosex_label.setObjectName(_fromUtf8("regression_train_choosex_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex_label)

        xvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df.columns.levels[0].values
        self.regression_train_choosex = make_listwidget(xvarchoices)
        self.regression_train_choosex.setObjectName(_fromUtf8("regression_train_choosex"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosex)
        self.regression_train_choosey_label = QtGui.QLabel(self.regression_train)
        self.regression_train_choosey_label.setObjectName(_fromUtf8("regression_train_choosey_label"))
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey_label)

        yvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df['comp'].columns.values
        self.regression_train_choosey = make_listwidget(yvarchoices)
        self.regression_choosevars_hlayout.addWidget(self.regression_train_choosey)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.regression_choosevars_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosevars_hlayout)

        # ransac options
        self.ransac_hlayout = QtGui.QHBoxLayout()
        self.regression_ransac_checkbox = QtGui.QCheckBox(self.regression_train)
        self.regression_ransac_checkbox.setObjectName(_fromUtf8("regression_ransac_checkbox"))
        self.regression_ransac_checkbox.setText('RANSAC')
        self.ransac_hlayout.addWidget(self.regression_ransac_checkbox)
        self.regression_vlayout.addLayout(self.ransac_hlayout)

        self.regression_ransac_checkbox.stateChanged.connect(self.make_ransac_widget)
        # choose regression algorithm
        self.regression_choosealg_hlayout = QtGui.QHBoxLayout()
        self.regression_choosealg_hlayout.setObjectName(_fromUtf8("regression_choosealg_hlayout"))
        self.regression_choosealg_label = QtGui.QLabel(self.regression_train)
        self.regression_choosealg_label.setObjectName(_fromUtf8("regression_choosealg_label"))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_alg_choices = ['Choose an algorithm', 'PLS', 'GP', 'More to come...']
        self.regression_choosealg = make_combobox(self.regression_alg_choices)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName(_fromUtf8("regression_choosealg"))
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        regression_choosealg_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                        QtGui.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(regression_choosealg_spacer)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.regression_choosealg.activated.connect(self.make_regression_widget)

        self.verticalLayout_8.addWidget(self.regression_train)
        self.regression_train.raise_()
        self.regression_train.setTitle(_translate("regression_train", "Regression - Train", None))

    def make_ransac_widget(self):
        try:
            self.ransac_widget.deleteLater()
        except:
            pass
        self.ransac_widget = QtGui.QWidget()
        if self.regression_ransac_checkbox.isChecked():
            ransac_widget_hlayout = QtGui.QHBoxLayout(self.ransac_widget)
            ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
            ransac_lossfunc_label = QtGui.QLabel(self.ransac_widget)
            ransac_lossfunc_label.setText('Loss function:')
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_label)
            ransac_lossfunc_combobox = QtGui.QComboBox(self.ransac_widget)
            ransac_lossfunc_combobox.addItem(_fromUtf8("Squared Error"))
            ransac_lossfunc_combobox.addItem(_fromUtf8("Absolute Error"))
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_combobox)
            ransac_lossfunc_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                                       QtGui.QSizePolicy.Minimum)
            ransac_lossfunc_hlayout.addItem(ransac_lossfunc_spacer)
            ransac_widget_hlayout.addLayout(ransac_lossfunc_hlayout)
            ransac_thresh_hlayout = QtGui.QHBoxLayout()
            ransac_thresh_label = QtGui.QLabel(self.ransac_widget)
            ransac_thresh_label.setText('Threshold:')
            ransac_thresh_hlayout.addWidget(ransac_thresh_label)
            ransac_thresh_spin = QtGui.QDoubleSpinBox(self.ransac_widget)
            ransac_thresh_hlayout.addWidget(ransac_thresh_spin)
            ransac_thresh_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            ransac_thresh_hlayout.addItem(ransac_thresh_spacer)
            ransac_widget_hlayout.addLayout(ransac_thresh_hlayout)
            self.ransac_hlayout.addWidget(self.ransac_widget)

    def make_regression_widget(self):
        alg = self.regression_choosealg.currentText()
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtGui.QWidget()
        if alg == 'Choose an algorithm':
            pass
        if alg == 'PLS':
            pls_hlayout = QtGui.QHBoxLayout(self.reg_widget)
            pls_nc_label = QtGui.QLabel(self.reg_widget)
            pls_nc_label.setText('# of components:')
            pls_hlayout.addWidget(pls_nc_label)
            pls_nc_spinbox = QtGui.QSpinBox(self.reg_widget)
            pls_hlayout.addWidget(pls_nc_spinbox)
            pls_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            pls_hlayout.addItem(pls_spacer)

        if alg == 'GP':
            gp_vlayout = QtGui.QVBoxLayout(self.reg_widget)
            gp_dim_red_hlayout = QtGui.QHBoxLayout()
            gp_dim_red_label = QtGui.QLabel(self.reg_widget)
            gp_dim_red_label.setText('Choose dimensionality reduction method:')
            gp_dim_red_hlayout.addWidget(gp_dim_red_label)
            gp_dim_red_combobox = QtGui.QComboBox(self.reg_widget)
            gp_dim_red_combobox.addItem(_fromUtf8("PCA"))
            gp_dim_red_combobox.addItem(_fromUtf8("ICA"))
            gp_dim_red_hlayout.addWidget(gp_dim_red_combobox)
            gp_vlayout.addLayout(gp_dim_red_hlayout)
            gp_rand_starts_hlayout = QtGui.QHBoxLayout()
            gp_rand_starts_label = QtGui.QLabel(self.reg_widget)
            gp_rand_starts_label.setText('# of random starts:')
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_label)
            gp_rand_starts_spin = QtGui.QSpinBox(self.reg_widget)
            gp_rand_starts_spin.setValue(1)
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_spin)
            spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_rand_starts_hlayout.addItem(spacerItem4)
            gp_vlayout.addLayout(gp_rand_starts_hlayout)
            gp_theta_vlayout = QtGui.QVBoxLayout()
            gp_theta0_label = QtGui.QLabel(self.reg_widget)
            gp_theta0_label.setText('Starting Theta:')
            gp_theta_vlayout.addWidget(gp_theta0_label)
            gp_theta0_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_theta0_spin.setValue(1.0)
            gp_theta_vlayout.addWidget(gp_theta0_spin)
            gp_thetaL_label = QtGui.QLabel(self.reg_widget)
            gp_thetaL_label.setText('Lower bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaL_label)
            gp_thetaL_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaL_spin.setValue(0.1)
            gp_theta_vlayout.addWidget(gp_thetaL_spin)
            gp_thetaU_label = QtGui.QLabel(self.reg_widget)
            gp_thetaU_label.setText('Upper bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaU_label)
            gp_thetaU_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaU_spin.setMaximum(10000)
            gp_thetaU_spin.setValue(100.0)

            gp_theta_vlayout.addWidget(gp_thetaU_spin)
            spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_theta_vlayout.addItem(spacerItem5)
            gp_vlayout.addLayout(gp_theta_vlayout)

        self.regression_vlayout.addWidget(self.reg_widget)

def make_combobox(choices):
    combo = QtGui.QComboBox()

    for i, choice in enumerate(choices):
        combo.addItem(_fromUtf8(""))
        combo.setItemText(i, _translate('', choice, None))

    return combo

def make_listwidget(choices):
    listwidget = QtGui.QListWidget()
    listwidget.setItemDelegate
    for item in choices:
        item = QtGui.QListWidgetItem(item)
        listwidget.addItem(item)
    return listwidget
