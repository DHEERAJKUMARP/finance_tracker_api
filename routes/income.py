from fastapi import APIRouter, Body, Path

router = APIRouter(
    prefix="/income",
    tags=["Income"]
)

@router.post("/")
async def add_income(data: dict = Body(...)):
    pass

@router.get("/")
async def get_income():
    pass

@router.get("/summary")
async def get_income_summary():
    pass

@router.post("/{id}/attach-file")
async def attach_file_to_income(id: int = Path(...)):
    pass
