from fastapi import APIRouter

from cortex.presentation.api.health.response import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="healthy")