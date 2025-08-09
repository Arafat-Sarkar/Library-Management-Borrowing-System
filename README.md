# 📚 Library Management & Borrowing System

A Django REST Framework API for managing a library system that allows users to register, login, browse books, borrow and return books with borrowing limits and penalty points. Admins can manage books, authors, and categories.

## 🚀 Features
🔐 User registration and login using JWT authentication

📚 Users can browse books  author or category

📖 Users can borrow books with a limit of 3 active borrows

🔄 Users can return borrowed books early

⏳ Borrow due date set to 14 days after borrowing

⚠️ Late returns add penalty points to user profiles

🛠️ Admin can add, edit, and delete books, authors, and categories via Django admin

🔄 Atomic updates to book inventory on borrow and return

🔒 Secure endpoints with permissions for users and admins

## 🛠️ Technologies Used
🔧 Backend (Django REST Framework)
Django

Django REST Framework

Simple JWT for authentication

## API Endpoints

/api/register/ – JWT authentication endpoints

/api/authors/ – Author CRUD (Admin only)

/api/category/ – Category CRUD (Admin only)

/api/books/ – List & manage books

/api/borrow/ – Borrow books
/api/return/ –  return books

