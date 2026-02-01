from pymongo import MongoClient, errors
from datetime import datetime, timezone
import uuid

"""
Student:
  student_id: ""          # e.g. "2022CSE045" (UNIQUE)
  pfp: ""                 # /uploads/pfps/student_id.jpg
  college_id: ""          # internal college ERP id
  name: ""
  email: ""               # institutional / personal
  phone: ""               # string, includes country code

  branch: ""              # ENUM ↓
    # ["CSE", "IT", "ECE", "EEE", "ME", "CE", "AI", "DS"]

  section: ""             # optional, e.g. "A", "B", "C"

  sem: 0                  # ENUM ↓
    # [1,2,3,4,5,6,7,8]

  cgpa: 0.0               # float (0.0 – 10.0)
  backlogs: 0             # integer ≥ 0

  skills: [
    {
      name: "",            # e.g. "Python", "React", "DSA"
      level: ""            # ENUM ↓
        # ["beginner", "intermediate", "advanced"]
    }
  ]

  projects: [
    {
      title: "",
      description: "",
      tech: [
        ""                 # e.g. "Python", "Flask", "MongoDB", "React"
      ],
      link: ""             # GitHub / demo link
    }
  ]

  internships: [
    {
      company: "",
      role: "",
      duration_months: 0,  # integer
      stipend: 0           # monthly stipend
    }
  ]

  achievements: [
    {
      title: "",
      year: 0,
      level: ""            # ENUM ↓
        # ["college", "inter-college", "state", "national", "international"]
    }
  ]

  resume_url: ""           # cloud / local hosted
  portfolio_url: ""
  github_url: ""
  linkedin_url: ""

  placement:
    status: 0              # ENUM ↓
      # 0 -> open
      # 1 -> applied
      # 2 -> shortlisted
      # 3 -> interview
      # 4 -> offered
      # 5 -> placed
      # 6 -> rejected

    company: ""            # company name if applicable
    package_lpa: 0.0
    offer_type: ""         # ENUM ↓
      # ["intern", "fte", "ppo"]

  created_at: new Date()
  updated_at: new Date()
  is_active: true          # soft delete / eligibility toggle
"""
"""
Recruiter:
  recruiter_id: ""        # UNIQUE (auto / uuid)
  company_name: ""

  recruiter_name: ""
  recruiter_email: ""
  recruiter_phone: ""

  role: ""                # ENUM ↓
    # ["hr", "tech-hr", "recruiter", "admin"]

  company_type: ""        # ENUM ↓
    # ["startup", "mnc", "service", "product", "govt"]

  industry: ""            # ENUM ↓
    # ["software", "hardware", "finance", "consulting",
    #  "core-engineering", "analytics", "ai-ml", "other"]

  website: ""
  linkedin_page: ""

  hiring_roles: [
    ""                     # ENUM ↓
      # ["sde", "frontend", "backend", "fullstack",
      #  "data-scientist", "ml-engineer",
      #  "devops", "analyst", "core-engineer"]
  ]

  locations: [
    ""                     # e.g. "Bangalore", "Pune", "Remote"
  ]

  work_mode: ""           # ENUM ↓
    # ["onsite", "remote", "hybrid"]

  eligibility:
    branches_allowed: [
      ""                   # same enum as student.branch
        # ["CSE", "IT", "ECE", "EEE", "ME", "CE", "AI", "DS", "OTHER: "]
    ]

    min_cgpa: 0.0
    max_backlogs: 0

    allowed_semesters: [
      0                    # ENUM ↓
        # [5,6,7,8]
    ]

    required_skills: [
      ""                   # e.g. "Python", "DSA", "React"
    ]

  is_active: true

  created_at: new Date()
  updated_at: new Date()
"""


class DBError(Exception):
    pass

