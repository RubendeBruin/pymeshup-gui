print("Starting STEP Mesher GUI...")

from PySide6.QtWidgets import QApplication
from pymeshup_gui.gui.stepmesher import StepMesherGui

app = QApplication([])
window = StepMesherGui()
window.MainWindow.show()

app.exec()

