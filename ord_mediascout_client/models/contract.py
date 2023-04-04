from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from enums import ContractStatus, ContractSubjectType, ContractType
from enums.contract_action_type import ContractActionType


@dataclass
class Contract:
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
