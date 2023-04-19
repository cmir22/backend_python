
### Main file ###

from fastapi import FastAPI
from api.users import users
from api.admin import admins
from api.places import places
# from security.jwt_valiator import valikdate_jwt

app = FastAPI()

# app.middleware("http")(validate_jwt)

# Routers
app.include_router(users.router)
app.include_router(admins.router)
app.include_router(places.router)
