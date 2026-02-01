from db import DB, DBError


def run_tests():
    try:
        db = DB()
        print("Connected to MongoDB")

        print("\nSTUDENT TESTS")

        student_data = {
            "student_id": "TEST2026CSE001",
            "college_id": "COL001",
            "name": "Test Student",
            "pfp": "",
            "email": "test@student.edu",
            "phone": "+911234567890",
            "branch": "CSE",
            "section": "A",
            "sem": 7,
            "cgpa": 8.5,
            "backlogs": 0,
            "skills": [
                {"name": "Python", "level": "advanced"},
                {"name": "Flask", "level": "intermediate"}
            ],
            "placement": {"status": 0}
        }

        sid = db.insert_student(student_data)
        print(f"Student inserted: {sid}")

        student = db.find_student({"student_id": "TEST2026CSE001"})
        print("Student fetched:", student)

        updated = db.update_student(
            {"student_id": "TEST2026CSE001"},
            {"cgpa": 8.8}
        )
        print(f"Student updated: {updated}")

        deleted = db.delete_student(
            {"student_id": "TEST2026CSE001"},
            soft=True
        )
        print(f"Student soft-deleted: {deleted}")

        print("\n--- RECRUITER TESTS ---")

        recruiter_data = {
            "company_name": "TestCorp",
            "recruiter_name": "Test HR",
            "recruiter_email": "hr@testcorp.com",
            "recruiter_phone": "+919999999999",
            "role": "hr",
            "company_type": "startup",
            "industry": "software",
            "work_mode": "remote",
            "eligibility": {
                "branches_allowed": ["CSE", "IT"],
                "min_cgpa": 7.5,
                "max_backlogs": 0,
                "allowed_semesters": [7, 8],
                "required_skills": ["Python"]
            }
        }

        rid = db.insert_recruiter(recruiter_data)
        print(f"Recruiter inserted: {rid}")

        recruiter = db.find_recruiters({"company_name": "TestCorp"})
        print("Recruiter fetched:", recruiter)

        updated = db.update_recruiter(
            {"company_name": "TestCorp"},
            {"work_mode": "hybrid"}
        )
        print(f"Recruiter updated: {updated}")

        deleted = db.delete_recruiter(
            {"company_name": "TestCorp"},
            soft=True
        )
        print(f"Recruiter soft-deleted: {deleted}")

        print("\nALL TESTS PASSED")

    except DBError as e:
        print("DB ERROR:", e)

    except Exception as e:
        print("UNEXPECTED ERROR:", e)


if __name__ == "__main__":
    run_tests()
