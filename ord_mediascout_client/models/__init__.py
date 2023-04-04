from dataclasses import dataclass

from enums import ClientRelationshipType, LegalForm


@dataclass
class Client:
    create_mode: ClientRelationshipType
    legal_form: LegalForm
    inn: str
    name: str
    mobile_phone: str
    epay_number: str
    reg_number: str
    oksm_number: str

    id: str
    status: str
