from src.python.client.useCases.createClient.create_client_controller import CreateClientController
from src.python.client.useCases.createClient.create_client_usecase import CreateClientUseCase

create_client_usecase = CreateClientUseCase()

create_client_controller = CreateClientController(create_client_usecase)
