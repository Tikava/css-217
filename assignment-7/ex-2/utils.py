import uuid

class AuthenticationManager:
    def __init__(self, users):
        self.users = users
        self.logged_in_users = {}

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            session_token = str(uuid.uuid4())
            self.logged_in_users[session_token] = username
            print("Login successful.")
            return session_token
        else:
            print("Invalid username or password.")
            return None

    def logout(self, session_token):
        if session_token in self.logged_in_users:
            del self.logged_in_users[session_token]
            print("Logout successful.")
        else:
            print("Session not found.")
    
    def is_authorized(self, session_token, required_roles):
        if session_token in self.logged_in_users:
            username = self.logged_in_users[session_token]
            user_roles = self.users[username]["roles"]
            for role in required_roles:
                if role in user_roles:
                    return True
            print("Unauthorized access.")
            return False
        else:
            print("Session not found.")
            return False