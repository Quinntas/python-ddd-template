from src.python.shared.core.base_repo import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    async def get_user_with_public_id(self, public_id: str):
        return await self.get_unique("user", {'publicId': public_id})

    async def get_user_with_email(self, email: str):
        return await self.get_unique("user", {'email': email})

    async def verify_email(self, public_id: str):
        return await self.update("user", {'email_verified': True}, {'publicId': public_id})
