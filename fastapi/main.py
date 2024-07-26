from fastapi import FastAPI
from settings import settings

app = FastAPI()

@app.get("/{variable_name}")
def get_variable(variable_name: str):
    # Retrieve the value of the specified environment variable
    value = settings.get(variable_name)
    return {
        "variable": variable_name,
        "value": value
    }
