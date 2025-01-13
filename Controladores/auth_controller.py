import hashlib

class AuthController:
    def __init__(self):
        self.users = {
            "admin": self.hash_password("password"),  # Ejemplo de usuario y contraseña
            "user1": self.hash_password("123456")
        }

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_credentials(self, username, password):
        hashed_password = self.hash_password(password)
        if username in self.users and self.users[username] == hashed_password:
            return True
        return False

    def add_user(self, username, password):
        if username in self.users:
            raise ValueError("El usuario ya existe")
        self.users[username] = self.hash_password(password)

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("El usuario no existe")
        del self.users[username]