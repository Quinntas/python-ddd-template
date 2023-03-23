from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.client.dto.new_client_dto import NewClientDTO
from src.python.client.repo.index import client_repo
from src.python.shared.core.base_usecase import UseCase
from src.python.user.domain.user_email import UserEmail
from src.python.user.domain.user_name import UserName
from src.python.user.domain.user_password import UserPassword


class CreateClientUseCase(UseCase):
    async def execute(self, new_client: NewClientDTO):
        name = UserName(new_client.name).value
        email = UserEmail(new_client.email).value
        phonenumber = ClientPhoneNumber(new_client.phone_number).value
        password = UserPassword(new_client.password, False).value

        client: NewClientDTO = NewClientDTO(
            email=email,
            name=name,
            phone_number=phonenumber,
            password=password
        )

        await client_repo.create_client(client)
