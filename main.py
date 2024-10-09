import random
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

roles = ['p', 'p', 'm', 'm']
roles_count = len(roles)

@app.get("/role/")
def read_games():
    print(roles)
    if not roles:
        return "Закончились роли"
    return roles.pop(random.randrange(len(roles))), roles_count

@app.post("/roles/{mafia_count}/{peace_count}")
def set_roles(mafia_count: int, peace_count: int):
    roles = 'm' * mafia_count + 'p' * peace_count
    roles_count = len(roles)
    return 'ok'
