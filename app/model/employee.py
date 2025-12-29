from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base

# ==========================================================
# Employee 테이블 스키마 정의
# - 사원 정보 관리 목적
# ----------------------------------------------------------
# 컬럼 설명:
#   id   : 사원 고유 번호 (PK, 자동 증가)
#   name : 사원 이름 (최대 100자, 필수)
#   role : 사원 직책 (최대 100자, 필수)
# ==========================================================

# (테이블 스키마 작성법 참고)
# class YourModel(Base):
#     __tablename__ = "your_table"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     column_name: Mapped[str] = mapped_column(String(길이), nullable=False)
#     ...
# ----------------------------------------------------------

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True, 
        doc="사원 고유 번호 (PK, 자동 증가)"
    )
    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False, 
        doc="사원 이름 (최대 100자, 필수)"
    )
    role: Mapped[str] = mapped_column(
        String(100), 
        nullable=False, 
        doc="사원 직책 (최대 100자, 필수)"
    )
