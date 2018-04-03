import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)  # 3期师兄
    extra = Column(Text, nullable=True)

    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'email'),
    )

class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    hobby_id = Column(Integer, ForeignKey("hobby.id"))


class b2g(Base):
    __tablename__ = 'b2g'
    id = Column(Integer, primary_key=True, autoincrement=True)
    girl_id = Column(Integer, ForeignKey('girl.id'))
    boy_id = Column(Integer, ForeignKey('boy.id'))


class Girl(Base):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Boy(Base):
    __tablename__ = 'boy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)



engine = create_engine(
    "mysql+pymysql://root@127.0.0.1:3306/school?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)





