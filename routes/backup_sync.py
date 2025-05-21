from fastapi import APIRouter, Body

router = APIRouter(
    tags=["Backup & Sync"]
)

@router.post("/backup/")
async def create_backup(data: dict = Body(...)):
    pass

@router.post("/sync/")
async def sync_data(data: dict = Body(...)):
    pass
