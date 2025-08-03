from pydantic_settings import BaseSettings, YamlConfigSettingsSource
from .yaml_config import Mode, DBConfig


class Config(BaseSettings):
    mode: Mode
    db: DBConfig
    
    
    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (YamlConfigSettingsSource(settings_cls, "infra/config.yaml"),)
