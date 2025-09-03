"""
📌 FastAPI Example: Path Parameters containing paths (:path)

Normally, path parameters capture only ONE segment of the URL (they stop at '/').
But sometimes, we want a parameter to capture a WHOLE path (with multiple '/').
For example: file system paths, nested directories, etc.

👉 Solution: Use `:path` after the parameter name.
"""

from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# ============================================================
# 1️⃣ Normal Path Parameter (default behavior)
# ============================================================

@app.get("/files/{file_name}")
async def get_file(file_name: str):
    """
    Endpoint: /files/{file_name}

    - Captures only ONE segment of the path (stops at '/').
    - Example:
        ✅ GET /files/myfile.txt  → {"file_name": "myfile.txt"}
        ❌ GET /files/home/johndoe/myfile.txt → Not allowed, breaks at first '/'
    """
    return {"file_name": file_name}


# ============================================================
# 2️⃣ Path Converter (:path) → Capture full path
# ============================================================

@app.get("/files/{file_path:path}")
async def get_file_with_path(file_path: str):
    """
    Endpoint: /files/{file_path:path}

    - Captures MULTIPLE segments of the path (includes '/').
    - Example:
        ✅ GET /files/home/johndoe/myfile.txt
            → {"file_path": "home/johndoe/myfile.txt"}

        ✅ GET /files//home/johndoe/myfile.txt
            → {"file_path": "/home/johndoe/myfile.txt"} (double // gives leading slash)

    🔎 Usage:
    - Useful for file systems, directories, nested routes, etc.
    """
    return {"file_path": file_path}

