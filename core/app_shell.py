# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter
from ui.estudiante_view import EstudianteView
from ui.docente_view import DocenteView

# Controlador principal de la aplicacion.
# Aquí se administran todas las pantallas y se cambia entre ellas
# dependiendo del rol del usuario.
class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_MAIN = 1

    def __init__(self):
        super().__init__()
        
        # Se crean todas las vistas que tendra la aplicación
        self.login_view = LoginView()
        self.main_view = MainView()
        self.estudiante_view = EstudianteView()
        self.docente_view = DocenteView()

        # Servicio encargado de validar usuarios
        self.auth_service = AuthService()
        
        # Presenter que conecta la vista login con la logica
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_main
        )
        
        # Se agregan todas las vistas al contenedor
        self.addWidget(self.login_view)
        self.addWidget(self.main_view)
        self.addWidget(self.estudiante_view)
        self.addWidget(self.docente_view)
        
        # La vista por defecto es siempre la del login
        self.setCurrentIndex(self.PAGE_LOGIN)
        
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    # Este metodo se ejecuta cuando el login fue exitoso
    # y decide que pantalla mostrar según el rol.
    def _go_main(self, username: str, rol:str):
        
        if rol == "admin":
            self.main_view.set_welcome(username)
            self.setCurrentWidget(self.main_view)

        elif rol == "estudiante":
            self.estudiante_view.set_welcome(username)
            self.setCurrentWidget(self.estudiante_view)

        elif rol == "docente":
            self.docente_view.set_welcome(username)
            self.setCurrentWidget(self.docente_view)
            
       