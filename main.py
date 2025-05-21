from fastapi import FastAPI

app = FastAPI(
    title="Finance Management API",
    description="API for managing personal finance, lending, borrowing, loans, payments, reports, and more.",
    version="1.0.0",
)

# Import routers (adjust imports based on your folder structure)
from routes.user_management import router as user_management_router
from routes.expenses import router as expenses_router
from routes.transactions import router as transactions_router
from routes.tax import router as tax_router
from routes.sharing import router as sharing_router
from routes.settings import router as settings_router
from routes.reports import router as reports_router
from routes.payment_methods import router as payment_methods_router
from routes.payment_integrations import router as payment_integrations_router
from routes.notifications import router as notifications_router
from routes.loans_emi import router as loans_emi_router
from routes.lending_borrowing import router as lending_borrowing_router
from routes.income import router as income_router
from routes.dashboard import router as dashboard_router
from routes.credit_bills import router as credit_bills_router
from routes.cashflow import router as cashflow_router
from routes.backup_sync import router as backup_sync_router

include_routers = [
    user_management_router,
    expenses_router,
    transactions_router,
    tax_router,
    sharing_router,
    settings_router,
    reports_router,
    payment_methods_router,
    payment_integrations_router,
    notifications_router,
    loans_emi_router,
    lending_borrowing_router,
    income_router,
    dashboard_router,
    credit_bills_router,
    cashflow_router,
    backup_sync_router
]

for router in include_routers:
    app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to your FastAPI app!"}
