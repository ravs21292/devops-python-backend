from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Keyboard"},
            {"id": 3, "name": "Mouse"}
        ]
    }