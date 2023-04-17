from fastapi import FastAPI
from derivation.ProfileModel import Profile

app = FastAPI()

obj = {
    "email_id": "test@gmail.com"
}

@app.get("/users/emails")
async def read_user_me(email_id: str, profile: Profile):
    profile.id = email_id
    return profile


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    profile = Profile()
    return {"user_id": user_id, "crdtn": profile.credit_card_no}