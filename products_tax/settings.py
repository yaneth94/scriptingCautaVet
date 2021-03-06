from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent.absolute() / '.env'
load_dotenv(dotenv_path=env_path)


# there are required to access to api
api_key = os.getenv('API_KEY_MASTER')
api_token = os.getenv('API_TOKEN_MASTER')

api_key_nexus = os.getenv('API_KEY_NEXUS')
