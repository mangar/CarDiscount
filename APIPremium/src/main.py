import logging

from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import classification_consulting

from helpers.log import AppLogger

API_KEY = "MINHA_CHAVE_SECRETA"
PRIVATE_ROUTES = [
    "/premium_consulting"
]

AppLogger.init(log_level="DEBUG", log_file="logs/app.log")




class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # if any(request.url.path.startswith(r) for r in ROTAS_PROTEGIDAS):
        if any(request.url.path.startswith(r) for r in PRIVATE_ROUTES):
            chave = request.headers.get("Authorization")
            if chave != API_KEY:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Acesso não autorizado. Chave inválida ou ausente."},
                )
            

        response = await call_next(request)
        return response



app = FastAPI()
app.add_middleware(APIKeyMiddleware)


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!!!!!"}

app.include_router(classification_consulting.router, prefix="/classification_consulting", tags=["ClassificationConsulting"])


