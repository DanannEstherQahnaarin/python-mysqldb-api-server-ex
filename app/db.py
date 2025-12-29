import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# 환경 변수에서 DB 접속 정보 로드. 기본값은 개발 환경 기준.
DB_HOST = os.getenv("DB_HOST", "localhost")     # 데이터베이스 호스트명
DB_PORT = os.getenv("DB_PORT", "3306")          # 데이터베이스 포트번호
DB_NAME = os.getenv("DB_NAME", "appdb")         # 데이터베이스 이름
DB_USER = os.getenv("DB_USER", "appuser")       # 데이터베이스 사용자명
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppw") # 데이터베이스 비밀번호

# SQLAlchemy에서 사용될 데이터베이스 URL 문자열 설정 (MySQL + PyMySQL 드라이버)
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    "?charset=utf8mb4"  # 한글 및 다양한 문자 지원을 위한 charset 설정
)

# SQLAlchemy 엔진 생성
# - pool_pre_ping=True: 연결이 끊겼는지 미리 점검하여 자동 재연결
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# 세션 팩토리 생성
# - autoflush=False: flush 동작을 수동으로 제어
# - autocommit=False: 명시적 커밋 필요
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 모든 모델 클래스가 상속받는 베이스 클래스 정의
class Base(DeclarativeBase):
    pass

# FastAPI Dependency로 사용될 DB 세션 제공 함수
# - yield 구문을 통해 세션을 반환
# - 사용 후 자동으로 세션 종료하여 리소스 누수 방지
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
