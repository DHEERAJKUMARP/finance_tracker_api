from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/summary")
async def get_dashboard_summary():
    pass

@router.get("/outstanding")
async def get_dashboard_outstanding():
    pass

@router.get("/upcoming-emis")
async def get_dashboard_upcoming_emis():
    pass

@router.get("/loan-visualization")
async def get_dashboard_loan_visualization():
    pass
