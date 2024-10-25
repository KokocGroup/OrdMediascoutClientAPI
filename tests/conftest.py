import logging
import random
import string
from datetime import datetime, timedelta
import time

import pytest

from ord_mediascout_client import (
    CreativeForm,
    CreatePlatformRequest,
    CampaignType,
    ContractType,
    ContractSubjectType,
    FileType,
    InvoicePartyRole,
    ORDMediascoutClient,
    ORDMediascoutConfig,
    PlatformType,
)


logging.getLogger('faker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


# Setup Contract test data
_contract = {
    'clientId': 'CLoEdAGEwv6EufqiTlkEeIAg',  # «Совкомбанк»
    'initial_contract_clientId': 'CLb0sZrPj5Y0KafIDU8ECPIw',  # «Рога и Копыта»
    'contractorId': 'CLcnt4AYTax0aLQfxuRZjG_Q',  # «ООО Рафинад»
    'finalContractId': 'CTiwhIpoQ_F0OEPpKj8vWKGg',
}


# Setup Invoice test data
_invoice = {
    'finalContractId': 'CTiwhIpoQ_F0OEPpKj8vWKGg',
    'initialContractId': 'CTKLAzsvgYREmK0unGXLsCTg',
    'erId': 'Pb3XmBtzsxtPgHUnh4hEFkxvF9Ay6CSGDzFnCHt',
}


# Setup Invoice test data
_creative = {
    'finalContractId': 'CTiwhIpoQ_F0OEPpKj8vWKGg',
    'initialContractId': 'CTKLAzsvgYREmK0unGXLsCTg',
    'srcUrl': 'https://kokoc.com/local/templates/kokoc/web/images/logo/logo.svg',
}


@pytest.fixture(scope='module')
def client():
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['ru_RU']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return int(time.time())


# Platform
@pytest.fixture
def create_platform_data():
    def _create_platform_data(**kwargs):
        rnd = random.randrange(111, 999)
        data = {
            'name': f'Test Platform {rnd}',
            'type': PlatformType.Site,
            'url': f'https://www.testplatform{rnd}.ru/',
            'isOwner': False,
        }
        data.update(kwargs)
        return CreatePlatformRequest(**data)

    return _create_platform_data


# Contract
@pytest.fixture(scope="module")
def final_contract_data():
    def _final_contract_data(**kwargs):
        data = {
            'number': f'{random_string()}-{random.randrange(111, 9999)}',
            'date': random_date(year='2024', month='05'),
            'amount': random.randrange(1000, 100000),
            'isAgentActingForPublisher': True,
            'type': ContractType.ServiceAgreement,
            'subjectType': ContractSubjectType.Distribution,
            # 'actionType': MediationActionType.Contracting,
            'parentMainContractId': '',
            'clientId': _contract['clientId'],
        }
        data.update(kwargs)
        return data

    return _final_contract_data


@pytest.fixture(scope="module")
def initial_contract_data():
    def _initial_contract_data(**kwargs):
        data = {
            'number': f'{random_string()}-{random.randrange(111, 9999)}',
            'date': random_date(year='2024', month='05'),
            'amount': random.randrange(1000, 100000),
            'isAgentActingForPublisher': True,
            'type': ContractType.ServiceAgreement,
            'subjectType': ContractSubjectType.Distribution,
            # 'actionType': MediationActionType.Contracting,
            'contractorId': _contract['contractorId'],
            'clientId': _contract['initial_contract_clientId'],
            'finalContractId': _contract['finalContractId'],
        }
        data.update(kwargs)
        return data

    return _initial_contract_data


@pytest.fixture(scope="module")
def outer_contract_data():
    def _outer_contract_data(**kwargs):
        data = {
            'number': f'{random_string()}-{random.randrange(111, 9999)}',
            'date': random_date(year='2024', month='05'),
            'amount': random.randrange(1000, 100000),
            'isAgentActingForPublisher': True,
            'type': ContractType.ServiceAgreement,
            'subjectType': ContractSubjectType.Distribution,
            # 'actionType': MediationActionType.Contracting,
            'contractorId': _contract['clientId'],
            'isRegReport': True,
        }
        data.update(kwargs)
        return data

    return _outer_contract_data


# Invoice
@pytest.fixture(scope="module")
def invoice_data():
    def _invoice_data(**kwargs):
        start_date = random_date(year='2024')
        end_date = random_date(start_date=start_date)
        start_date_fact = random_date(start_date=start_date)
        end_date_plan = random_date(start_date=start_date_fact)
        end_date_fact = random_date(start_date=end_date_plan)
        imps_plan = random.randrange(1000, 100000)

        data = {
            'number': 'INV-{}'.format(random.randrange(11111111, 99999999)),
            'date': start_date,
            'contractorRole': InvoicePartyRole.Rr,
            'clientRole': InvoicePartyRole.Ra,
            'amount': random.randrange(10000, 50000),
            'startDate': start_date,
            'endDate': end_date,
            'finalContractId': _invoice['finalContractId'],
            'initialContractsData': [
                {
                    'initialContractId': _invoice['initialContractId'],
                    'amount': 1000.00
                }
            ],
            'statisticsByPlatforms': [
                {
                    'initialContractId': _invoice['initialContractId'],
                    'erid': _invoice['erId'],
                    'platformUrl': 'http://www.testplatform.ru',
                    'platformName': 'Test Platform 1',
                    'platformType': PlatformType.Site,
                    'platformOwnedByAgency': False,
                    'impsPlan': imps_plan,
                    'impsFact': imps_plan,
                    'startDatePlan': start_date,
                    'startDateFact': start_date_fact,
                    'endDatePlan': end_date_plan,
                    'endDateFact': end_date_fact,
                    'amount': random.randrange(100, 1000),
                    'price': 0.5,
                }
            ]
        }

        data.update(kwargs)
        return data

    return _invoice_data


# Creative
@pytest.fixture(scope="module")
def creative_data():
    def _creative_data(**kwargs):
        rnd = random.randrange(111, 9999)
        data = {
                'finalContractId': _creative['finalContractId'],
                'initialContractId': _creative['initialContractId'],
                'creativeGroupName': f'_generated_creative_group_name_{random.randint(1000, 99999)}',
                'type': CampaignType.CPM,
                'form': CreativeForm.Banner,
                'advertiserUrls': ['https://clisite1.ru/', 'https://clisite2.ru/'],
                'description': f'Test mediadata creative {rnd}',
                'targetAudienceParams': [],
                'isSelfPromotion': False,
                'isNative': False,
                'isSocial': False,
                'mediaData': [
                    {
                        'fileName': 'logo.svg',
                        'fileType': FileType.Image,
                        # fileContentBase64="string",
                        'srcUrl': _creative['srcUrl'],
                        'description': f'Тестовый баннер {rnd}',
                        'isArchive': False,
                    }],
                'textData': [{'textData': f'Creative {rnd} text data test'}],
        }
        data.update(kwargs)
        return data

    return _creative_data


# Platform
@pytest.fixture(scope="module")
def platform_data():
    def _platform_data(**kwargs):
        rnd = random.randrange(100000, 999999)
        data = {
            'name': f'Test Platform {rnd}',
            'type': PlatformType.Site,
            'url': f'http://www.testplatform{rnd}.ru/',
            'isOwner': True,
        }
        data.update(kwargs)
        return data

    return _platform_data


# Utils
def parse_relative_value(value, base, lower_limit=None, upper_limit=None):
    """
    Функция для обработки строковых значений с "+" и "-" и вычисления целевого значения на основе base.
    """
    if isinstance(value, str) and value.startswith(("+", "-", "+-")):
        if value.startswith("+-"):
            delta = int(value[2:])
            return random.randint(base - delta, base + delta)
        elif value.startswith("+"):
            delta = int(value[1:])
            return random.randint(base, base + delta)
        elif value.startswith("-"):
            delta = int(value[1:])
            return random.randint(base - delta, base)

    # Если значение не является строкой с "+", "-" или "+-", то используем указанное значение как есть.
    return int(value)


def random_date(year=None, month=None, start_date=None):
    """Генерация даты в формате '2024-10-23'
    Примеры использования:
    random_date(year='+3', month='05'))        # Рандомная дата от текущего до +3 лет, в мае
    random_date(year='+3', month='05'))        # Рандомная дата от текущего до +3 лет, в мае
    random_date(year='2024', month='-5'))      # Рандомная дата в 2024 году, месяцы -5 от текущего (например, текущий - октябрь, результат - май)
    random_date(year='+-5', month='+-2'))      # Рандомная дата +/- 5 лет и +/- 2 месяца от текущего
    random_date(year='+-5', month='+-2', start_date='2023-05-16'))  # Аналогично, но от указанной стартовой даты
    """
    # Установить базовую дату
    if start_date:
        base_date = datetime.strptime(start_date, '%Y-%m-%d')
    else:
        base_date = datetime.now()

    year = year or base_date.year
    month = month or base_date.month

    # Определить год и месяц на основе переданных значений или устанавить случайные значения
    year = parse_relative_value(year, base_date.year) if year is not None else random.randint(2000, datetime.now().year)
    month = parse_relative_value(month, base_date.month, 1, 12) if month is not None else random.randint(1, 12)

    # Если месяц за пределами 1-12, то скорректировать значения года и месяца
    if month < 1:
        year -= 1
        month = 12 + month
    elif month > 12:
        year += 1
        month = month - 12

    # Определить начальный день
    start_day = base_date.day if start_date else 1

    # Создать базовую дату и добавить случайное количество дней
    base_date = datetime(year=year, month=month, day=start_day)
    random_days_to_add = random.randint(1, 3)
    new_date = base_date + timedelta(days=random_days_to_add)

    return new_date.strftime('%Y-%m-%d')


def random_string(length=3):
    return ''.join(random.choices(string.ascii_uppercase, k=length))
