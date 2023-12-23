


def load_variable(env_filename=".env", variable_name: str) -> str:
    import os
    from dotenv import load_dotenv
    load_dotenv(env_filename)
    return os.getenv(variable_name)
    
    