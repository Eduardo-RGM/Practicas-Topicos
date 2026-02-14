# ui/Estudiante_view.py
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget,
    QTextEdit, QTableWidget, QTableWidgetItem
)

class EstudianteView(QMainWindow):
    verTareasRequested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel Estudiante")
        self.resize(700, 450)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        
        self.lbl_bienvenida = QLabel("Bienvenido estudiante")
        self.lbl_bienvenida.setAlignment(Qt.AlignCenter)
        self.lbl_bienvenida.setStyleSheet("font-size:18px; font-weight:bold;")

        
        self.lista_materias = QListWidget()
        self.lista_materias.addItems(["Matemáticas", "Programación", "Base de Datos"])

       
        self.tabla_horario = QTableWidget(3, 4)
        self.tabla_horario.setHorizontalHeaderLabels(["Hora", "Materia", "Aula", "Docente"])

        datos = [
            ("8:00", "Matemáticas", "A1", "Profe Luis"),
            ("10:00", "Programación", "B2", "Profe Ana"),
            ("12:00", "BD", "C3", "Profe Juan")
        ]

        for i, fila in enumerate(datos):
            for j, valor in enumerate(fila):
                self.tabla_horario.setItem(i, j, QTableWidgetItem(valor))

       
        self.txt_avisos = QTextEdit()
        self.txt_avisos.setReadOnly(True)
        self.txt_avisos.setText("No hay avisos nuevos.")

        
        self.btn_tareas = QPushButton("Ver tareas")
        self.btn_tareas.clicked.connect(self.verTareasRequested.emit)

        layout.addWidget(self.lbl_bienvenida)
        layout.addWidget(QLabel("Materias inscritas"))
        layout.addWidget(self.lista_materias)
        layout.addWidget(QLabel("Horario"))
        layout.addWidget(self.tabla_horario)
        layout.addWidget(QLabel("Avisos"))
        layout.addWidget(self.txt_avisos)
        layout.addWidget(self.btn_tareas)

    def set_welcome(self, user: str):
        self.lbl_bienvenida.setText(f"Bienvenido {user}")