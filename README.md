# Mediascout ORD API client

Unofficial python client for [ORD Mediascout API](https://demo.mediascout.ru/swagger/index.html).

## Installation

    pip install ord-mediascout-client

## Usage

    from ord_mediascout_client import ORDMediascoutClient, ORDMediascoutConfig, Client

    config = ORDMediascoutConfig(
        url='http://localhost:5000',
        username='username',
        password='password',
    )  

    api = MediaScoutClient(config)

    client = Client(
        name="Test Client",
        inn="1234567890",
        ...
    )

    try:
        client = api.register_client(client)
    except ClientAlreadyExists:
        pass
    except ORDMediascoutError as e:
        print(e.response.code)


## Testing

    pytest
