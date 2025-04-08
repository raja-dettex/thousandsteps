from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
import ssl
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

engine = create_async_engine('postgresql+asyncpg://neondb_owner:npg_qWcZyeGgua21@ep-red-union-a44wyiep-pooler.us-east-1.aws.neon.tech/thousandsteps', echo=True, connect_args = { "ssl": ssl_context})

sessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, autoflush=True, expire_on_commit=False)
Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with  sessionLocal() as session:
        print(session)
        yield session
