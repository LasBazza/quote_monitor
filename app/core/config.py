from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):

    DB_NAME: str
    DB_PASSWORD: str
    DB_USER: str
    DB_PORT: int

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    API_KEY: str
    BASE_URL: str
    QUOTE_FUNCTION: str
    CURRENCY_FUNCTION: str

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
