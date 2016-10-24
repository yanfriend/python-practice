from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Sequence,
    Float
)
import datetime

from sqlalchemy import create_engine
engine = create_engine('mysql://root:@localhost:3306/test', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
DBSession = Session()

Base = declarative_base()

class Book(Base):  #<------------------------- 
    __tablename__  = "books"    #matches the name of the actual database table
    id             = Column(Integer,Sequence('book_seq'),primary_key=True) # plays nice with all major database engines
    name           = Column(String(50))                                    # string column need lengths
    author_id      = Column(Integer,ForeignKey('authors.id'))              # assumes there is a table in the database called 'authors' that has an 'id' column
    price          = Column(Float)
    date_added     = Column(DateTime, default=datetime.datetime.now)       # defaults can be specified as functions
    promote        = Column(Boolean,default=False)                         #     or as values


#fetch everything
lBooks = DBSession.query(Book)  #returns a Query object. 
for oBook in lBooks:
    print oBook.name

#simple filters
lBooks = DBSession.query(Book).filter_by(author_id=1) #returns all the books for a specific author

#more complex filters
lBooks = DBSession.query(Book).filter(Book.price<20) #returns all the books with price <20. Note we use filter, not filter_by

#filters can be combined
lBooks = DBSession.query(Book).filter_by(author_id=1).filter(Book.price<20) #all books by a specific author, with price<20

#logical operations can be used in filters
from sqlalchemy import or_
lBooks = DBSession.query(Book).filter(or_(Book.price<20,promote==True)) # returns all books  that cost less than 20 OR are being promoted

#ordering
from sqlalchemy import desc
DBSession.query(Book).order_by(Book.price) #get all books ordered by price
DBSession.query(Book).order_by(desc(Book.price)) #get all books ordered by price descending

#other useful things
DBSession.query(Book).count() #returns the number of books
DBSession.query(Book).offset(5) #offset the result by 5
DBSession.query(Book).limit(5) # return at most 5 books
DBSession.query(Book).first() #return the first book only or None
DBSession.query(Book).get(8) #return the Book with primary key = 8, or None 
