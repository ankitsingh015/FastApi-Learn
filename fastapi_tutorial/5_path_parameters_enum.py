from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# ============================================================
# 1️⃣ Enum Definition
# ============================================================
# - We create an Enum class to restrict valid values.
# - Inherit from (str, Enum) so FastAPI knows it's a string enum.
# - Each attribute defines one allowed value.

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# ============================================================
# 2️⃣ Basic Enum Usage
# ============================================================
@app.get("/models-basic/{model_name}")
async def get_model_basic(model_name: ModelName):
    """
    Example: /models-basic/alexnet

    - model_name must be one of: "alexnet", "resnet", "lenet".
    - FastAPI will validate automatically.
    - Docs will show dropdown of allowed values.

    ✅ GET /models-basic/alexnet → {"model_name": "alexnet"}
    ❌ GET /models-basic/invalid → 422 validation error
    """
    return {"model_name": model_name}


# ============================================================
# 3️⃣ Advanced Enum Usage
# ============================================================
@app.get("/models-advanced/{model_name}")
async def get_model_advanced(model_name: ModelName):
    """
    Example: /models-advanced/resnet

    Demonstrates advanced Enum usage:
    - Compare directly with Enum members
    - Extract raw value using .value
    - Return enum → auto-converted to string in JSON
    """
    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name,          # returns "alexnet"
            "message": "Deep Learning FTW!",
            "raw_value": model_name.value      # explicit string
        }

    if model_name.value == "lenet":
        return {
            "model_name": model_name,          # returns "lenet"
            "message": "LeCNN all the images",
            "raw_value": model_name.value
        }

    return {
        "model_name": model_name,              # returns "resnet"
        "message": "Have some residuals",
        "raw_value": model_name.value
    }
