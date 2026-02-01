from db import DB

db = DB()


def run_test(name, payload):
    print(f"\nTEST: {name}")
    res = db.act(payload)
    print(res)


run_test(
    "Valid new user",
    {
        "task": "newUser",
        "data": {
            "student_id": "DEPLOY2026CSE001",
            "email": "deploy1@test.com",
            "name": "Deploy User"
        }
    }
)

run_test(
    "Duplicate student_id",
    {
        "task": "newUser",
        "data": {
            "student_id": "DEPLOY2026CSE001",
            "email": "deploy2@test.com"
        }
    }
)

run_test(
    "Duplicate email",
    {
        "task": "newUser",
        "data": {
            "student_id": "DEPLOY2026CSE002",
            "email": "deploy1@test.com"
        }
    }
)
run_test(
    "Missing student_id",
    {
        "task": "newUser",
        "data": {
            "email": "missing@test.com"
        }
    }
)
run_test(
    "Empty data",
    {
        "task": "newUser",
        "data": {}
    }
)
run_test(
    "No data key",
    {
        "task": "newUser"
    }
)

run_test(
    "Invalid task",
    {
        "task": "createUser",
        "data": {
            "student_id": "DEPLOY2026CSE003"
        }
    }
)
run_test(
    "Invalid data type",
    {
        "task": "newUser",
        "data": "this-should-be-a-dict"
    }
)
run_test(
    "Partial but valid",
    {
        "task": "newUser",
        "data": {
            "student_id": "DEPLOY2026CSE004"
        }
    }
)
