from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

    smtp_email = Column(String, nullable=True)
    smtp_password = Column(String, nullable=True)
