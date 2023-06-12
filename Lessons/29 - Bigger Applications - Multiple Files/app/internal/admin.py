from fastapi import APIRouter, Depends
from ..dependencies import get_special_header

router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(get_special_header)],
    tags=["Admin"]
)


@router.get("/")
def index():
    return {"message": "You're an admin, I think"}
