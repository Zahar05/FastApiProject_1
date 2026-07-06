from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():

    return {"status": True, "service": "FastAPI", "version": "1.0.0"}
