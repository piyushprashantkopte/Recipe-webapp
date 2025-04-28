# Recipe WebApp - Django Project

![if authenticted show home page](https://github.com/user-attachments/assets/9c2fa61f-96ba-499a-b6e5-cbfb081ad6d4)

## Project Description
The Recipe WebApp is a Django-based application that allows users to:
- Create, read, update, and delete recipes
- Search through existing recipes
- View detailed recipe information
- Register and authenticate to access personalized features

This application is designed for food enthusiasts who want to maintain and share their favorite recipes in an organized manner.

## Features
- **User Authentication**:
  - Registration with email, name, and password
  - Secure login functionality
- **Recipe Management**:
  - Add new recipes with name, description, and images
  - Edit existing recipes
  - View all recipes in a clean table format
- **Search Functionality**:
  - Search recipes by name or keywords
- **Responsive Design**:
  - Works on various screen sizes

## Screenshots

### Login Page
![loginform](https://github.com/user-attachments/assets/ced92f66-f5cb-4d45-b63a-f6c76fbfc8d6)

### Registration Page
![registrationform](https://github.com/user-attachments/assets/5e1a7cce-48ed-4e75-a04b-8100e880c42e)

### Recipe Display
![recipes display table](https://github.com/user-attachments/assets/b56c60b2-4b72-4704-b3c8-98e60b748b60)

### Add Recipe
![add new recipe](https://github.com/user-attachments/assets/ffa69bb0-fee1-4782-9098-906b554cde47)

### Update Recipe
![update recipe page](https://github.com/user-attachments/assets/a1fc8e3f-2dec-4bbe-bc68-12514918077b)

### Search Functionality
![searchbar functionality](https://github.com/user-attachments/assets/f51b9a9b-a12c-4ca7-900b-f3ea92081dd8)
![show that recipe](https://github.com/user-attachments/assets/3d2deb6a-53e2-4868-b0f5-d35ff1107528)


## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone "repository url"
   cd recipe-webapp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

## Usage
1. Register a new account or login if you already have one
2. Navigate to the recipes section
3. Use the "Add Recipe" button to create new recipes
4. Click on any recipe to view details
5. Use the search bar to find specific recipes
6. Edit or delete recipes as needed

## Technologies Used
- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, can be configured for others)
- **Authentication**: Django's built-in authentication system
- **Deployment**: (Optional) Heroku, AWS, or other platforms

