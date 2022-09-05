from typing import Union, List
from uuid import UUID, uuid4
from fastapi import FastAPI, Path, Query, HTTPException

from models import User, Gender, Role, UserUpdateRequest


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


db: List[User] = [
    User(
        id=uuid4(),
        first_name="İsmail",
        last_name="Eski",
        gender=Gender.male,
        roles=[Role.admin],
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete(
    user_id: UUID = Path(..., description="The ID of the User you want to delete.")
):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"User with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(
    user_update: UserUpdateRequest,
    user_id: UUID = Path(..., description="The ID of the User you want to update."),
):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exists"
    )
