from fastapi import APIRouter, Body

router = APIRouter(
    tags=["Sharing"]
)

@router.post("/reports/share")
async def share_report(data: dict = Body(...)):
    """Share a report with others."""
    pass

@router.post("/profiles/")
async def create_profile(data: dict = Body(...)):
    """Create a user profile for sharing or collaboration."""
    pass

@router.get("/profiles/")
async def get_profiles():
    """Get list of all profiles."""
    pass
