from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import schema
from database import SessionLocal, engine
import model
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

app = FastAPI()
model.Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def read_movies(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(Movie).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": records})

@app.get("/movie/{name}", response_class=HTMLResponse)
def read_movie(request: Request, name: schema.Movie.name, db: Session = Depends(get_database_session)):
    item = db.query(Movie).filter(Movie.id==name).first()
    print(item)
    return templates.TemplateResponse("overview.html", {"request": request, "movie": item})

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")