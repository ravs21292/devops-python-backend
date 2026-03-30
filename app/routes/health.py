from fastapi import APIRouter 
from app.service.sample_service import get_health_status

router = APIRouter()

@router.get("/health")
def health_check():
    return get_health_status()
