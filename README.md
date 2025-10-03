# 📝 Todo App

تطبيق **ToDo App** مبسط وحديث يهدف لإدارة المهام اليومية بسهولة.  
يدعم خاصية **تسجيل الدخول (Login)** بحيث يستطيع المستخدم الوصول لقائمة مهامه من أي جهاز، بالإضافة إلى الخصائص الأساسية لإدارة المهام مثل الإضافة، التعديل، الحذف، الإكمال، تحديد الوقت والمدة.

---

## 🚀 Features (الخصائص)

- 👤 **Authentication (Login/Signup)**:  
  - يسمح لكل مستخدم بامتلاك قائمة مهامه الخاصة.  
  - تسجيل الدخول يتيح الوصول من أي جهاز.  

##🔑 Authentication Endpoints
Signup

POST /auth/signup

👉 إنشاء حساب جديد

Request body:

{
  "username": "john_doe",
  "password": "securePassword"
}


Response:

{
  "message": "User created successfully",
  "userId": 1
}

Login

POST /auth/login

👉 تسجيل الدخول والحصول على Token للوصول للمهام الخاصة

Request body:

{
  "username": "john_doe",
  "password": "securePassword"
}


Response:

{
  "token": "jwt_token_example"
}


GET /todos/{id}

👉 جلب مهمة واحدة بالـ ID

Response:

{
  "id": 1,
  "title": "Buy groceries",
  "completed": false,
  "createdAt": "2025-09-24T12:00:00Z"
}


- ➕ **إضافة مهمة جديدة**: كتابة عنوان المهمة + وقت إنشائها.

POST /todos
Request body:
{ "title": "Go for a run" } 

Response:
{
  "id": 3,
  "title": "Go for a run",
  "completed": false,
  "createdAt": "2025-09-24T14:00:00Z"
}

- ✏️ **تعديل مهمة**: تحديث العنوان أو حالة الإنجاز.
  PUT /todos/{id}
Request body:

{
  "title": "Buy groceries and snacks",
  "completed": true
}


Response:

{
  "id": 1,
  "title": "Buy groceries and snacks",
  "completed": true,
  "createdAt": "2025-09-24T12:00:00Z"
} 

- ✅ **إكمال مهمة**: تغيير حالة المهمة إلى منجزة. 

- 🗑 **حذف مهمة**: إزالة أي مهمة نهائيًا.

DELETE /todos/{id}
Response:

{ "message": "Todo deleted successfully" }
 

- ⏰ **التوقيت والمدة**: إمكانية حفظ وقت الإنشاء والمدة المطلوبة لإنجاز المهمة.
  - إمكانية تحديد تاريخ المهمة (اليوم، الغد، أو تاريخ معين).  
  - تحديد وقت التنفيذ (مثلاً 15:30).  
  - تحديد المدة المتوقعة لإنجاز المهمة (minutes أو hours).   

---

## 📌 Endpoints

### 1. Get all todos  
**GET /todos**  

👉 جلب جميع المهام الخاصة بالمستخدم الحالي  

**Response:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false,
    "createdAt": "2025-09-24T12:00:00Z"
  },
  {
    "id": 2,
    "title": "Finish project",
    "completed": true,
    "createdAt": "2025-09-24T13:00:00Z"
  }
]
```
## ⚙️ Workflow (آلية العمل)

يقوم المستخدم بإنشاء حساب جديد أو تسجيل الدخول.

عند تسجيل الدخول يحصل على Token يستخدمه للوصول لجميع الـ Endpoints.

كل مستخدم يمتلك قائمة Todos خاصة به فقط.

يمكن إضافة/تعديل/حذف/إكمال المهام في أي وقت.

يتم حفظ وقت الإنشاء (createdAt) لكل مهمة.

يمكن تحديد تاريخ (dueDate) ومدة زمنية (duration) لإنجاز المهمة.

يمكن تحديد Priority لتصنيف المهام (عالية/متوسطة/منخفضة الأهمية).

واجهة التطبيق تغيّر ألوان عرض المهام بناءً على الأولوية.

## 📦 Tech Stack

Backend: Python (Flask)

Frontend: React

Database: MySQL

Authentication: JWT

Date/Time Handling: Python datetime

ORM: SQLAlchemy / Peewee (مقترح للربط مع MySQL)
