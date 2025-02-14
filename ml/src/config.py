from fastapi.security import OAuth2PasswordBearer
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.logger import logger


class AuthConfig(BaseSettings):
    secret_key: str
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_prefix='AUTH_', extra="allow")


class DBConfig(BaseSettings):
    driver: str
    host: str
    port: int | None = Field(default=None)
    username: str
    password: str
    db_name: str = Field(validation_alias="db_name")

    @property
    def db_url(self):
        db_url = f"{self.driver}://{self.username}:{self.password}@{self.host}{f':{self.port}' if self.port else ''}/{self.db_name}"
        logger.debug("DB URL: %s", db_url)
        return db_url

    model_config = SettingsConfigDict(env_prefix='DB_', extra="allow")


auth_config = AuthConfig()
db_config = DBConfig()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"http://localhost/api/auth/login")