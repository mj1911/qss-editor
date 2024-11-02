import os
from PyQt5 import QtGui, uic
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "../ui/fan.ui"))
class FanWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	w = FanWidget()
	w.show()
	sys.exit(app.exec_())

