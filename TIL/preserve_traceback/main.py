import asyncio
from fastapi import HTTPException

async def call_keycloak():
    raise ValueError("Invalid user data")  # Lỗi giả lập

# preserve traceback với 'from'
async def main_with_from():
    try:
        await call_keycloak()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": "internal_error", "message": "Service unavailable"}
        ) from e

async def main_without_from():
    try:
        await call_keycloak()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail={"error": "internal_error", "message": "Service unavailable"}
        )

# Chạy thử
async def test():
    try:
        await main_with_from()
    except HTTPException as e:
        print("With 'from':", e.__cause__)

    try:
        await main_without_from()
    except HTTPException as e:
        print("Without 'from':", e.__cause__)

asyncio.run(test())