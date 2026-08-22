import os
from dotenv import load_dotenv

# Carga las variables desde el archivo .env al entorno de ejecución
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "App Default")
APP_VERSION = os.getenv("APP_VERSION", "0.0")
ADMIN_USER = os.getenv("ADMIN_USER", "root")
