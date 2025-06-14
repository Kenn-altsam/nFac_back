from src.db import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

class AILog(Base):
    __tablename__ = "ai_logs"

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String)
    input_text = Column(String)
    output_text = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
