from fastapi import FastAPI, Form, APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.responses import HTMLResponse
import psycopg2
from sqlalchemy import func
from sqlalchemy.orm import Session
from Database import get_db
import models
from typing import List

routers = APIRouter(
    tags=['Users'],
)



@routers.post("/login")
async def login(email: str = Form(...), password: str = Form(...), db:Session = Depends(get_db)):

    User = db.query(models.Customer).filter(func.lower(models.Customer.email) == func.lower(email.strip())).first()

    if not User:
        return HTMLResponse("""
        <script>
            alert("User does not exist, Sign Up first!");
            window.location.href = '/static/Register.html';
        </script>
        """, status_code=200)
    
    if password != User.password:
        return HTMLResponse("""
        <script>
            alert("Wrong Email or Password!! Try Again");
            window.location.href = '/static/index.html';
        </script>
        """, status_code=200)
    
    return HTMLResponse("""
    <script>
        alert("You have successfully logged in");
        window.location.href = '/static/book.html';
    </script>
    """, status_code=200)

    


# <?php
# session_start();
# if(isset($_POST['login']))
# {
    
#     $emailid=$_POST['email'];
#     $pass=$_POST['pass'];
    
#     $con=mysqli_connect('127.0.0.1','root','','car_rent');
#     if($con==false)
#     {
#         echo "Error in connection";
#     }
#     else
#     {
#         $select="SELECT * FROM `Sign_in` WHERE `emailid`='$emailid'  AND `password`='$pass'";
#         $query=mysqli_query($con,$select);
#         $row=mysqli_num_rows($query);
#         if($row)
#         {
#             $data=mysqli_fetch_assoc($query);
#             $_SESSION['name']=$data['name'];
#             ?>
#             <script>
#                 alert("You have successfully logged in");
#                 window.open('book.html','_self');
#             </script>
#             <?php
#         }
#         else
#         {
#             ?>
#             <script>
#                 alert("Wrong Emailid and Password!! Try Again");
#                 window.open('index.html','_self');
#             </script>
#             <?php
#         }
        
#     }
# }
# ?>
