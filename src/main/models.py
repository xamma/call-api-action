from pydantic_settings import BaseSettings
from pydantic import validator

"""
Configuration class for the app.
Precendences:
1. ENV Vars
2. .env File
3. Default Vars
"""

class AppSettings(BaseSettings):
    api_url: str | None = None
    headers: str | None = None
    http_method: str | None = None
    request_body: str | None = None
    query_params: str | None = None

    @validator('http_method')
    def validate_http_method(cls, value):
        allowed_methods = {"GET", "POST", "PUT", "PATCH", "DELETE"}
        if value not in allowed_methods:
            raise ValueError(f'Invalid HTTP method: {value}. Must be one of {allowed_methods}')
        return value