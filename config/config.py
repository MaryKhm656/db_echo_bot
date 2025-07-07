import logging
import os
from dataclasses import dataclass

from environs import Env

logger = logging.getLogger(__name__)

@dataclass
class BotSettings:
    token: str
    admin_ids: list[int]
    
    
@dataclass
class DatabaseSettings:
    name: str
    host: str
    port: int
    user: str
    password: str
    
    
@dataclass
class RedisSettings:
    host: str
    port: int
    db: int
    password: str
    username: str
    
    
@dataclass
class LoggSettings:
    level: str
    format: str
    
    
@dataclass
class Config:
    bot: BotSettings
    db: DatabaseSettings
    redis: RedisSettings
    log: LoggSettings
    
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    
    if path:
        if not os.path.exists(path):
            logger.warning(".env file not found at '$s', skipping...", path)
        else:
            logger.info("Loading .env from '%s'", path)