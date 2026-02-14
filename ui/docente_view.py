# ui/docente_view.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import  (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget,
    QTextEdit, QLineEdit
)

class DocenteView(QWidget):
    guardarCalificacionRequested = pyqtSignal(str, str)
    publicarAvisoRequested = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Docente")
        self.resize(700, 450)

        # Layout principal directamente sobre self
        layout = QVBoxLayout(self)

        self.lbl_bienvenida = QLabel("Bienvenido docente")
        self.lbl_bienvenida.setAlignment(Qt.AlignCenter)
        self.lbl_bienvenida.setStyleSheet("font-size:18px; font-weight:bold;")

        self.lista_alumnos = QListWidget()
        self.lista_alumnos.addItems(["Eduardo", "Luis", "Ana"])

        # Fila para calificaciones
        fila_calif = QHBoxLayout()
        self.txt_alumno = QLineEdit()
        self.txt_alumno.setPlaceholderText("Alumno")
        self.txt_calificacion = QLineEdit()
        self.txt_calificacion.setPlaceholderText("Calificación")
        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self._emit_calificacion)
        fila_calif.addWidget(self.txt_alumno)
        fila_calif.addWidget(self.txt_calificacion)
        fila_calif.addWidget(self.btn_guardar)

        # Avisos
        self.txt_aviso = QTextEdit()
        self.btn_publicar = QPushButton("Publicar aviso")
        self.btn_publicar.clicked.connect(self._emit_aviso)

        # Agregar todo al layout principal
        layout.addWidget(self.lbl_bienvenida)
        layout.addWidget(QLabel("Lista de alumnos"))
        layout.addWidget(self.lista_alumnos)
        layout.addLayout(fila_calif)
        layout.addWidget(QLabel("Publicar aviso"))
        layout.addWidget(self.txt_aviso)
        layout.addWidget(self.btn_publicar)

    def _emit_calificacion(self):
        self.guardarCalificacionRequested.emit(
            self.txt_alumno.text(),
            self.txt_calificacion.text()
        )

    def _emit_aviso(self):
        self.publicarAvisoRequested.emit(self.txt_aviso.toPlainText())

    def set_welcome(self, user: str):
        self.lbl_bienvenida.setText(f"Bienvenido docente, {user}")