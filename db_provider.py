from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from settings import settings
from logging import getLogger

logger = getLogger("db_provider")
logger.setLevel("INFO")

engine = create_async_engine(settings.DATABASE_URL)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session