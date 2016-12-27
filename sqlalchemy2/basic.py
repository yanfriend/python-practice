# 1, Connect to the mydb database:
from sqlalchemy import create_engine
engine = create_engine('mysql://root:@localhost:3306/test', echo=True)

# 2,  Define the models class mapper:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class MyTable(Base):
        __tablename__ = 'mytable'

        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        value = Column(String(100))

        def __init__(self, name, value):
                self.name = name
                self.value = value

        def __repr__(self):
                return "<MyTable(%s, %s)>" % (self.name, self.value)

Base.metadata.create_all(engine)

# 3,  Call the session which bind the db engine to manipulate the database:
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# 4, add, query and delete
new_record = MyTable('Genius', 'me')
session.add(new_record)
session.commit()

list_of_records = [MyTable('Genius', 'me'), MyTable('Super', 'me')]
session.add_all(list_of_records)
session.commit()

records = session.query(MyTable).filter_by(name='Genius')
all_records = session.query(MyTable).all()

records_to_delete = session.query(MyTable).filter_by(name='Super')
for record in records_to_delete:
        session.delete(record)
session.commit()
