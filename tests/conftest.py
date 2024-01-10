import pytest

from ord_mediascout_client import ORDMediascoutClient, ORDMediascoutConfig


@pytest.fixture
def client() -> ORDMediascoutClient:
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)
