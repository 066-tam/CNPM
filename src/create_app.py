from fastapi import FastAPI
from .config import settings
from .app_logging import configure_logging
from .cors import setup_cors
from .infrastructure.databases.base import init_engine, Base
from .api.schemas.swagger import get_openapi_overrides
from .api.controllers.todo_controller import router as todo_router
from .api.controllers.user_controller import router as user_router
from .api.controllers.course_controller import router as course_router

def create_app() -> FastAPI:
    logger = configure_logging()
    app = FastAPI(title=settings.app_name)
    setup_cors(app)

    # DB init
    engine = init_engine(settings.database_url)
    Base.metadata.create_all(bind=engine)

    # Routers
    app.include_router(user_router, prefix="/api/users", tags=["users"])
    app.include_router(todo_router, prefix="/api/todos", tags=["todos"])
    app.include_router(course_router, prefix="/api/courses", tags=["courses"])

    # OpenAPI override (optional)
    overrides = get_openapi_overrides()
    if overrides:
        app.openapi_schema = overrides

    logger.info("App initialized")
    return app
