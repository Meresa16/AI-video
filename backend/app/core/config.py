from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    DATABASE_URL: str = \
postgresql+psycopg2://postgres:postgres@localhost:5432/ai_video_studio\\n    REDIS_URL: str = \redis://localhost:6379/0\\n    SECRET_KEY: str = \change-me\\n    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60\n    \n    class Config:\n        env_file = \.env\\n\nsettings = Settings()
