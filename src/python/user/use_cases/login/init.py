from src.python.user.use_cases.login.login_controller import LoginController
from src.python.user.use_cases.login.login_usecase import LoginUseCase

login_usecase = LoginUseCase()
login_controller = LoginController(login_usecase)
