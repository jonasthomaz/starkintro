import os


class Config:
    STARK_ENVIRONMENT = os.getenv("STARK_ENVIRONMENT", "sandbox")
    STARK_ID = os.getenv("STARK_ID", "")
    STARK_ORGANIZATION_ID = os.getenv("STARK_ORGANIZATION_ID", "")
    STARK_PRIVATE_KEY = os.getenv("STARK_PRIVATE_KEY", "")
