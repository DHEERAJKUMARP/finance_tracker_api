from fastapi import APIRouter, Body

router = APIRouter(
    tags=["Payment Methods"]
)

@router.post("/payment-apps/")
async def add_payment_app(data: dict = Body(...)):
    pass

@router.get("/payment-apps/")
async def get_payment_apps():
    pass

@router.post("/bank-accounts/")
async def add_bank_account(data: dict = Body(...)):
    pass

@router.get("/bank-accounts/")
async def get_bank_accounts():
    pass
