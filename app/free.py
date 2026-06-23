from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

router_p = APIRouter(tags=["Мои Роуты"])


@router_p.get("/test")
async def checkIN():
    return {"Detail": "API POEHALO"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Запуск_!!")
    yield
    print("Стоп_!!")


def create_api() -> FastAPI:
    jj = FastAPI(title="Заголовок АПИ", version="2.0", lifespan=lifespan)

    @jj.get("/", include_in_schema=False)
    async def redir_to_docs():
        return RedirectResponse(url="/docs")

    jj.include_router(router_p)
    return jj


yyy = create_api()
