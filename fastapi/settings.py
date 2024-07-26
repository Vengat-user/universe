from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    def get(self, variable_name):
        return os.getenv(variable_name, 'Not Set')

settings = Settings()
