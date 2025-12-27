import hashlib
import getpass

class SecureLoginSystem:
    """
    Secure Login System implementing secure coding practices.
    Passwords are hashed using SHA-256 to prevent plaintext storage
    and credential exposure.
    """

    def __init__(self):
        # Simulated stored credentials (hashed password)
        self.stored_username = "admin"
        self.stored_password_hash = self.hash_password("admin123")

    def hash_password(self, password: str) -> str:
        """
        Hashes a password using SHA-256.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticates user credentials by comparing hashed passwords.
        """
        hashed_input_password = self.hash_password(password)
        return (
            username == self.stored_username and
            hashed_input_password == self.stored_password_hash
        )

    def run(self):
        """
        Executes the login process.
        """
        print("=== Secure Login System ===")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if self.authenticate(username, password):
            print("Login successful: Access granted.")
        else:
            print("Login failed: Invalid credentials.")


if __name__ == "__main__":
    login_system = SecureLoginSystem()
    login_system.run()

