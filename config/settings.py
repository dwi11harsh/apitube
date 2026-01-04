from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str = "youtube-transcripts"
    PINECONE_ENVIRONMENT: str = "us-east-1"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    SUPABASE_URL: str
    SUPABASE_KEY: str
    CHUNK_SIZE: int = 6000
    CHUNK_OVERLAP: int = 1000
    TOP_K: int = 5

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
