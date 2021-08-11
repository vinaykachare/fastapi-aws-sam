from pydantic import BaseSettings
from os import getenv, path

base_dir_path = f"{path.dirname(path.realpath(__file__))}"
class Settings(BaseSettings):
    env: str
    
    class Config:
        env_file = f"{base_dir_path}/{getenv('ENV','dev')}.env"
