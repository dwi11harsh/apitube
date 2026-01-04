from .health import router as health_router

health = type("Module", (), {"router": health_router})

__all__ = ["health"]
