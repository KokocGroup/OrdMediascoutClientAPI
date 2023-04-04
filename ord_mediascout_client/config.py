from dataclasses import dataclass


@dataclass
class ORDMediascoutConfig:
    url: str
    username: str
    password: str
