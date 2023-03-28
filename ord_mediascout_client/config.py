from pydantic.env_settings import BaseSettings
from pydantic.fields import Field
import dotenv
dotenv.load_dotenv()


class ORDMediascoutConfig(BaseSettings):
    class Config:
        case_sensitive = True

    url: str = Field(..., env='URL')
    username: str = Field(..., env='USERNAME')
    password: str = Field(..., env='PASSWORD')
