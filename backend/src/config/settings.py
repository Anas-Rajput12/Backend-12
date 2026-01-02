from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    # =====================
    # API Keys & URLs
    # =====================
    openrouter_api_key: str
    qdrant_api_key: Optional[str] = None
    qdrant_url: str
    neon_database_url: str

    # =====================
    # Model Configuration
    # =====================
    embedding_model: str = "openai/text-embedding-3-small"
    llm_model: str = "anthropic/claude-sonnet-4.5"

    # =====================
    # App Settings
    # =====================
    app_name: str = "RAG Chatbot API"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # =====================
    # Qdrant Settings
    # =====================
    qdrant_collection_name: str = "document_chunks"

    # =====================
    # Vector Settings
    # =====================
    embedding_dimensions: int = 1536

    class Config:
        env_file = ".env"
        extra = "ignore"


# ✅ IMPORTANT: Lazy-load settings (Vercel-safe)
@lru_cache
def get_settings() -> Settings:
    return Settings()
