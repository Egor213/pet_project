from enum import Enum

from pydantic import BaseModel


class Mode(str, Enum):
    debug = 'debug'
    production = 'production'
    
    
class DBConfig(BaseModel):
    uri: str
