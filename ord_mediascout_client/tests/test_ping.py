import pytest

from ord_mediascout_client import ORDMediascoutConfig, ORDMediascoutClient


@pytest.fixture
def client():
    config = ORDMediascoutConfig()
    return ORDMediascoutClient(config)


def test_ping(client):
    assert client.ping()


def test_ping_auth(client):
    assert client.ping_auth()
