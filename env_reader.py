from pydantic_settings import BaseSettings
from pydantic import SecretStr


class AppConfig(BaseSettings):
    DB_IP: SecretStr
    DB_NAME: SecretStr
    DB_LOGIN: SecretStr
    DB_PASSWORD: SecretStr
    BOT_TOKEN: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_config = AppConfig()
