import os
from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import hashlib

# Load environment variables
load_dotenv()

# Database setup from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", 
                        f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'postgres')}@"
                        f"{os.getenv('POSTGRES_HOST', 'db')}:{os.getenv('POSTGRES_PORT', '5432')}/"
                        f"{os.getenv('POSTGRES_DB', 'auth_db')}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

# Add initial user
def add_initial_user():
    db = SessionLocal()
    
    # Check if user already exists
    existing_user = db.query(User).filter(User.username == "johndoe").first()
    if existing_user:
        print("⚠️  Initial user already exists")
        return
    
    # Create initial user
    initial_user = User(
        username="johndoe",
        full_name="John Doe",
        email="johndoe@example.com",
        hashed_password=hashlib.sha256("secret".encode()).hexdigest(),
        disabled=False
    )
    
    db.add(initial_user)
    db.commit()
    db.refresh(initial_user)
    print("✅ Initial user created successfully!")
    db.close()

if __name__ == "__main__":
    init_db()
    add_initial_user()
