from fastapi import FastAPI, Form, APIRouter, Depends
from fastapi.responses import HTMLResponse
import psycopg2
from Database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
import models

routers = APIRouter(
    tags=['UsersRegister'],
)

@routers.post("/register", response_class=HTMLResponse)
async def register(
    name: str = Form(...),
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    repeatpass: str = Form(...),
    db:Session = Depends(get_db)
):
    if password != repeatpass:
        return HTMLResponse("""
        <script>
            alert("Passwords do not match!");
            window.location.href = '/static/Register.html';
        </script>
        """, status_code=200)


    User = db.query(models.Customer).filter(models.Customer.email==email).first()

    if User:
        return HTMLResponse(
            content=f"""
            <script>
                alert("Email already exists! Register with different email");
                window.location.href = '/static/Register.html';
            </script>
            """,
            status_code=200
        )
    
    User_new = models.Customer(name = name, password=password, email=email, username=username)
    db.add(User_new)
    db.commit()
    db.refresh(User_new)

    return HTMLResponse(
        content=f"""
        <script>
            alert("Registered Successfully");
            window.location.href = '/';
        </script>
        """,
        status_code=200
    )

