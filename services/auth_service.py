# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    rol: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        
        self._users = {
            "admin": ("1234", "admin"),
            "estudiante": ("abcd", "estudiante"),
            "docente": ("9999", "docente")
        }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")

        if username in self._users:
            pw, rol = self._users[username]
            if password == pw:
                return AuthResult(True, "Autenticación exitosa.", rol)
            
        return AuthResult(False, "Usuario o contraseña incorrectos.")
