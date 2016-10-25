# https://www.codementor.io/python/tutorial/understanding-sqlalchemy-cheat-sheet

class Parent(Base):
    __tablename__ = 'parent'
    id = ColumnColumn(Integer,Sequence('p_seq'),primary_key=True) 
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", backref=backref("parent", uselist=False)) # <------
    # child access parent does not use list

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer,Sequence('c_seq'),primary_key=True) 


