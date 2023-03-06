from src.python.client.domain.client_avatar import ClientAvatar
from src.python.client.domain.client_model import Client
from src.python.client.domain.client_phone_number import ClientPhoneNumber
from src.python.shared.core.value_object.value_object import ValueObject
from src.python.shared.domain.shared_datetime import SharedDatetime
from src.python.shared.domain.shared_uuid import SharedUUID


def to_model(client) -> Client:
    client_loaded = {
        'id': client.id,
        'publicId': SharedUUID(client.publicId),
        'phone_number': ClientPhoneNumber(client.phone_number),
        'avatar': ClientAvatar(client.avatar),
        'userId': client.userId,
        'createdAt': SharedDatetime(client.createdAt),
        'updatedAt': SharedDatetime(client.updatedAt)
    }
    return Client(**client_loaded)


def to_dict(_client: Client) -> dict:
    return_value = {}
    client_dict: dict = _client.dict()
    private_attributes: list = Client.get_private_attributes()
    for key in client_dict:
        if key in private_attributes:
            continue
        if ValueObject in client_dict[key].__class__.__mro__:
            return_value[key] = client_dict[key].get_value()
            continue
        return_value[key] = client_dict[key]
    return return_value
