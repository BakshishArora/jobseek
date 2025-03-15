from controllers.auth.models import LoginRequest
class LoginUser:
    def __init__(self, user_details: LoginRequest):
        self.user_details = user_details

    def handler(self):
        return "hello again"