import os
from PyQt5 import QtWidgets, uic	# adapted to Qt5
from functools import partial
#from PySide2.QtUiTools import loadUiType	# next test
#from PySide6.QtUiTools import loadUiType	# next test
#from PySide6 import QtWidgets, QtUiTools
from PySide6 import QtUiTools

current_dir = os.path.dirname(os.path.abspath(__file__))
# the main.ui has the buttons and stackedWidget
Form, Base = uic.loadUiType(os.path.join(current_dir, "ui/main.ui"))

class MainWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		# try to intercept file open buttons
		self.openqssbutton.clicked.connect(self.openqss)
		self.openqssbutton.setDisabled(True)
		self.openuibutton.clicked.connect(self.openui)
		buttons = (self.homebutton, self.statusbutton, self.fanbutton, 
			self.energybutton)
		for i, button in enumerate(buttons):
			button.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))
	
	def openqss(self):
		print("Open QSS button pressed!")
		self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
            "", "", "Qt5 QSS File (*.qss)" )
	
	def openui(self):
		print("Open UI button pressed!")
		self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
            "", "", "Qt5 UI File (*.ui)" )
		# have valid file_name here
		pass
		# crashes here...
		#Form, Base = uic.loadUiType(self.file_name)
		#self.stackedWidget.addWidget(uic.loadUiType(self.file_name))
		#self.stackedWidget.addWidget(self.file_name)
		#self.stackedWidget.setCurrentIndex(4)

		# next test (apparently this won't work and isn't supported...)
#		generated_class, base_class = loadUiType(self.file_name)
#		# the values will be:
#		#  (<class '__main__.Ui_ThemeWidgetForm'>, <class 'PySide2.QtWidgets.QWidget'>)
#		widget = base_class()
#		#form = generated_class()
#		#form.setupUi(widget)
#		# form.a_widget_member.a_method_of_member()
#		widget.show()

		# next test
		self.window = QtUiTools.QUiLoader().load(self.file_name)
		self.window.show()


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("fusion")
	w = MainWidget()
	w.show()
	sys.exit(app.exec_())

#from: https://stackoverflow.com/questions/53899209/load-whole-ui-file-in-an-frame-widget-of-another-ui-file
#and: https://github.com/eyllanesc/stackoverflow/tree/master/questions/53899209

# Currently seeing how gui.py can be changed to:
# A) use a main.ui instead of the hard-coded entries in the file,
# B) open a .ui file into a frame or stackedWidget instead of the boilerplate
