from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://minhacarteirapoc.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "O meu também é Beth"}

handler = Mangum(app=app)