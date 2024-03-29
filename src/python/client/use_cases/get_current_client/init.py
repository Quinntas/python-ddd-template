from src.python.client.use_cases.get_current_client.get_current_client_usecase import GetCurrentClientUseCase
from src.python.user.use_cases.get_current_user.get_current_user_controller import GetCurrentUserController

get_current_client_usecase = GetCurrentClientUseCase()
get_current_client_controller = GetCurrentUserController(get_current_client_usecase)
