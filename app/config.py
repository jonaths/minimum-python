from dotenv import load_dotenv
import os
from rich.console import Console

console = Console()

load_dotenv(verbose=True)

ENV_VAR = os.getenv('ENV_VAR')