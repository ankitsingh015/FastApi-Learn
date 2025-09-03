from fastapi import FastAPI

app = FastAPI()

# ------------------- Path Parameters -------------------
# Path parameters are variables that form part of the URL.
# You declare them inside curly braces {} in the path.
# The value passed in the URL will be sent to your function.


# ============================================================
# 1️⃣ Path Parameter WITHOUT Type Declaration
# ============================================================

@app.get("/info-no-type/{user_id}")
async def get_info_no_type(user_id):
    """
    Endpoint: /info-no-type/{user_id}
    
    Path Parameter:
    - user_id: str (no explicit type declared, defaults to string).
    
    Behavior:
    - Whatever value is passed in the URL is treated as a string.
    - No validation happens.

    Examples:
    - GET /info-no-type/foo   → {"user_id": "foo"}
    - GET /info-no-type/123   → {"user_id": "123"}  (still a string, not int)
    """
    return {"user_id": user_id}


# ============================================================
# 2️⃣ Path Parameter WITH Type Declaration (int)
# ============================================================

@app.get("/info/{user_id}")
async def get_info(user_id: int):
    """
    Endpoint: /info/{user_id}
    
    Path Parameter:
    - user_id: int  👈 FastAPI will automatically parse and validate this as an integer.

    Examples:
    - GET /info/10   → {"user_id": 10}  ✅ integer
    - GET /info/abc  → ❌ Validation error (422)
    """
    return {"user_id": user_id}
