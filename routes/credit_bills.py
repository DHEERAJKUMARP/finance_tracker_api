from fastapi import APIRouter, Body, Path

router = APIRouter(
    prefix="/credit-bills",
    tags=["Credit Card Bills"]
)

@router.post("/")
async def create_credit_bill(data: dict = Body(...)):
    pass

@router.get("/")
async def get_credit_bills():
    pass

@router.put("/{id}/mark-paid")
async def mark_credit_bill_paid(id: int = Path(...)):
    pass
