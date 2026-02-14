# services/auth_service.py
from dataclasses import dataclass
 
# Regresa el resultado del login
@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    rol: str = ""

# Servicio que valida usuarios.
class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        # Mientras no esta conectado a una base de datos
        # usuario, contraseña y rol
        self._users = {
            "admin": ("1234", "admin"),
            "estudiante": ("5678", "estudiante"),
            "docente": ("4321", "docente")
        }

    # Metodo que revisa si las credenciales son correctas
    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")

        if username in self._users:
            pw, rol = self._users[username]
            if password == pw:
                return AuthResult(True, "Autenticación exitosa.", rol)
            
        return AuthResult(False, "Usuario o contraseña incorrectos.")
