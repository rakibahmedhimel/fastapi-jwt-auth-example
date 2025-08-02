# FastAPI JWT Authentication Example

This is a minimal FastAPI project demonstrating user authentication using JWT tokens.

## 🔐 Features
- Register new users
- Login with JWT token
- Access a protected route using Bearer Token

## 🧪 Tested With
- Postman

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/rakibahmedhimel/fastapi-jwt-auth-example.git
cd fastapi-jwt-authentication
```

2. Create virtual environment and activate:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the API:
uvicorn app.main:app --reload

📂 Folder Structure
app/main.py – FastAPI entry point

routers/auth.py – Register/Login/Protected routes

oauth2.py – JWT token creation & verification

models.py – SQLAlchemy models

schemas.py – Pydantic schemas

database.py – DB engine and session

hashing.py – Password hashing

📸 Screenshots


📎 Author
Rakib Ahmed Himel
LinkedIn


🏷️ Tags
#fastapi #jwt #backenddevelopment #authentication