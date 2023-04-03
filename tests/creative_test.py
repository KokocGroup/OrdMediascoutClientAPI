import pytest


from ord_mediascout_client import (
    ORDMediascoutConfig,
    ORDMediascoutClient,
    CreateCreativeWebApiDto,
    GetCreativesWebApiDto,
    CreativeMediaDataItemWebApiDto,
    CreativeTextDataItemWebApiDto,
    CreativeType,
    CreativeForm,
    CreativeStatus,
)


@pytest.fixture
def client() -> ORDMediascoutClient:
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)


def test_create_mediadata_creative(client: ORDMediascoutClient) -> None:
    request_data = CreateCreativeWebApiDto(
        finalContractId='CTiwhIpoQ_F0OEPpKj8vWKGg',
        initialContractId='CTKLAzsvgYREmK0unGXLsCTg',
        type=CreativeType.CPM,
        form=CreativeForm.Banner,
        advertiserUrls=[
            'https://clisite1.ru/',
            'https://clisite2.ru/',
        ],
        description='Test mediadata creative 1',
        targetAudience='',
        isNative=False,
        isSocial=False,
        okvedCodes=[
            '01.02',
            '01.03',
        ],
        mediaData=[
            CreativeMediaDataItemWebApiDto(
                fileName='logo.svg',
                # fileContentBase64="string",
                srcUrl="https://kokoc.com/local/templates/kokoc/web/images/logo/logo.svg",
                description='Тестовый баннер 1',
                isArchive=False
            )
        ],
    )

    response_data = client.create_creative(request_data)

    assert response_data.id is not None


def test_create_textdata_creative(client: ORDMediascoutClient) -> None:
    request_data = CreateCreativeWebApiDto(
        finalContractId='CTiwhIpoQ_F0OEPpKj8vWKGg',
        initialContractId='CTKLAzsvgYREmK0unGXLsCTg',
        type=CreativeType.CPM,
        form=CreativeForm.Banner,
        advertiserUrl='https://clisite.ru/',
        description='Test textdata creative 2',
        targetAudience='',
        isNative=False,
        isSocial=False,
        okvedCodes=[
            '01.05',
        ],
        textData=[
            CreativeTextDataItemWebApiDto(
                textData='Creative 1 text data test'
            ),
        ]
    )

    response_data = client.create_creative(request_data)

    assert response_data.id is not None


def test_get_creatives(client: ORDMediascoutClient) -> None:
    request_data = GetCreativesWebApiDto(
        status=CreativeStatus.Active
    )

    response_data = client.get_creatives(request_data)

    for creative in response_data:
        assert creative.id is not None
