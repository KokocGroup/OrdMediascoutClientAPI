from dataclasses import dataclass
from enum import Enum, StrEnum
from decimal import Decimal
from datetime import date

from requests.auth import HTTPBasicAuth


class ORDMediascoutConfig(dataclass):
    url: str
    username: str
    password: str


class ClientRelationshipType(StrEnum):
    DirectClient = "DirectClient"
    InitialContractClient = "InitialContractClient"


class LegalForms(StrEnum):
    JuridicalPerson = "JuridicalPerson"
    IndividualEntrepreneur = "IndividualEntrepreneur"
    PhysicalPerson = "PhysicalPerson"
    InternationalJuridicalPerson = "InternationalJuridicalPerson"
    InternationalPhysicalPerson = "InternationalPhysicalPerson"


class CounterpartyStatus(StrEnum):
    Created = "Created"
    Active = "Active"


class Client(dataclass):
    create_mode: ClientRelationshipType
    legal_form: LegalForms
    inn: str
    name: str
    mobile_phone: str
    epay_number: str
    reg_number: str
    oksm_number: str

    id: str
    status: str


class ContractStatus(StrEnum):
    Created = "Created"
    Active = "Active"


class ContractType(StrEnum):
    ServiceAgreement = "ServiceAgreement"
    MediationContract = "MediationContract"
    AdditionalAgreement = "AdditionalAgreement"
    SelfPromotionContract = "SelfPromotionContract"
    VirtualFinalContract = "VirtualFinalContract"


class ContractSubjectType(StrEnum):
    Distribution = "Distribution"
    OrgDistribution = "OrgDistribution"
    Representation = "Representation"
    Mediation = "Mediation"
    Other = "Other"


class ContractActionType(StrEnum):
    Contracting = "Contracting"
    Distribution = "Distribution"
    CommercialRepresentation = "CommercialRepresentation"
    Other = "Other"


class Contract(dataclass):
    number: str
    date: date
    amount: Decimal
    vat_included: bool
    is_agent_acting_for_publisher: bool
    type: ContractType
    subject_type: ContractSubjectType
    action_type: ContractActionType
    parent_main_contract_id: str
    contractor_id: str
    client_id: str
    final_contract_id: str

    id: str
    status: ContractStatus
    contractor_inn: str
    contractor_name: str
    client_inn: str
    client_name: str


class ORDMediascoutClient():
    def __init__(self, config: ORDMediascoutConfig):
        self.config = config
        self.auth = HTTPBasicAuth(self.config.username, self.config.password)

    def create_client(self, client: Client):
        pass

    def get_clients(self, id: str, inn: str, status: CounterpartyStatus) -> list(Client):
        pass

    def create_initial_contract(self, contract: Contract):
        pass

    def edit_initial_contract(self, contract: Contract):
        pass

    def get_initial_contracts(self, id: str, status: ContractStatus) -> list(Contract):
        pass
