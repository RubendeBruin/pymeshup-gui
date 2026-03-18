from pathlib import Path
from random import random

import numpy as np
from PySide6.QtCore import QEvent, QObject
from PySide6.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QCheckBox, QMainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer


class _FileDropFilter(QObject):
    """Event filter that enables file drag-and-drop on a QLineEdit."""

    def __init__(self, line_edit):
        super().__init__(line_edit)
        self._le = line_edit
        self._le.setAcceptDrops(True)

    def eventFilter(self, obj, event):
        if obj is self._le:
            if event.type() == QEvent.Type.DragEnter:
                if event.mimeData().hasUrls():
                    event.acceptProposedAction()
                    return True
            elif event.type() == QEvent.Type.Drop:
                urls = event.mimeData().urls()
                if urls:
                    self._le.setText(urls[0].toLocalFile())
                    return True
        return super().eventFilter(obj, event)

from pymeshup import STEP
from pymeshup_gui.gui.forms.step_mesher import Ui_MainWindow
from pymeshup_gui.gui.helpers.vtkBlenderLikeInteractionStyle import BlenderStyle
from pymeshup_gui.gui.main import CreateVTKActor, CreateVTKLineActor


class StepMesherGui:
    def __init__(self):

        self.MainWindow = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.MainWindow.setToolTip("StepMesher - CadQuery + VTK")

        self.ui.pbBrowse.clicked.connect(self.browse)
        self.ui.pbLoad.clicked.connect(self.load_step_file)

        self.ui.leFilename.textChanged.connect(self.load_step_file)

        self.ui.dsAngTol.valueChanged.connect(self.changed)
        self.ui.dsLinTol.valueChanged.connect(self.changed)
        self.ui.pbApply.clicked.connect(self.update_mesh)

        self.ui.pbSave.clicked.connect(self.save_stl)

        self.ui.pbBatch.clicked.connect(self.process_all_files_in_folder)

        self._drop_filter = _FileDropFilter(self.ui.leFilename)
        self.ui.leFilename.installEventFilter(self._drop_filter)

        self.step_file : STEP | None = None

        self.MainWindow.show()

        self.setup_3d()

        self.iren.Initialize()
        self.style = BlenderStyle()
        self.iren.SetInteractorStyle(self.style)

        self.MainWindow.closeEvent = self.on_dialog_closed

        self.ui.leFilename.setText(r"Drop or enter your file here or press ...")



    def setup_3d(self):
        self.vtkWidget = QVTKRenderWindowInteractor()
        layout = QVBoxLayout()
        layout.addWidget(self.vtkWidget)
        self.ui.view3d.setLayout(layout)

        self.renderer = vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.renderer.SetBackground((254, 254, 254))
        self.create3Dorigin()

        # set camera orientation such that Z is up, X is right and Y is forward
        camera = self.renderer.GetActiveCamera()
        camera.SetViewUp(0, 0, 1)
        camera.SetPosition(20, -100, 20)
        camera.SetFocalPoint(0, 0, 0)
        self.renderer.ResetCamera()





    def browse(self):
        """Open the standard Qt file open dialog to choose a STEP file and
        set the chosen path into the output line edit.
        """
        # Use the standard Open dialog (not Save) as requested.
        filename, _ = QFileDialog.getOpenFileName(
            self.MainWindow,
            "Select STEP File",
            "",
            "STEP Files (*.step *.stp);;All Files (*)",
        )

        if not filename:
            return

        self.ui.leFilename.setText(filename)

    def load_step_file(self):
        filename = self.ui.leFilename.text()

        if Path(filename).exists():
            print(f"Loading STEP file: {filename}")

        else:
            self.ui.leFilename.setStyleSheet("color: red")
            return

        self.ui.leFilename.setStyleSheet("")

        scale = 1.0
        if self.ui.leScale.text():
            try:
                scale = float(self.ui.leScale.text())
            except:
                self.ui.lbFeedback.setText("Scale must be a number")
                return

        try:
            self.step_file = STEP(filename, scale = scale)
        except Exception as e:
            self.ui.lbFeedback.setText(str(e))
            return

        self.ui.lbFeedback.setText(f"Loaded: {filename}")

        # get the bounding box of the file with scale applied
        bbox = self.step_file._workplane.val().BoundingBox()
        info = f"Loaded; size = {bbox.xlen:.1f}m x {bbox.ylen:.1f}m x {bbox.zlen:.1f}m with center at {bbox.center.x:.2f},{bbox.center.z:.2f},{bbox.center.z:.2f}"
        self.ui.lbInfo.setText(info)

    def changed(self):
        if not self.ui.chAutoApply.isChecked():
            return

        self.update_mesh()

    def update_mesh(self, *args, filename : Path | None = None):

        lintol = self.ui.dsLinTol.value()
        angtol_deg = self.ui.dsAngTol.value()
        angtol = np.deg2rad(angtol_deg)

        try:
            mesh = self.step_file.to_volume(
                linear_tolerance=lintol,
                angular_tolerance=angtol,
                filename=filename,
            )

            self.ui.lbFeedback.setText(
                f"Generated mesh with {len(mesh.vertices)} vertices using lin.tol={lintol}, ang.tol={angtol}"
            )
            self.ui.lbFeedback.setStyleSheet("")
        except Exception as e:
            self.ui.lbFeedback.setText(str(e))
            self.ui.lbFeedback.setStyleSheet("color: red")
            return

        cm = mesh.ms.current_mesh()

        vertices = cm.vertex_matrix()
        faces = cm.face_matrix()
        actor = CreateVTKActor(vertices, faces)

        # use a random color
        red = random()
        green = random()
        blue = 0.5*random()


        actor.GetProperty().SetColor(red, green, blue)
        actor.GetProperty().SetRepresentationToWireframe()

        self.renderer.RemoveAllViewProps()

        self.renderer.AddActor(actor)
        self.renderer.Render()

        self.vtkWidget.update()

        nFaces = len(faces)
        self.ui.lbInfoMesh.setText(f"{nFaces} faces")

    def create3Dorigin(self):
        self.renderer.AddActor(CreateVTKLineActor((0, 0, 0), (10, 0, 0), (254, 0, 0)))
        self.renderer.AddActor(CreateVTKLineActor((0, 0, 0), (0, 10, 0), (0, 254, 0)))
        self.renderer.AddActor(CreateVTKLineActor((0, 0, 0), (0, 0, 10), (0, 0, 254)))

    def save_stl(self):
        file = Path(self.ui.leFilename.text())

        # output file is same as input only with .stl extension
        filename = file.with_suffix(".stl")

        self.update_mesh(filename = filename)
        self.ui.lbFeedback.setText("Saved as: " + str(filename))



    def process_all_files_in_folder(self):
        path = Path(self.ui.leFilename.text()).parent

        for file in path.glob("*.step"):
            self.ui.leFilename.setText(str(file))
            self.load_step_file()

            # output file is same as input only with .stl extension
            filename = file.with_suffix(".stl")

            self.update_mesh(filename = filename)
            self.ui.lbFeedback.setText("Saved as: " + str(filename))

            QApplication.instance().processEvents()



    def on_dialog_closed(self, event):
        pass
        # self.vtkWidget.GetRenderWindow().Finalize()



if __name__ == '__main__':
    app = QApplication([])
    window = StepMesherGui()
    window.MainWindow.show()

    app.exec()

