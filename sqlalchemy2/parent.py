from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
# https://www.codementor.io/python/tutorial/understanding-sqlalchemy-cheat-sheet
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer,primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", backref=backref("parent", uselist=False)) # <------
    # child access parent does not use list

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer,primary_key=True)
 
from sqlalchemy import create_engine
# engine = create_engine('sqlite:///orm_in_detail.sqlite')
engine = create_engine('mysql://root:@localhost:3306/test', echo=True)
 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)

Base.metadata.create_all(engine)
session = Session()


a_parent = Parent()
a_child = Child()

a_parent.child = a_child

session.add(a_parent)
session.commit()

print a_child.id
print a_child.parent.id

# session.delete(a_child)
# session.delete(a_parent)
# session.commit()

