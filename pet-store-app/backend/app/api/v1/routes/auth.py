from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

# Sample route
@router.get("/")
def get_auth_status():
    return {"status": "ok"}
