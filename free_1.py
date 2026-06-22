from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from fastapi.responses import RedirectResponse

router = APIRouter(tags=['My_Routs'])

@router.get('/test')
async def checkes():
    return {
        'Test_api' : 'POGNALI'
    }

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting!')
    yield
    print('Stopping!!')

def create_app() -> FastAPI:
    dd = FastAPI(
        title='My_API',
        version='4.3',
        lifespan=lifespan
    )

    @dd.get('/', include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse('/docs')

    dd.include_router(router)
    return dd

lj = create_app()