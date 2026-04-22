# FastAPI Blog Application

Full-stack blog platform following [the Corey Schafer series](https://youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI&si=TAQ1Nim2XPYu53xw). Built with **Python 3.12**, this repository implements a dual-layer architecture: a robust **REST API** for programmatic access and a server-side rendered **frontend** for human users.

## 🛠 Dev Stack

* **Backend:** FastAPI, Pydantic
* **Data/ORM:** SQLAlchemy (SQLite for dev, PostgreSQL for production)
* **Security:** OAuth2, JWT Authentication, Passlib (bcrypt)
* **Frontend:** Jinja2 Templates, HTML5, CSS3
* **Tooling:** UV package manager, Python-Multipart
* **OS:** Optimized for Fedora/Linux deployment

## 🚀 Key Features

* **Interactive Docs:** Automatic Swagger UI (`/docs`) and ReDoc (`/redoc`) generation.
* **Secure Auth:** Full user registration and login with encrypted password storage.
* **Content Management:** Complete CRUD operations (Create, Read, Update, Delete) for posts.
* **Schema Isolation:** Frontend-only routes are hidden from the public API schema for a cleaner developer experience.

## 📦 Installation & Setup

This project uses **uv** for high-performance dependency management.

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/fastapi-blog.git](https://github.com/yourusername/fastapi-blog.git)
   cd fastapi-blog
