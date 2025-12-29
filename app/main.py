from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from .db import Base, engine, get_db
from .models import Employee
from .schemas import EmployeeOut
from typing import List

app = FastAPI(title="MySQL API Server")

@app.on_event("startup")
def on_startup():
    # 테이블 자동 생성 (튜토리얼용)
    Base.metadata.create_all(bind=engine)

    # 샘플 데이터 자동 삽입(없을 때만)
    with engine.begin() as conn:
        result = conn.execute(select(Employee).limit(1)).first()
        if result is None:
            conn.execute(
                Employee.__table__.insert(),
                [
                    {"name": "Alice", "role": "Developer"},
                    {"name": "Bob", "role": "Manager"},
                ],
            )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/employees", response_model=List[EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    rows = db.execute(select(Employee).order_by(Employee.id)).scalars().all()
    return rows
