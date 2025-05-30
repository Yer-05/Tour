                    Final Project

Coursework Report: Tour Booking System
Student: Seiman Yerman
Date: May 30, 2025

1. Introduction and Project Goals
The main goal of this project is to make a website for tourists. On this website, people can look at tours and book them. There are also tools for managers and administrators to manage the tours and bookings. The website keeps users safe by giving different access for tourists, managers, and administrators.
Key Functional Requirements:
⦁	User registration and authentication with role-based access control (Tourist / Manager / Admin).
⦁	Full Create, Read, Update, Delete (CRUD) operations for tours, bookings, and reviews.
⦁	Secure password hashing and session management.
⦁	AI-powered automatic tour description generation to assist admins in creating attractive tour listings.
⦁	Responsive, user-friendly interface with intuitive navigation for seamless user experience.

2. Application Features and AI Integration
Main Functionalities by Role
Role	Features
Tourist	Browse tours, make bookings, submit reviews, view manager replies
Manager	All Tourist features, plus edit tour prices/status, respond to customer reviews
Admin	Full system control: create/edit/delete tours, manage users, approve or reject bookings
AI Description Generator
⦁	Added an AI feature using OpenAI GPT-3.5 to help write tour descriptions automatically.
⦁	When an admin creates a new tour, they can click “Generate Description”, which calls a function in app/ai_utils.py.
⦁	This function crafts a prompt from tour title and country, sends it to OpenAI, and fills the response into the tour description field.
⦁	The OpenAI API key is securely stored in environment variables (never hard-coded or committed).
Example usage:
from app.ai_utils import generate_description

description = generate_description(title=form.title.data, country=form.country.data)

3. Entity Relationship Diagram (ER)
Entities and Attributes
Entity	Attributes
User	id, username, password_hash, is_admin
Tour	id, title, country, description, price, image
Booking	id, user_id (FK), tour_id (FK), date
Review	id, user_id (FK), tour_id (FK), rating, comment
Relationships
⦁	One User can have many Bookings and many Reviews.
⦁	One Tour can have many Bookings and many Reviews.
⦁	Each Booking and Review is linked to exactly one User and one Tour.
ER diagram was generated using sqlacodegen and visualized with Graphviz.

4. Code Structure and Architecture
Project Directory Layout
FinalBEKEND/
├── app/
│   ├── __init__.py          # Initializes Flask app, SQLAlchemy, LoginManager
│   ├── models.py            # ORM models for User, Tour, Booking, Review
│   ├── forms.py             # WTForms definitions for input validation
│   ├── sentiment.py         # AI integration logic, e.g., description generation, sentiment analysis
│   ├── routes/
│   │   ├── __init__.py      # Blueprint registration
│   │   ├── user_routes.py   # Routes accessible by tourists
│   │   └── admin_routes.py  # Routes for admin and manager functions
│   └── templates/           # Jinja2 HTML templates for UI rendering
├── config.py                # Configuration: SECRET_KEY, database URI, OpenAI API key setup
├── run.py                   # Main application entry point
└── requirements.txt         # List of Python package dependencies
Architectural Highlights
⦁	OOP Principles: Core entities (Tour, Booking, User) implemented as classes with clear encapsulation.
⦁	Blueprints: Modular routing separated by user roles to improve maintainability and scalability.
⦁	Secure Authentication: Passwords hashed securely; session management through Flask-Login.
⦁	AI Integration: Encapsulated AI features in dedicated modules (sentiment.py or ai_utils.py) for clarity.
⦁	Template-driven UI: Using Jinja2 for dynamic server-side HTML rendering.

The result is a screenshot
 

 






