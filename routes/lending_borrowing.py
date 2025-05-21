from fastapi import APIRouter, Body, Path

router = APIRouter(
    tags=["Lending & Borrowing"]
)

@router.post("/lending/")
async def create_lending(data: dict = Body(...)):
    pass

@router.post("/borrowing/")
async def create_borrowing(data: dict = Body(...)):
    pass

@router.get("/lending/")
async def get_lending():
    pass

@router.get("/borrowing/")
async def get_borrowing():
    pass

@router.put("/lending/{id}/mark-returned")
async def mark_lending_returned(id: int = Path(...)):
    pass

@router.put("/borrowing/{id}/mark-paid")
async def mark_borrowing_paid(id: int = Path(...)):
    pass

@router.get("/lending-borrowing/outstanding")
async def get_outstanding_lending_borrowing():
    pass
