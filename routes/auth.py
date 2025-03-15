from fastapi import APIRouter
from controllers.auth.login_user import LoginUser
from controllers.auth.models import LoginRequest

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/login')
def login_user(user_details: LoginRequest):
    return LoginUser(user_details).handler()