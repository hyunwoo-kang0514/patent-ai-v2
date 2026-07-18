"""
This file is the main entry point for PatenAI OA API - FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "PatentAI OA API", description = "OA first response + Pattern report + Search")

app.add_middleware(
    CORSMiddleware,
    # a code that only allows requets from this frontend origin
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    # 쿠키를 다 보내도 허용한다
    allow_credentials=True,
    # 어떤 메서드든 허용한다
    allow_methods=["*"],
    # 어떤 헤더든 허용한다
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}