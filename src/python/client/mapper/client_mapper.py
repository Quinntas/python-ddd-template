from src.python.client.domain.client import Client
from src.python.shared.core.base_mapper import BaseMapper
from src.python.shared.utils.model_loader import dict_to_domain_loader, domain_to_dict_loader


class ClientMapper(BaseMapper):
    def __init__(self):
        super().__init__()

    @staticmethod
    def to_domain(raw_client_repo_result: dict) -> Client:
        return dict_to_domain_loader(Client, raw_client_repo_result.__dict__)

    @staticmethod
    def to_dict(_client: Client) -> dict:
        return domain_to_dict_loader(_client, Client)
