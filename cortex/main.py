from fastapi import FastAPI

from cortex.shared.logging import logger
from cortex.shared.logging import configure_logging
from cortex.presentation.api.health.router import router as health_router
from cortex.presentation.api.root.router import router as root_router


configure_logging()


app = FastAPI(
    title="Cortex API",
    version="0.1.0",
)


logger.info("application_started", application="cortex")

app.include_router(root_router)
app.include_router(health_router)