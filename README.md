# Full-Stack Authentication App

A modern full-stack application with JWT authentication, built with React (Bootstrap) frontend and FastAPI backend.

## 📋 Project Description

This application demonstrates a complete authentication flow with:
- User login with JWT token generation
- Protected routes for authenticated users
- Responsive UI with Bootstrap
- Secure password handling
- RESTful API backend

## 🛠 Tech Stack

### Frontend
- **React 19** - JavaScript library for building user interfaces
- **Bootstrap 5** - CSS framework for responsive design
- **React Router v6** - Client-side routing
- **Vite** - Fast frontend build tool
- **Axios** (via fetch API) - HTTP client for API calls

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Python-JOSE** - JWT token handling
- **Hashlib** - Password hashing (SHA-256)
- **CORS Middleware** - Cross-origin resource sharing
- **SQLAlchemy** - ORM for database operations
- **Psycopg2** - PostgreSQL database adapter
- **Python-dotenv** - Environment variable management

### Database
- **PostgreSQL 16** - Relational database
- **Alpine-based container** - Lightweight PostgreSQL image

### Development Tools
- **Python 3.14** - Backend language
- **Node.js** - Frontend runtime
- **npm** - Package manager
- **Podman/Docker** - Containerization
- **Podman Compose** - Container orchestration

## 🚀 Getting Started

### Prerequisites
- **For manual setup**:
  - Python 3.14+
  - Node.js 18+
  - npm 9+

- **For containerized setup**:
  - Podman or Docker
  - Podman Compose or Docker Compose

### Installation

#### Option 1: Manual Setup

##### 1. Clone the repository
```bash
git clone https://github.com/yourusername/auth-app.git
cd auth-app
```

##### 2. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

##### 3. Set up the frontend
```bash
cd ../frontend
npm install
```

#### Option 2: Containerized Setup (Recommended)

##### 1. Build and start containers
```bash
podman-compose up --build
```

##### 2. To run in detached mode
```bash
podman-compose up --build -d
```

### Running the Application

#### Manual Setup

##### Start the backend
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

##### Start the frontend
```bash
cd ../frontend
npm run dev
```

#### Containerized Setup

The containers will start automatically with:
- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`

To stop the containers:
```bash
podman-compose down
```

## 📱 Usage

### Access the Application
- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000`

### Login
1. Navigate to the login page
2. Enter test credentials:
   - **Username**: `johndoe`
   - **Password**: `secret`
3. Click "Sign In"

### Welcome Page
After successful login, you'll be redirected to the welcome page showing:
- Your username
- Full name
- Email address
- Logout button

### Logout
Click the "Logout" button to:
- Clear the JWT token
- Return to the login page

## 🔧 API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/token` | POST | Get JWT token | None |
| `/welcome/` | GET | Get user welcome data | Bearer Token |
| `/users/me/` | GET | Get current user info | Bearer Token |
| `/users/me/items/` | GET | Get user items | Bearer Token |
| `/users/` | POST | Create new user | None |

**POST /users/ Parameters:**
- `username` (string, required)
- `password` (string, required)
- `full_name` (string, optional)
- `email` (string, optional)

## 📝 Features

### Authentication
- JWT token-based authentication
- Secure password hashing with SHA-256
- Token storage in localStorage
- Protected routes

### UI/UX
- Responsive design with Bootstrap
- Loading states
- Error handling
- Form validation
- Blue color palette

### Security
- CORS restricted to frontend origin
- Password hashing
- JWT token expiration
- HTTPS-ready (configure for production)

## 🔒 Security Best Practices

### 🛑 Important Security Notes

This project includes a `.gitignore` file that excludes sensitive files like `.env` from version control. A sample `.env.example` file is provided for reference.

### 🔐 For Production Deployment

1. **Generate Strong Secrets**:
   ```bash
   # Generate a strong secret key
   openssl rand -hex 32
   ```

2. **Environment Variables**:
   - Copy `.env.example` to `.env`
   - Replace all placeholder values with strong credentials
   - Never commit `.env` to version control

3. **Database Security**:
   - Use strong PostgreSQL credentials
   - Create separate users with least privilege
   - Use different database names for production

4. **HTTPS**:
   - Always use HTTPS in production
   - Configure proper SSL certificates
   - Use secure cookie settings

5. **Password Hashing**:
   - Consider using bcrypt for production
   - Add salt to password hashes
   - Implement proper password policies

6. **Additional Security Measures**:
   - Add rate limiting to prevent brute force attacks
   - Implement CSRF protection
   - Add input validation and sanitization
   - Set up proper CORS policies
   - Implement password reset functionality
   - Add logging and monitoring

### 📝 Environment Variables

The project uses the following environment variables (see `.env.example`):

**Security:**
- `SECRET_KEY`: JWT signing key
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

**Database:**
- `DATABASE_URL`: Full PostgreSQL connection URL
- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `POSTGRES_HOST`: Database host
- `POSTGRES_PORT`: Database port

### 🚨 Security Vulnerabilities

If you discover any security vulnerabilities, please:
1. **Do not open an issue**
2. **Do not create a pull request**
3. **Do not disclose publicly**
4. **Contact the maintainers privately**

## 📝 Environment Setup

### Development Setup

1. Copy the example environment file:
   ```bash
   cd backend
   cp .env.example .env
   ```

2. Edit `.env` with your preferred credentials (keep development values for local testing)

3. The application will automatically use these environment variables

### Production Setup

1. Generate strong secrets:
   ```bash
   # Generate secret key
   echo "SECRET_KEY=$(openssl rand -hex 32)" > .env
   
   # Generate database password
   echo "POSTGRES_PASSWORD=$(openssl rand -hex 16)" >> .env
   ```

2. Complete the `.env` file with all required variables

3. Ensure `.env` is in `.gitignore` and never committed

## 📁 Project Structure

```
auth-app/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── init_db.py        # Database initialization script
│   ├── generate_secret.py # Secret key generator
│   ├── requirements.txt # Python dependencies
│   ├── run_backend.sh   # Startup script
│   ├── Dockerfile       # Backend container configuration
│   ├── .env             # Environment variables (gitignored)
│   ├── .env.example     # Example environment variables
│   └── venv/            # Python virtual environment
│
├── frontend/
│   ├── src/
│   │   ├── LoginPage.jsx     # Login component
│   │   ├── WelcomePage.jsx   # Welcome component
│   │   ├── main.jsx          # App entry point
│   │   ├── index.css         # Global styles
│   │   └── ...
│   ├── package.json     # Node.js dependencies
│   ├── Dockerfile       # Frontend container configuration
│   └── vite.config.js    # Vite configuration
│
├── .gitignore          # Git ignore rules
├── podman-compose.yml   # Container orchestration
└── README.md           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions or support, please contact:
- Your Name: [bozzimarcello@gmail.com](mailto:your.email@example.com)
- Project Link: [https://github.com/bozzimarcello/vibe-test](https://github.com/bozzimarcello/vibe-test)
