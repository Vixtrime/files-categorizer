from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    Table,
)

from .meta import Base


class File(Base):
    __tablename__ = 'file'
    file_id = Column(Integer, primary_key=True)
    file_name = Column(Text, nullable=False)
    file_path = Column(Text, unique=True)
    file_category_id = Column(ForeignKey('category.category_id'))
