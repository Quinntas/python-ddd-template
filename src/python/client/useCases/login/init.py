from src.python.client.useCases.login.login_controller import LoginController
from src.python.client.useCases.login.login_usecase import LoginUseCase

login_usecase = LoginUseCase()
login_controller = LoginController(login_usecase)
