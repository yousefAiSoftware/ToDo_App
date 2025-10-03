# ToDo App API Documentation

## Authentication

### 1. Register a new user
- **Method:** POST
- **URL:** /api/auth/register
- **Body (JSON):**
  {
      "username": "some_username",
      "password": "some_password"
  }

### 2. Login a user
- **Method:** POST
- **URL:** /api/auth/login
- **Body (JSON):**
  {
      "username": "some_username",
      "password": "some_password"
  }
- **Success Response:**
  {
      "token": "your_jwt_token"
  }

---

## Tasks (Requires Authentication)

**All task requests must include the following header:**
`Authorization: Bearer <your_jwt_token>`

### 1. Get all tasks for the logged-in user
- **Method:** GET
- **URL:** /api/tasks

### 2. Create a new task
- **Method:** POST
- **URL:** /api/tasks
- **Body (JSON):**
  {
      "title": "My new task title",
      "task_description": "Optional description",
      "due_date": "YYYY-MM-DD HH:MM:SS" 
      // At least one time-related field is required
  }

### 3. Get a single task
- **Method:** GET
- **URL:** /api/tasks/<task_id>

### 4. Update a task
- **Method:** PUT
- **URL:** /api/tasks/<task_id>
- **Body (JSON):** (Send only the fields you want to update)
  {
      "title": "My updated title",
      "is_completed": true
  }

### 5. Delete a task
- **Method:** DELETE
- **URL:** /api/tasks/<task_id>