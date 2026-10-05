from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """
    Configuration de l'application chargée depuis le fichier .env
    """
    DATABASE_URL: str
    GEO_API_URL: str = "http://ip-api.com/json"
    CORS_ORIGINS: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> list[str]:
        """Retourne la liste des origines CORS autorisées."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    """Cache les settings pour éviter de relire le .env à chaque appel."""
    return Settings()