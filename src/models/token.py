from enum import Enum


class TokenType(str, Enum):
    BEARER = 'bearer'


class Token():
    def __init__(self, access_token: str, refresh_token: str, token_type=TokenType.BEARER):
        self.token_type = token_type
        self.access_token = access_token
        self.refresh_token = refresh_token
