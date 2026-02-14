# presenters/login_presenter.py
from services.auth_service import AuthService
from ui.login_view import LoginView

# Este presenter funciona como intermediario entre la interfaz
# de login y el servicio que valida usuarios.
class LoginPresenter:
    def __init__(self, view: LoginView, auth: AuthService, on_success):
        self.view = view
        self.auth = auth
        self.on_success = on_success
        
        # Se conecta la señal del login con el método que lo procesa
        self.view.loginRequested.connect(self.handle_login)

    # Aquí se valida el usuario cuando intenta iniciar sesión
    def handle_login(self, username: str, password: str):
        result = self.auth.login(username, password)
        if result.ok:
            # Si todo sale bien se notifica al AppShell
            self.on_success(username, result.rol)
        else:
            # En caso de fallo se muestra el error
            self.view.show_error(result.message)
            self.view.clear_password()
