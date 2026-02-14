# ui/main_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuracion de la ventana principal
        self.setWindowTitle("Ventana Principal - MVP")
        self.resize(520, 320)
        self._label = QLabel("Bienvenido, has iniciado sesión correctamente.", alignment=Qt.AlignCenter)
        self.setCentralWidget(self._label)

    # mensaje de bienvenida para el admin
    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, {user}. ¡Sesión iniciada!")
