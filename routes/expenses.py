from fastapi import APIRouter, Body, Path, Query

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post("/")
async def create_expense(data: dict = Body(...)):
    pass

@router.get("/")
async def get_expenses(month: str = Query(None, description="Filter expenses by month YYYY-MM")):
    pass

@router.get("/{id}")
async def get_expense(id: int = Path(...)):
    pass

@router.put("/{id}")
async def update_expense(id: int = Path(...), data: dict = Body(...)):
    pass

@router.delete("/{id}")
async def delete_expense(id: int = Path(...)):
    pass

@router.post("/{id}/attach-receipt")
async def attach_receipt(id: int = Path(...), data: dict = Body(...)):
    pass

@router.post("/{id}/set-recurring")
async def set_recurring_expense(id: int = Path(...), data: dict = Body(...)):
    pass

@router.get("/summary-by-category")
async def get_expense_summary_by_category():
    pass
