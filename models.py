from sqlalchemy import  Column, ForeignKey, Integer, String

from database import Base


class product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, unique=True, index=True)
    product_price= Column(Integer)

