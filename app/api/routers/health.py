from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():

    return {"status": True, "service": "Fast", "version": "1.0"}
