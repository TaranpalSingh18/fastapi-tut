# 🍕 Pizza Delivery API

A FastAPI-based backend project simulating a pizza delivery system. It includes user authentication, order management, and admin-level control over orders.

---

## ✅ Project Status: Completed

### Implemented Endpoints:

* `POST /api/signup` – User registration
* `POST /api/login` – User login and JWT token generation
* `POST /api/order` – Place a new pizza order
* `PUT /api/order/update/{order_id}` – Update an existing order (e.g., change quantity or pizza size)
* `PUT /api/order/status/{order_id}` – Update order delivery status (e.g., *In Transit*, *Delivered*, *Cancelled*)
* `DELETE /api/order/{order_id}/delete` – Delete a specific order
* `GET /api/user/orders/` – Retrieve all orders placed by the logged-in user
* `GET /api/orders/` – Admin view to list **all** orders
* `GET /api/orders/{order_id}` – Retrieve specific order (Admin or User with permissions)
* `GET /api/user/order/{order_id}` – Get a specific order placed by the current user

---

## 🛠 Tech Stack & Skills Learned

| 🔧 Tool    | 💡 Concept Learned                   |
| ---------- | ------------------------------------ |
| PostgreSQL | Relational database management       |
| FastAPI    | Building RESTful APIs with Python    |
| Pydantic   | Data validation using models         |
| SQLAlchemy | ORM for defining and querying models |
| JWT Auth   | User authentication & authorization  |

---

## 🧱 Models Defined

* **User**
* **Order**

### Key Fields

* User: `id`, `username`, `email`, `password`
* Order: `id`, `pizza_size`, `quantity`, `status`, `user_id`

---

## 🔒 Authentication

* All endpoints (except signup/login) are secured using **JWT-based Auth**.
* Tokens are required in headers to access protected routes.

---

## 📃 API Usage Examples

### Signup:

```bash
POST /api/signup
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure123"
}
```

### Login:

```bash
POST /api/login
{
  "username": "john_doe",
  "password": "secure123"
}
Response:
{
  "access_token": "your_jwt_token"
}
```

### Place an Order:

```bash
POST /api/order
Headers: { Authorization: Bearer <token> }
{
  "pizza_size": "LARGE",
  "quantity": 2
}
```

---

## 📊 Database Schema Overview

**User Table**

* `id`: Primary Key
* `username`, `email`, `password`

**Order Table**

* `id`: Primary Key
* `pizza_size`, `quantity`, `status`
* `user_id`: Foreign Key -> User

---

## ⚖️ API Testing Tools

* Swagger Docs: Available at `/docs`

---

## ♻️ Deployment

* FastAPI app hosted locally or on cloud (e.g., AWS EC2 or Render)
* PostgreSQL running on local or managed service (e.g., Supabase or RDS)
* Environment variables managed via `.env`

---

## 🚀 Future Enhancements

* Real-time order tracking via WebSocket
* Admin dashboard with analytics
* Email notifications on order status

---

> Built with love using FastAPI, PostgreSQL & SQLAlchemy. Contributions welcome!
