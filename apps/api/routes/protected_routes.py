from fastapi import APIRouter, Depends

from services.auth.dependencies import get_current_user
from services.database.models.user import User


router = APIRouter(prefix="/protected", tags=["protected"])


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_active": current_user.is_active,
        "is_superuser": current_user.is_superuser,
    }
