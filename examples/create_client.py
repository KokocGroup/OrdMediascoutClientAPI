from ord_mediascout_client import (
    ClientRelationshipType,
    CreateClientWebApiDto,
    LegalForm,
    ORDMediascoutClient,
    ORDMediascoutConfig,
)
from ord_mediascout_client.client import APIError

config = ORDMediascoutConfig(url='http://localhost:5000', username='username', password='password')

api = ORDMediascoutClient(config)

client = CreateClientWebApiDto(
    createMode=ClientRelationshipType.DirectClient,
    legalForm=LegalForm.JuridicalPerson,
    inn='1234567890',
    name='Test Client',
    mobilePhone='1234567890',
    epayNumber=None,
    regNumber=None,
    oksmNumber=None,
)

try:
    client = api.create_client(client)
    print(client)
except APIError as ex:
    print(ex)
except Exception as ex:
    print(ex)
