from fastapi import FastAPI

app = FastAPI()

# Fake database (for demonstration)
fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Qux"},
    {"item_name": "Quux"},
]

# Query parameters → any function parameter that is not part of the path.

# ======================================================
# 1️⃣ Basic Query Parameters
# ======================================================
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 5):
    return fake_items_db[skip: skip + limit]

# ======================================================
# 2️⃣ Optional Query Parameter
# ======================================================
@app.get("/items/{item_id}")
async def read_item_optional(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# ======================================================
# 3️⃣ Query Parameter Type Conversion
# ======================================================
@app.get("/items/{item_id}/details")
async def read_item_type(item_id: str, short: bool = False):
    item = {"item_id": item_id}
    if not short:
        item.update({"description": "This is a detailed description"})
    return item

# ======================================================
# 4️⃣ Multiple Path + Query Parameters
# ======================================================
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Long description here"})
    return item

# ======================================================
# 5️⃣ Required Query Parameter
# ======================================================
@app.get("/items/{item_id}/required")
async def read_required_query(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}

# ======================================================
# 6️⃣ Mixed Query Parameters: required, default, optional
# ======================================================
@app.get("/items/{item_id}/mixed")
async def read_mixed_query(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


# ======================================================
# 7️⃣ THEORY SUMMARY (Interview Ready)
# ======================================================
"""
Query Parameters in FastAPI:
1. Passed after "?" in URL as key=value pairs. Example: /items/?skip=1&limit=2
2. Path params vs Query params:
   - Path param → fixed part of URL (/items/123)
   - Query param → optional info (?skip=1&limit=2)
3. Optional query params → set default=None
4. Type conversion → FastAPI auto converts (e.g., bool, int)
5. Defaults → provide default values if query not supplied
6. Required params → don't provide default; FastAPI returns 422 if missing
7. Multiple path + query → declare together, FastAPI distinguishes automatically
8. Mixed params → you can mix required, defaulted, and optional query params
9. Benefits:
   - Automatic validation and type conversion
   - Automatic interactive docs (/docs)
   - Cleaner API with clear contracts
"""
