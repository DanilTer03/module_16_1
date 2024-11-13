from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main() -> dict:
    return {"message": "Главная страница"}


@app.get("/user")
async def user() -> dict:
    return {"message": "Информация о пользователе. Имя: <username>, Возраст: <age>"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/[{user_id}")
async def user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}