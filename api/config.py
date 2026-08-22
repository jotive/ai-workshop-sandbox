import os


class Settings:
    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY", "dev-local-key")
        self.database_path = os.getenv("DATABASE_PATH", "tickets.db")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
