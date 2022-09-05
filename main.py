from fastapi import FastAPI

from api import users

from db.db_setup import engine
from db.models import user

user.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Api Gateway",
    description="",
    version="0.0.1",
    terms_of_service="https://github.com/ieski",
    contact={
        "name": "ismail eski",
        "url": "https://github.com/ieski",
        "email": "ismaileski@gmail.com",
    },
    license_info={
        "name": "AGPL-3.0-only",
        "url": "https://www.gnu.org/licenses/agpl-3.0.tr.html",
    },
)

app.include_router(users.router, prefix="/api/v1")
