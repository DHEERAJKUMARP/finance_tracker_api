from fastapi import APIRouter, Body, Path

router = APIRouter(
    prefix="/loans",
    tags=["Loans & EMI"]
)

@router.post("/")
async def create_loan(data: dict = Body(...)):
    pass

@router.get("/")
async def get_loans():
    pass

@router.put("/{id}/add-emi")
async def add_emi_to_loan(id: int = Path(...), data: dict = Body(...)):
    pass

@router.put("/{id}/mark-emi-paid")
async def mark_emi_paid(id: int = Path(...)):
    pass

@router.get("/{id}/balance")
async def get_loan_balance(id: int = Path(...)):
    pass

@router.get("/upcoming-emis")
async def get_upcoming_emis():
    pass
