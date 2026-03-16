from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.interface.api.dashboard import router as dashboard_router
from backend.interface.api.indicator_result import router as indicator_result_router
from backend.interface.api.teacher_navigation_router import router as teacher_navigation_router
from backend.interface.api.teacher_dashboard_controller import router as teacher_dashboard_router


def create_app() -> FastAPI:
    app = FastAPI(title="Pedagogical OS")

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(dashboard_router)
    app.include_router(indicator_result_router)
    app.include_router(teacher_navigation_router, prefix="/teacher")
    app.include_router(teacher_dashboard_router)

    return app


app = create_app()