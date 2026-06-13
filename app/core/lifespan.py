from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):
    print("Application startup")

    app.state.service_name = "Document Analyzer Service"
    app.state.version = "1.0.0"

    yield

    print("Application shutdown")