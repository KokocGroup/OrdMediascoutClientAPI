from config import ORDMediascoutConfig
from enums import ContractStatus, CounterpartyStatus
from models import Client
from models.contract import Contract
from requests.auth import HTTPBasicAuth


class ORDMediascoutClient:
    def __init__(self, config: ORDMediascoutConfig):
        self.config = config
        self.auth = HTTPBasicAuth(self.config.username, self.config.password)

    def create_client(self, client: Client):
        pass

    def get_clients(self, id: str, inn: str, status: CounterpartyStatus) -> list[Client]:
        pass

    def create_initial_contract(self, contract: Contract):
        pass

    def edit_initial_contract(self, contract: Contract):
        pass

    def get_initial_contracts(self, id: str, status: ContractStatus) -> list[Contract]:
        pass
