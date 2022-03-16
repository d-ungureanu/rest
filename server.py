from flask import Flask, request, jsonify

flask_object = Flask(__name__)


# http://127.0.0.1:5000
@flask_object.route("/", methods=["GET"])
def homepage():
    return "Welcome to your first WEB server."


# http://127.0.0.1:5000/hi
@flask_object.route("/hi", methods=["GET"])
def say_hi():
    return "Hello visitor."


# http://127.0.0.1:5000/hello?name=Daniel
# http://127.0.0.1:5000/hello?name=Daniel&position=manager
@flask_object.route("/hello", methods=["GET"])
def hello():
    name_var = request.args.get("name")
    position_var = request.args.get("position")
    return f"Hello {name_var}, welcome to your first server. Your position in the enterprise is: {position_var}"


# http://127.0.0.1:5000/employee/312
@flask_object.route("/employee/<employee_id>", methods=["GET"])
def employee_getter(employee_id):
    return f"You're asking for info about employee ID: {employee_id}"


# http://127.0.0.1:5000/employee_record/1
@flask_object.route("/employee_record/<employee_id>", methods=["GET"])
def employee_record_getter(employee_id):
    data = jsonify(id=employee_id, name="Daniel", position="manager")
    return data


@flask_object.route("/employee_add", methods=["POST"])
def employee_add():
    employee_data = request.json
    employee_id = employee_data["e_id"]
    employee_firstname = employee_data["e_firstname"]
    employee_lastname = employee_data["e_lastname"]
    return f"Employee ID: {employee_id} - {employee_firstname} {employee_lastname}"


if __name__ == "__main__":
    flask_object.run(debug=True)
