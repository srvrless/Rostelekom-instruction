from fastapi import FastAPI
from routes.main import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/", tags=["Welcome"])
async def welcome():
    return {"If you wanna go to the swagger, click: http://localhost:8000/docs"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
