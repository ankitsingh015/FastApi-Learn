from fastapi import FastAPI
from pydantic import BaseModel  # Pydantic is used for data validation and settings

app = FastAPI()


# ----------------------
# Define a Pydantic model (schema)
# ----------------------
class Info(BaseModel):  # 👈 Schema for data validation
    name: str
    age: str
    # exiting: bool = False  # Default value if not provided
    exiting: bool = None  # Optional field


# ----------------------
# POST endpoint using the schema
# ----------------------
@app.post("/create_post/")
async def create_post(payload: Info):
    """
    POST endpoint that accepts JSON body in this schema:
    {
      "name": "Jai Shree Ram",
      "age": "infinite"
      "exiting": true
    }
    """
    # Access values using dot notation (payload.name, payload.age)
    print(f"Name: {payload.name} \nAge: {payload.age} \nExiting: {payload.exiting}")
    return {"message": f"Name: {payload.name}, Age: {payload.age} Exiting: {payload.exiting} User Created Successfully!"}


# ----------------------
# Recap / Steps to create FastAPI app with schema validation
# ----------------------
# 1. Import FastAPI and Pydantic's BaseModel.
# 2. Create a FastAPI app instance.
# 3. Define a Pydantic model (schema) for expected data.
# 4. Write a POST endpoint using @app.post("/create_post/").
# 5. Accept the Pydantic model as a parameter in the endpoint function.
# 6. FastAPI automatically validates input and generates docs.


# ----------------------
# Why We Need Schema?
# ----------------------
# - Clients can send any random data in the request body.
# - Schema defines the expected structure of request and response data.
# - Provides automatic data validation and type conversion.
# - Creates clear API contracts for clients.
# - Generates interactive API documentation (Swagger UI / ReDoc).
