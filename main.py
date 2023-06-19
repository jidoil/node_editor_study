import sys
from PySide2 import QtWidgets
from node_editor import NodeEditorWindow

app = QtWidgets.QApplication()
window = NodeEditorWindow()
window.show()

sys.exit(app.exec_())