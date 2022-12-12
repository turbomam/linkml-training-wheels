from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a file-based SQLite database
engine = create_engine('sqlite:///sqlalchemy_ride.db', echo=True)

# Declare a base for our models
Base = declarative_base()


# Define a model class for our table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to use the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
user = User(name="Alice", email="alice@example.com")

# Add the user to the session
session.add(user)

# Save the changes to the database
session.commit()

# Print the ID of the new user
print(user.id)
