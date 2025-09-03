from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# ============================================================
# 1️⃣ Order Matters in Path Operations
# ============================================================

# Fixed path: /users/me
# This must be declared BEFORE /users/{user_id}, otherwise
# "me" will be mistakenly treated as a user_id value.
@app.get("/users/me")
async def read_user_me():
    """
    Endpoint: /users/me
    
    Behavior:
    - Always returns a fixed response for the current user.
    
    Example:
    - GET /users/me → {"user_id": "the current user"}
    """
    return {"user_id": "the current user"}


# Dynamic path: /users/{user_id}
# This will capture any value passed in place of {user_id}.
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    Endpoint: /users/{user_id}
    
    Path Parameter:
    - user_id: str (captured from URL)
    
    Behavior:
    - Any string after /users/ will be treated as user_id.
    
    Example:
    - GET /users/john → {"user_id": "john"}
    - GET /users/123  → {"user_id": "123"}
    """
    return {"user_id": user_id}


# ============================================================
# 2️⃣ Duplicate Path Operations (NOT ALLOWED)
# ============================================================

# First definition of /users
@app.get("/users")
async def read_users():
    """
    Endpoint: /users
    
    Behavior:
    - Returns a list of user names.
    """
    return ["Rick", "Morty"]


# Second definition of /users
# ⚠️ This will NEVER run because the first one always matches.
@app.get("/users")
async def read_users2():
    """
    Endpoint: /users
    
    Behavior:
    - This will be ignored since the first definition takes priority.
    """
    return ["Bean", "Elfo"]

# ============================================================
# Recap
# ============================================================
# 1. Always define fixed paths (e.g., /users/me) BEFORE dynamic ones (/users/{user_id}).
# 2. FastAPI matches routes in the order they are defined.
# 3. Duplicate paths (e.g., two /users) → only the FIRST one is used.
