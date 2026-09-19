def create_user(user):
    if user.age < 18:
        return {"error": "User must be 18 or older"}

    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }