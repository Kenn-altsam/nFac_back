from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))  # если у книги есть "владелец"
