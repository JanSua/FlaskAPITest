from flask_restful import Api, Resource, reqparse

# Simularuna base de datos
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": False},
]

# Instancia de la API
api = Api()

# Recursos
class TaskList(Resource):
    def get(self):
        """Lista todas las tareas"""
        return tasks, 200

    def post(self):
        """Crea una nueva tarea"""
        parser = reqparse.RequestParser()
        parser.add_argument("title", required=True, help="Title cannot be blank!")
        parser.add_argument("completed", type=bool, default=False)
        args = parser.parse_args()

        new_task = {
            "id": len(tasks) + 1,
            "title": args["title"],
            "completed": args["completed"],
        }
        tasks.append(new_task)
        return new_task, 201

class Task(Resource):
    def get(self, task_id):
        """Obtiene una tarea específica por ID"""
        task = next((task for task in tasks if task["id"] == task_id), None)
        if not task:
            return {"error": "Task not found"}, 404
        return task, 200

    def put(self, task_id):
        """Actualiza una tarea específica"""
        task = next((task for task in tasks if task["id"] == task_id), None)
        if not task:
            return {"error": "Task not found"}, 404

        parser = reqparse.RequestParser()
        parser.add_argument("title", required=False)
        parser.add_argument("completed", type=bool, required=False)
        args = parser.parse_args()

        if args["title"]:
            task["title"] = args["title"]
        if args["completed"] is not None:
            task["completed"] = args["completed"]

        return task, 200

    def delete(self, task_id):
        """Elimina una tarea específica"""
        global tasks
        tasks = [task for task in tasks if task["id"] != task_id]
        return {"message": "Task deleted"}, 200

# Registrar los recursos
def init_app(app):
    api.add_resource(TaskList, "/tasks")
    api.add_resource(Task, "/tasks/<int:task_id>")
    api.init_app(app)
