from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.post("/settings")
async def update_notification_settings(settings: dict = Body(...)):
    pass

@router.get("/")
async def get_notifications():
    pass

@router.get("/budget-alerts")
async def get_budget_alerts():
    pass
