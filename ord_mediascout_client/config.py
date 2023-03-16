from dataclasses import dataclass


class ORDMediascoutConfig(dataclass):
    url: str
    username: str
    password: str
