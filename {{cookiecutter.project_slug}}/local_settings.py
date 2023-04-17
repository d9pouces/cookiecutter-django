# ##############################################################################
#  Copyright (c) 2023.                                                         #
#  This file local_settings.py is part of GlobalSiteChecker.                   #
#  Please check the LICENSE file for sharing or distribution permissions.      #
# ##############################################################################
"""Define settings for local development."""
import os

DEBUG = True
LOG_LEVEL = "DEBUG"
if "CI" not in os.environ:
    LOCAL_PATH = ".docker"
    LANGUAGE_CODE = "fr-FR"
    LISTEN_ADDRESS = "127.0.0.1:8000"
    DATABASE_URL = "postgres://username:password@127.0.0.1:5432/database"
    COMMON_REDIS_URL = "redis://:password@127.0.0.1:6379/1"
