from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/transactions",
    tags=["Transaction History"]
)

@router.get("/")
async def get_all_transactions():
    pass

@router.get("/filter")
async def filter_transactions(
    start_date: str = Query(None),
    end_date: str = Query(None),
    category: str = Query(None),
    min_amount: float = Query(None),
    max_amount: float = Query(None),
):
    pass

@router.get("/search")
async def search_transactions(
    keyword: str = Query(...)
):
    pass

@router.get("/export")
async def export_transactions(
    type: str = Query(..., regex="^(csv|pdf)$")
):
    pass
