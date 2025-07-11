# 🐾 Pet Store Backend API

This is a backend API for managing a comprehensive Pet Store Management System. It includes functionality for users, pets, appointments, adoptions, bills, medications, medical records, reviews, mating, inventory, authentication, reports, and payments.

---

## 🚀 Features

- 🔐 User management & authentication
- 🐶 Pet creation & adoption system
- 📅 Appointments scheduling & confirmation
- 💊 Medical records & medication tracking
- 🧾 Billing & payment processing
- 🛒 Inventory management
- 🐕‍🦺 Vet reviews and ratings
- ❤️ Pet mating request handling
- 📊 Reports: revenue, appointments, inventory status

---

## 🛠️ Tech Stack

| Layer         | Technology                       |
|---------------|----------------------------------|
| Backend       | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM           | [SQLAlchemy](https://www.sqlalchemy.org/) |
| Data Models   | [Pydantic](https://docs.pydantic.dev/) |
| Database      | PostgreSQL / SQLite (configurable) |
| Dependency Injection | FastAPI's Depends            |
| Docs (auto-generated) | Swagger UI & ReDoc            |
| Development Tools | Uvicorn (ASGI server), Python 3.13, Virtualenv |
| Testing       | (TBD: pytest suggested)          |

---

## 🧪 Requirements

- Python 3.13+
- pip
- virtualenv
- PostgreSQL (optional, SQLite fallback)

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/pet-store-app.git
cd pet-store-app/backend
```

2. **Create and activate virtual environment:**

```bash
python3 -m venv app/env
source app/env/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Start the server:**

```bash
uvicorn app.main:app --reload
```

5. **Access API Docs:**

- Swagger: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redoc

6. **Run using Docker**

```bash
# Build the image
docker build -t petstore-backend .

# Run the container
docker run -p 8000:8000 petstore-backend

```

## API Modules

```/users``` – Manage users

```/pets``` – Manage pet listings

```/pet-adoptions``` – Pet adoption workflows

```/appointments``` – Appointments and scheduling

```/bills``` – Billing endpoints

```/payments``` – Payment tracking

```/inventory``` – Store inventory

```/medications``` – Track medication

```/medical-records``` – Vet medical records

```/reviews``` – Vet reviews by users

```/mating-requests``` – Handle mating proposals

```/auth``` – Authentication status

```/reports``` – Business insights and reports

---

## To Do

Add pet sitting services

Add pet vaccination records

Add pet photo

Add delete requests for adoptions and mating

Add JWT-based authentication

Implement pagination and filters

Unit & integration tests

Role-based access control (admin, vet, user)

Email notifications (e.g. appointment confirmation)

---

## License

This project is licensed under the MIT License. Feel free to use and modify.

---

## Contributions

Feel free to fork this repo and contribute via Pull Requests. Open issues for any bugs or feature requests.

---

---

## 🖥️ Frontend Setup

The frontend for this application is located in the `frontend/` directory and is built using [React](https://reactjs.org/).

### 🚧 Prerequisites

- Node.js (v18+ recommended)
- npm or yarn

---

### ▶️ Run the Frontend

1. **Navigate to the frontend directory:**

```bash
cd ../frontend
```

2. **Install dependencies:**

```bash
npm install
# or
yarn install
```

---

3. **Start the development server:**

```bash
npm run dev
# or
yarn dev
```

---

4. **Access the frontend app:**

- http://localhost:3000

## 🛠️ Frontend Environment Variables

Create a .env file in the frontend root and set the base URL for the backend API:

```
VITE_API_BASE_URL=http://localhost:8000
```

Replace VITE_ with NEXT_PUBLIC_ or VUE_APP_ if you're using Next.js or Vue.

---

## 🧰 Useful Scripts

| Command           | Description                |
| ----------------- | -------------------------- |
| `npm run dev`     | Start development server   |
| `npm run build`   | Create production build    |
| `npm run preview` | Preview production build   |
| `npm run lint`    | Run linter (if configured) |

---

## ✅ Combined Start (Backend + Frontend)

```bash
# In separate terminals:
uvicorn app.main:app --reload         # Backend
npm run dev                           # Frontend
```

Alternatively, consider using concurrently or Docker Compose for unified startup.
