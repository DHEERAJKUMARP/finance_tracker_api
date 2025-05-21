from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/integrations",
    tags=["Payment Integration"]
)

@router.post("/bank-link")
async def link_bank_account(data: dict = Body(...)):
    pass

@router.post("/pay-bill")
async def pay_bill(data: dict = Body(...)):
    pass
