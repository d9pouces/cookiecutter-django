import tempfile

DEBUG = True

MEDIA_ROOT = ".docker/media"
FILE_UPLOAD_TEMP_DIR = tempfile.gettempdir()
LOG_DIRECTORY = ".docker/log"
DATABASE_URL = "postgres://username:password@localhost:5432/database"
COMMON_REDIS_URL = "redis://:password@localhost:6379/1"
SERVER_BASE_URL = "http://localhost:8000/"
LOG_LEVEL = "DEBUG"
ADMIN_EMAIL = "asterix@19pouces.net"
