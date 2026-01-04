import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ApiTube",
    description="YouTube Transcript and Analytics API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: update in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main() -> None:
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=os.getenv("PORT", 8000),
        reload=True
    )


if __name__ == "__main__":
    main()
