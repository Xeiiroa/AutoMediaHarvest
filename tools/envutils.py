import os
from dotenv import load_dotenv

def load_variable(variable_name, env_filename=".env"):
    load_dotenv(env_filename)
    return os.getenv(variable_name)
    




