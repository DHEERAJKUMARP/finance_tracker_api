from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/users",
    tags=["User Management"]
)

@router.post("/register")
async def register_user(user_data: dict = Body(...)):
    pass

@router.post("/login")
async def login_user(credentials: dict = Body(...)):
    pass

@router.post("/set-pin")
async def set_pin(data: dict = Body(...)):
    pass

@router.post("/set-biometric")
async def set_biometric(data: dict = Body(...)):
    pass
