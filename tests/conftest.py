import pytest

from ord_mediascout_client import ORDMediascoutClient, ORDMediascoutConfig


@pytest.fixture
def client():
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)
