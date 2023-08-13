# Library Management System

Welcome to the Library Management System repository! This repository contains the source code for a Django-based web application designed to manage a library's operations, including book management, member records, lending, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Library Management System is a web application built using Django framework. It allows librarians to manage books, members, lendings, returns, and more in an efficient manner. The application provides an intuitive user interface and streamlines library operations.

## Features
![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/9738e485-a73d-46a6-ae12-33bfb349beb0)

- Add, view, and edit book records
  ![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/afc590d9-ba24-46e4-b3fd-55c14cbef26b)

- Manage member information
  ![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/ba3f35bb-7e96-4798-8968-219ae41fa4d4)

- Track book lendings and returns
  ![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/67b4663c-48cf-4fa5-af35-68f89dafd2d7)

- Debt management for members with outstanding dues
  ![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/44277776-b2e7-4568-88eb-9efd7a3f4784)

- Search functionality to find books by title or author, import books using the Frappe API
  Link to Frappe API - https://frappe.io/api/method/frappe-library
  ![image](https://github.com/anant-khandelwal/LibraryManagementSystem/assets/132798996/61350750-a5ac-4af9-bc26-470722826ea5)
  

## Getting Started

### Prerequisites

- Python
- HTML, CSS 
- Django (install using `pip install Django`)
- Git (optional, for version control)

### Installation

1. Clone the repository
2. Navigate to the project directory: cd library-management
3. Install required dependencies: pip install -r requirements.txt4. 
4. Run the migrations: python manage.py migrate
5. Start the development server: python manage.py runserver 
6. Access the app in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. Access the admin interface at `http://127.0.0.1:8000/admin/` to manage books, members, and lendings.
2. Use the provided URLs to access different sections of the app (e.g., `http://127.0.0.1:8000/books/`, `http://127.0.0.1:8000/members/`, etc.).
3. To import books from the Frappe API, use the "Import Book" feature.
   Link to Frappe API - https://frappe.io/api/method/frappe-library
5. Explore and interact with the app as needed.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Add some feature"`.
4. Push the changes to your forked repository: `git push origin feature-name`.
5. Create a pull request on GitHub.


---

Created by Anant Krishna Khandelwal
https://github.com/anant-khandelwal

   






