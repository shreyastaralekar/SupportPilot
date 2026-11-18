import os
import secrets

DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "supportpilot"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@127.0.0.1:3306/supportpilot"
)

ADMIN_ID = "ADMIN001"
ADMIN_PASSWORD = "SupportPilot@2026"

SECRET_KEY = os.environ.get(
    "SECRET_KEY", secrets.token_hex(32)
)