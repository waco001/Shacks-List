import os
SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
CSRF_ENABLED = True
USER_APP_NAME        = "Shack's List"                # Used by email templates
DATABASE_URL = "sqlite:///database/database.db"