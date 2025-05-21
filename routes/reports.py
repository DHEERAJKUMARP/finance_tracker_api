from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/reports",
    tags=["Reports & Analytics"]
)

@router.get("/expenses")
async def get_expense_report():
    pass

@router.get("/income")
async def get_income_report():
    pass

@router.get("/net-cashflow")
async def get_net_cashflow_report():
    pass

@router.get("/compare-months")
async def compare_monthly_reports():
    pass

@router.get("/download")
async def download_report(type: str = Query(..., regex="^(csv|pdf)$")):
    pass
