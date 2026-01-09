from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

    sender_email = Column(String, nullable=True)
    brevo_login = Column(String, nullable=True)
    brevo_password = Column(String, nullable=True)
