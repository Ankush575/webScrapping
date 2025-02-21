# route file ibn which routing or the api is defined
from flask import Blueprint, request, jsonify
from controllers.studentController import insertSingleStudent, insertMultipleStudents, fetchAllStudentsFromDatabase

# Create a Blueprint for routes
student_routes = Blueprint('student_routes', __name__)

# API to insert a student


@student_routes.route('/addSingleStudent', methods=['POST'])
def addSingleStudent():
    data = request.json
    if not all(k in data for k in ("id", "firstName", "lastName", "rollNumber", "email", "age")):
        return jsonify({"success": False, "message": "Missing required fields!"}), 400

    result = insertSingleStudent(
        data["id"],
        data["firstName"],
        data["lastName"],
        data["rollNumber"],
        data["email"],
        data["age"]
    )
    return jsonify(result), (200 if result["success"] else 400)

# API to insert multiple students


@student_routes.route('/addMultipleStudents', methods=['POST'])
def addMultipleStudents():
    data = request.json
    if not isinstance(data, list):
        return jsonify({"success": False, "message": "input should be list of students."}), 400

    requiredFileds = {"id", "firstName",
                      "lastName", "rollNumber", "email", "age"}

    for student in data:
        if not all(k in student for k in requiredFileds):
            return jsonify({"success": False, "message": "Missing required fields!"}), 400

    result = insertMultipleStudents(data)
    return jsonify(result), (200 if result["success"] else 400)


# API to fetch all the students from database
@student_routes.route('/fetchAllStudents', methods=['GET'])
def getAllStudents():
    result = fetchAllStudentsFromDatabase()
    return jsonify(result), (200 if result["success"] else 400)
