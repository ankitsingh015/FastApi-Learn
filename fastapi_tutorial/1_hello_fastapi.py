from fastapi import FastAPI
from pydantic import BaseModel  # Pydantic is used for data validation and settings management using Python type annotations.

app = FastAPI()  # Create a FastAPI application instance (this will be your main app)


# ---------------------- Basic GET endpoints ----------------------

@app.get("/")  # → decorator that registers the function as a GET endpoint at /
async def root():  # → defines an asynchronous function (can handle many requests efficiently).
    return {"message": "Welcome to FastAPI!"}  # automatically returned as JSON response.


@app.get("/info")
async def get_info():
    return {"message": "This is your information"}

# If two functions have same path then first function will run only
# @app.get("/info")
# async def get_info_duplicate():
#     return {"message": "This is duplicate information"}  # This will not work  




# ---------------------- Recap ----------------------
# Steps to create a FastAPI application:
# 1. Import FastAPI.
# 2. Create an app instance.
# 3. Write a path operation decorator using decorators like @app.get("/").
# 4. Define a path operation function; for example, def root(): ....
# 5. Run the development server using the command: fastapi dev main.py
