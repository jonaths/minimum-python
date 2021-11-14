from dotenv import load_dotenv
import os
from rich.console import Console

from common.tools.lg import Logger

load_dotenv(verbose=True)

# Poner aquí cualquier otra variable que haya que cargar del archivo .env

ENV_VAR = os.getenv('ENV_VAR')
STORAGE_LOGS = os.getenv('STORAGE_LOGS')

console = Console()
log = Logger(log_dir=STORAGE_LOGS).logger
