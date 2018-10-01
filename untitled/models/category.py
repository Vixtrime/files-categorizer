from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(Text, nullable=False)
