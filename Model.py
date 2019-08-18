from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DECIMAL


class Type(Base):
    # 表名称
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(length=255), nullable=False)
    type_url = Column(String(length=255), nullable=False)


class Anchor(Base):
    # 表名称
    __tablename__ = 'anchor'

    anchor_type_id = Column(Integer, primary_key=True, autoincrement=True)
    anchor_type = Column(String(length=255), nullable=True)
    anchor_name = Column(String(length=255), nullable=True)
    anchor_id = Column(Integer, nullable=True)
    anchor_follow = Column(Integer, nullable=True)
    anchor_url = Column(String(length=255), nullable=True)


class Fans(Base):
    # 表名称
    __tablename__ = 'fans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fan_follow_id = Column(Integer, nullable=True)
    fan_name = Column(String(length=255), nullable=True)
    fan_pirce = Column(Integer, nullable=True)
    rmb = Column(DECIMAL, nullable=True)


class Proxy(Base):
    # 表名称
    __tablename__ = 'zmproxy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    proxy = Column(String(length=255), nullable=True)

