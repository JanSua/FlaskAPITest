
# 🚀 Flask API Template

A minimal **Flask-RESTful API template** for quick REST API setup.

---

## 🛠️ Installation

```
git clone https://github.com/JanSua/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate (Windows)
pip install -r requirements.txt
python app.py
```

Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛣️ Endpoints

### **GET /tasks**
List all tasks.

Response:
```
[]
```

---

### **POST /tasks**
Create a new task.

Body:
```
{
  "title": "Example Task",
  "completed": false
}
```

Response:
```
{
  "id": 1,
  "title": "Example Task",
  "completed": false
}
```

---

### **GET /tasks/<task_id>**
Get a single task by ID.

---

### **PUT /tasks/<task_id>**
Update a task.

Body:
```
{
  "title": "Updated Task",
  "completed": true
}
```

---

### **DELETE /tasks/<task_id>**
Delete a task.

Response:
```
{
  "message": "Task deleted"
}
```
