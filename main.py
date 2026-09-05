from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db_provider import get_db, engine
from models import Ticket, TicketStatus, Base
from schemas import TicketCreate, TicketResponse

app = FastAPI(title="Support Service")

# Зависимость для извлечения ID пользователя из заголовка шлюза
async def get_current_user_id(x_user_id: str = Header(None, alias="X-User-Id")):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Запрос должен идти через API Gateway (отсутствует X-User-Id)")
    return int(x_user_id)

@app.on_event("startup")
async def startup():
    # Создаем таблицы при старте (для простоты, в проде лучше использовать Alembic, как в Billing)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/tickets/", response_model=TicketResponse, status_code=201)
async def create_ticket(
    ticket_data: TicketCreate,
    user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    new_ticket = Ticket(
        user_id=user_id,
        subject=ticket_data.subject,
        message=ticket_data.message,
        status=TicketStatus.OPEN
    )
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket

@app.get("/tickets/", response_model=list[TicketResponse])
async def get_my_tickets(
    user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Ticket).where(Ticket.user_id == user_id).order_by(Ticket.created_at.desc())
    )
    return result.scalars().all()
