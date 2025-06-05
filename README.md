🛍️ E-Commerce Sales Chatbot
📌 Project Overview
This project implements an AI-powered sales chatbot for an e-commerce platform specializing in electronics. Developed using Python and Django, the chatbot enhances the shopping experience by assisting customers in product discovery, providing personalized recommendations, and facilitating seamless transactions.

🛠️ Key Features
Product Search & Discovery: Users can inquire about products by category, price range, or brand.

Personalized Recommendations: The chatbot suggests products based on user preferences and browsing history.

Order Assistance: Guides users through the purchasing process, including adding items to the cart and checking out.

User Authentication: Secure login and session management to personalize interactions.

Responsive Design: Optimized for desktop, tablet, and mobile devices.

⚙️ Technology Stack
Backend: Python 3.11, Django 5.1.6

Frontend: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5

Database: SQLite (for development); PostgreSQL or MySQL recommended for production

AI Integration: OpenAI API for natural language processing

Asynchronous Task Management: Celery with Redis (for background tasks)

WebSockets: Django Channels for real-time communication

🗂️ Project Structure
The project follows Django's standard structure with the addition of specific components for the chatbot functionality:


ecommerce_chatbot/
├── chatbot/                  
│   ├── migrations/
│   ├── templates/
│   │   └── chatbot/
│   │       ├── chat.html     
│   │       ├── login.html    
│   │       └── register.html 
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py          
│   ├── forms.py
│   ├── models.py
│   ├── routing.py          
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── nlp.py             
├── ecommerce_chatbot/
│   ├── __init__.py
│   ├── asgi.py               
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
