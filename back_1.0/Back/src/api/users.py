from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src import models, database  # ✅ absolute import
from src.auth import get_current_user, create_access_token  # ✅ your question
from src.schemas.users import UserCreate, UserRead, UserUpdate  # ✅ user schemas
from src.schemas.auth import LoginRequest, TokenResponse  # ✅ for login schema
from passlib.context import CryptContext


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.users.User).filter(models.users.User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def get_me(current_user: models.users.User = Depends(get_current_user)):
    return current_user

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.users.User).filter(models.users.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    db_user = models.users.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# PUT http://127.0.0.1:8000/users/1
# {
#   "username": "newname",
#   "email": "newemail@example.com",
#   "password": "newpass123"
# }
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if updates.username:
        user.username = updates.username
    if updates.email:
        user.email = updates.email
    if updates.password:
        user.hashed_password = hash_password(updates.password)

    db.commit()
    db.refresh(user)
    return user

# DELETE http://127.0.0.1:8000/users/1
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": f"User {user_id} deleted"}
