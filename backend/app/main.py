from fastapi import FastAPI

from backend.interface.api.dashboard import router as dashboard_router


def create_app() -> FastAPI:
    """
    Application factory.

    Keeps app creation explicit and testable.
    """
    app = FastAPI(title="Pedagogical OS")

    app.include_router(dashboard_router)

    return app


app = create_app()
