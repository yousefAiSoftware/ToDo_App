### 📌 Endpoints

- **GET /todos**  
  👉 Fetch all todos  
  **Response:**
  
  `[   {     "id": 1,     "title": "Buy groceries",     "completed": false,     "createdAt": "2025-09-24T12:00:00Z"   },   {     "id": 2,     "title": "Finish project",     "completed": true,     "createdAt": "2025-09-24T13:00:00Z"   } ]`

- **POST /todos**  
  👉 Add a new todo  
  **Request body:**
  
  `{   "title": "Go for a run" }`
  
  **Response:**
  
  `{   "id": 3,   "title": "Go for a run",   "completed": false,   "createdAt": "2025-09-24T14:00:00Z" }`

- **GET /todos/{id}**  
  👉 Get a single todo by ID  
  **Response:**
  
  `{   "id": 1,   "title": "Buy groceries",   "completed": false,   "createdAt": "2025-09-24T12:00:00Z" }`

- **PUT /todos/{id}**  
  👉 Update a todo (title or completed status)  
  **Request body:**
  
  `{   "title": "Buy groceries and snacks",   "completed": true }`
  
  **Response:**
  
  `{   "id": 1,   "title": "Buy groceries and snacks",   "completed": true,   "createdAt": "2025-09-24T12:00:00Z" }`

- **DELETE /todos/{id}**  
  👉 Delete a todo  
  **Response:**
  
  `{   "message": "Todo deleted successfully" }`

---

### 📌 Data model (Todo)

`{   "id": number,   "title": string,   "completed": boolean,   "createdAt": ISODate string }`

---

Do you want me to also sketch **auth endpoints** (signup/login) in case you guys want users to have their own todo lists, or keep it **single-user only** for now?

##### You said:

can you put it all in a markdown file

###### ChatGPT said:

Here’s a clean **Markdown file** version you can hand to your friend 👇

`# 📝 Todo App Backend API  A simple REST API model for a Todo app. ---  ## 📌 Endpoints  ### 1. Get all todos **GET /todos**  **Response:** ```json [   {     "id": 1,     "title": "Buy groceries",     "completed": false,     "createdAt": "2025-09-24T12:00:00Z"   },   {     "id": 2,     "title": "Finish project",     "completed": true,     "createdAt": "2025-09-24T13:00:00Z"   } ]`

---

### 2. Add a new todo

**POST /todos**

**Request body:**

`{   "title": "Go for a run" }`

**Response:**

`{   "id": 3,   "title": "Go for a run",   "completed": false,   "createdAt": "2025-09-24T14:00:00Z" }`

---

### 3. Get a single todo

**GET /todos/{id}**

**Response:**

`{   "id": 1,   "title": "Buy groceries",   "completed": false,   "createdAt": "2025-09-24T12:00:00Z" }`

---

### 4. Update a todo

**PUT /todos/{id}**

**Request body:**

`{   "title": "Buy groceries and snacks",   "completed": true }`

**Response:**

`{   "id": 1,   "title": "Buy groceries and snacks",   "completed": true,   "createdAt": "2025-09-24T12:00:00Z" }`

---

### 5. Delete a todo

**DELETE /todos/{id}**

**Response:**

`{   "message": "Todo deleted successfully" }`

---

## 📌 Data Model

A todo object has the following structure:

`{   "id": number,   "title": string,   "completed": boolean,   "createdAt": ISODate string }`

`---  Want me to extend this file with **authentication endpoints (signup/login)**, so each user can have their own todo list, or keep it simple single-user for now?`
