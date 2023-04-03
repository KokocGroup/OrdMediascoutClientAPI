import pytest


from ord_mediascout_client import (
    ORDMediascoutConfig,
    ORDMediascoutClient,
    CreateInitialContractWebApiDto,
    CreateFinalContractWebApiDto,
    CreateOuterContractWebApiDto,
    SelfPromotionContractWebApiDto,
    GetInitialContractsWebApiDto,
    GetFinalContractsWebApiDto,
    GetOuterContractsWebApiDto,
    ContractType,
    ContractStatus,
    ContractSubjectTypeWebApi,
    MediationActionType,
)


@pytest.fixture
def client() -> ORDMediascoutClient:
    config = ORDMediascoutConfig()
    config.username = 'M0000034' # *****
    return ORDMediascoutClient(config)


def test_create_final_contract(client: ORDMediascoutClient) -> None:
    request_data = CreateFinalContractWebApiDto(
        number='AB1234567890C',
        date='2023-03-02',
        amount=100000.00,
        vatIncluded=True,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectTypeWebApi.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId='',
        clientId='CLoEdAGEwv6EufqiTlkEeIAg',
    )

    response_data = client.create_final_contract(request_data)

    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    assert request_data.vatIncluded == response_data.vatIncluded
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    # assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.clientId == response_data.clientId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_final_contracts(client: ORDMediascoutClient) -> None:
    request_data = GetFinalContractsWebApiDto(
        status=ContractStatus.Active
    )

    response_data = client.get_final_contracts(request_data)

    for final_contract in response_data:
        assert final_contract.id is not None


def test_create_initial_contract(client: ORDMediascoutClient) -> None:
    request_data = CreateInitialContractWebApiDto(
        number='AB234567890987654321C',
        date='2023-03-07',
        amount=145000.00,
        vatIncluded=True,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectTypeWebApi.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId=None,
        contractorId='CLcnt4AYTax0aLQfxuRZjG_Q',
        clientId='CLoEdAGEwv6EufqiTlkEeIAg',
        finalContractId='CTiwhIpoQ_F0OEPpKj8vWKGg',
    )

    response_data = client.create_initial_contract(request_data)

    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    assert request_data.vatIncluded == response_data.vatIncluded
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.contractorId == response_data.contractorId
    assert request_data.clientId == response_data.clientId
    assert request_data.finalContractId == response_data.finalContractId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_initial_contracts(client: ORDMediascoutClient) -> None:
    request_data = GetInitialContractsWebApiDto(
        status=ContractStatus.Active
    )

    response_data = client.get_initial_contracts(request_data)

    for initial_contract in response_data:
        assert initial_contract.id is not None


def test_create_outer_contract(client: ORDMediascoutClient) -> None:
    request_data = CreateOuterContractWebApiDto(
        number='AB1234567890123CD',
        date='2023-03-05',
        amount=150000.00,
        vatIncluded=True,
        isAgentActingForPublisher=True,
        type=ContractType.ServiceAgreement,
        subjectType=ContractSubjectTypeWebApi.Distribution,
        # actionType=MediationActionType.Contracting,
        parentMainContractId='',
        contractorId='CLoEdAGEwv6EufqiTlkEeIAg',
    )

    response_data = client.create_outer_contract(request_data)

    assert request_data.number == response_data.number
    assert request_data.date == response_data.date
    assert request_data.amount == response_data.amount
    assert request_data.vatIncluded == response_data.vatIncluded
    # assert request_data.isAgentActingForPublisher == response_data.isAgentActingForPublisher
    assert request_data.type == response_data.type
    assert request_data.subjectType == response_data.subjectType
    # assert request_data.actionType == response_data.actionType
    # assert request_data.parentMainContractId == response_data.parentMainContractId
    assert request_data.contractorId == response_data.contractorId
    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active


def test_get_outer_contracts(client: ORDMediascoutClient) -> None:
    request_data = GetOuterContractsWebApiDto(
        status=ContractStatus.Active
    )

    response_data = client.get_outer_contracts(request_data)

    for outer_contract in response_data:
        assert outer_contract.id is not None

"""
! ОТКЛЮЧЕНО
! СОЗДАЕТСЯ ТОЛЬКО ОДИН РАЗ, ПОСЛЕ ЧЕГО СОЗДАТЬ НОВЫЙ НЕ ДАЕТ
def test_create_self_promotion_contract(client: ORDMediascoutClient) -> None:
    request_data = SelfPromotionContractWebApiDto()

    response_data = client.create_self_promotion_contract(request_data)

    assert response_data.id is not None
    assert response_data.status == ContractStatus.Created or ContractStatus.Active
"""


def test_get_self_promotion_contract(client: ORDMediascoutClient) -> None:
    response_data = client.get_self_promotion_contracts()

    for self_promotion_contract in response_data:
        assert self_promotion_contract.id is not None
