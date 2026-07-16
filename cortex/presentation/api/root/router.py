from fastapi import APIRouter

from cortex.shared.config import settings
from cortex import __version__
from cortex.presentation.api.root.response import RootResponse

router = APIRouter(tags=["Root"])


@router.get("/", response_model=RootResponse)
async def root() -> RootResponse:
    return RootResponse(
        name=settings.app_name,
        version=__version__,
        environment=settings.environment,
    )