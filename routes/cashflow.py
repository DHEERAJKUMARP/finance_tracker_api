from fastapi import APIRouter

router = APIRouter(
    prefix="/cashflow",
    tags=["Net Cash Flow & Savings"]
)

@router.get("/net-balance")
async def get_net_balance():
    pass

@router.get("/summary-chart")
async def get_summary_chart():
    pass