class DB:
    def __init__(self):
        try:
            self.client = MongoClient(
                "mongodb://localhost:27017/",
                serverSelectionTimeoutMS=3000
            )
            self.client.server_info()  # force connection check

            self.db = self.client.placement_db
            self.students = self.db.students
            self.recruiters = self.db.recruiters

        except errors.ServerSelectionTimeoutError:
            raise DBError("MongoDB server not reachable")


    def insert_student(self, data: dict):
        try:
            data.setdefault("created_at", datetime.now(timezone.utc))
            data.setdefault("updated_at", datetime.now(timezone.utc))
            data.setdefault("is_active", True)

            return self.students.insert_one(data).inserted_id

        except errors.DuplicateKeyError:
            raise DBError("Student already exists")

        except errors.PyMongoError as e:
            raise DBError(f"Insert student failed: {str(e)}")

    def find_students(self, query: dict = {}, projection: dict = {"_id": 0}):
        try:
            return list(self.students.find(query, projection))
        except errors.PyMongoError as e:
            raise DBError(f"Fetch students failed: {str(e)}")

    def find_student(self, query: dict, projection: dict = {"_id": 0}):
        try:
            return self.students.find_one(query, projection)
        except errors.PyMongoError as e:
            raise DBError(f"Fetch student failed: {str(e)}")

    def update_student(self, query: dict, new_data: dict):
        try:
            new_data["updated_at"] = datetime.now(timezone.utc)
            result = self.students.update_one(query, {"$set": new_data})

            if result.matched_count == 0:
                raise DBError("Student not found")

            return result.modified_count

        except errors.PyMongoError as e:
            raise DBError(f"Update student failed: {str(e)}")

    def delete_student(self, query: dict, soft: bool = True):
        try:
            if soft:
                return self.update_student(query, {"is_active": False})

            result = self.students.delete_one(query)
            if result.deleted_count == 0:
                raise DBError("Student not found")

            return result.deleted_count

        except errors.PyMongoError as e:
            raise DBError(f"Delete student failed: {str(e)}")


    def insert_recruiter(self, data: dict):
        try:
            data.setdefault("recruiter_id", str(uuid.uuid4()))
            data.setdefault("created_at", datetime.now(timezone.utc))
            data.setdefault("updated_at", datetime.now(timezone.utc))
            data.setdefault("is_active", True)

            return self.recruiters.insert_one(data).inserted_id

        except errors.PyMongoError as e:
            raise DBError(f"Insert recruiter failed: {str(e)}")

    def find_recruiters(self, query: dict = {}, projection: dict = {"_id": 0}):
        try:
            return list(self.recruiters.find(query, projection))
        except errors.PyMongoError as e:
            raise DBError(f"Fetch recruiters failed: {str(e)}")

    def find_recruiter(self, query: dict, projection: dict = {"_id": 0}):
        try:
            return self.recruiters.find_one(query, projection)
        except errors.PyMongoError as e:
            raise DBError(f"Fetch recruiter failed: {str(e)}")

    def update_recruiter(self, query: dict, new_data: dict):
        try:
            new_data["updated_at"] = datetime.now(timezone.utc)
            result = self.recruiters.update_one(query, {"$set": new_data})

            if result.matched_count == 0:
                raise DBError("Recruiter not found")

            return result.modified_count

        except errors.PyMongoError as e:
            raise DBError(f"Update recruiter failed: {str(e)}")

    def delete_recruiter(self, query: dict, soft: bool = True):
        try:
            if soft:
                return self.update_recruiter(query, {"is_active": False})

            result = self.recruiters.delete_one(query)
            if result.deleted_count == 0:
                raise DBError("Recruiter not found")

            return result.deleted_count

        except errors.PyMongoError as e:
            raise DBError(f"Delete recruiter failed: {str(e)}")

    def handle_login(self, data):
        email = data.get("email")
        password = data.get("password")
        
        student = self.find_student({"email": email})
        if student:
            if self.verify_password(password, student.get("password")):
                del student["password"]
                return {"status": "ok", "role": "student", "data": student}
        
        recruiter = self.find_recruiter({"email": email})
        if recruiter:
            if self.verify_password(password, recruiter.get("password")):
                del recruiter["password"]
                return {"status": "ok", "role": "recruiter", "data": recruiter}

        return {"status": "error", "msg": "Invalid email or password"}

    def act(self, query: dict):
        try:
            task = query.get("task")
            data = query.get("data", {})

            match task:
                case "newUser":
                    self.insert_student(data)
                    return {"status": "ok"}

                case "getStudent":
                    student = self.find_student(data)
                    return {"status": "ok", "data": student}
                case "login":
                    return self.handle_login(data)
                case "updateStudent":
                    self.update_student(
                    data.get("query", {}),
                    data.get("update", {})
                    )
                    return {"status": "ok"}

                case "deleteStudent":
                    self.delete_student(data, soft=True)
                    return {"status": "ok"}

                case "newRecruiter":
                    self.insert_recruiter(data)
                    return {"status": "ok"}

                case "getRecruiter":
                    recruiter = self.find_recruiter(data)
                    return {"status": "ok", "data": recruiter}

                case "updateRecruiter":
                    self.update_recruiter(
                        data.get("query", {}),
                        data.get("update", {})
                    )
                    return {"status": "ok"}

                case "deleteRecruiter":
                    self.delete_recruiter(data, soft=True)
                    return {"status": "ok"}

                case _:
                    return {
                    "status": "error",
                    "msg": f"Unknown task: {task}"
                    }

        except DBError as e:
            return {
            "status": "error",
            "msg": e.args[0]
            }

        except Exception as e:
            return {
            "status": "error",
            "msg": f"Internal error: {str(e)}"
        }

