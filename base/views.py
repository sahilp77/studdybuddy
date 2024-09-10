from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm


# rooms = [
    
#     {'id': 1, 'tittle': 'Learn Python', 'name': '''What is Python? A Quick Overview
# Python is a high-level, versatile programming language known for its simplicity and readability. Created in 1991 by Guido van Rossum, Python emphasizes clean code and ease of learning, making it popular among beginners and professionals alike.

# Key Features
# Easy to Learn: Python’s syntax is straightforward, mimicking human language, which makes it beginner-friendly.

# Versatile: It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is used for web development, data science, automation, artificial intelligence, and more.

# Extensive Libraries: Python has a rich ecosystem of libraries and frameworks like Django, Flask (web development), NumPy, Pandas (data science), and TensorFlow (machine learning).

# Cross-Platform: It works across different operating systems, including Windows, macOS, and Linux.

# Why Choose Python?
# Productivity: Simple syntax leads to faster development.
# Community Support: Python has a massive, active community, ensuring abundant resources for learning and problem-solving.
# Extensibility: Integration with other languages like C, C++, and Java is seamless.
# In summary, Python’s versatility, ease of use, and strong community make it a top choice for developers across industries.'''},

#     {'id': 2, 'tittle': 'Learn django', 'name': '''What is Django? A Quick Overview
# Django is a high-level, open-source web framework built with Python, designed to enable rapid development and a clean design for web applications. Created in 2005, Django focuses on automating repetitive tasks, allowing developers to build complex, database-driven websites faster and more efficiently.

# Key Features
# Fast Development: Django helps developers move quickly from idea to implementation by providing ready-made solutions for common web development tasks.

# Batteries Included: It comes with built-in components like authentication, URL routing, form handling, and an admin interface, which eliminates the need for third-party packages.

# Security: Django has robust security features, protecting against threats like SQL injection, XSS, and CSRF attacks by default.

# Scalable: Designed for scalability, Django can handle large amounts of traffic and data, making it ideal for growing websites.

# Why Use Django?
# Ease of Use: It’s perfect for both beginners and experienced developers.
# Time-Saving: Built-in features speed up the development process.
# Community Support: Backed by a large, active community, making it easier to find support and resources.
# In summary, Django is a reliable, efficient, and secure framework for building modern web applications.'''},
    
#     {'id': 3, 'tittle': 'Learn js', 'name': '''What is JavaScript? A Quick Overview
# JavaScript is a dynamic, high-level programming language primarily used for building interactive elements on websites. Created in 1995, it runs in the browser, making it essential for front-end development, and has since expanded to server-side environments like Node.js.

# Key Features
# Client-Side Scripting: JavaScript enables dynamic content updates, user interaction, animations, and form validation directly in the browser.

# Cross-Platform: Runs on any device with a browser, making it highly versatile for web applications.

# Event-Driven: JavaScript handles events (e.g., clicks, inputs) to create interactive user experiences.

# Server-Side with Node.js: JavaScript is also used for server-side development, allowing full-stack development with a single language.

# Why Choose JavaScript?
# Interactivity: It brings life to web pages through features like animations and real-time updates.
# Popularity: It's widely used, ensuring strong community support and numerous frameworks like React, Angular, and Vue.
# Versatility: Works across different platforms, from web to mobile and even backend.
# In summary, JavaScript is essential for modern web development, offering dynamic functionality and versatility both on the client and server sides.'''},
    
#     {'id': 4, 'tittle': 'Learn java', 'name': '''What is Java? A Quick Overview
# Java is a high-level, object-oriented programming language designed for portability and performance. Released in 1995 by Sun Microsystems, Java is widely used for building applications that run on any device with a Java Virtual Machine (JVM).

# Key Features
# Write Once, Run Anywhere (WORA): Java code can run on any platform that has a JVM, making it highly portable.

# Object-Oriented: Java’s structure encourages the use of objects, promoting reusable and modular code.

# Robust and Secure: Built-in memory management, exception handling, and security features make Java reliable and secure for large-scale applications.

# Multithreading: Java supports multithreading, allowing concurrent execution of multiple tasks, which is essential for high-performance applications.

# Why Choose Java?
# Scalability: Ideal for enterprise-level applications like banking systems.
# Community Support: Java has a large, mature ecosystem with extensive documentation and libraries.
# Cross-Platform: Its ability to run on various platforms makes it versatile for web, mobile, and desktop applications.
# In summary, Java's portability, reliability, and scalability make it a go-to language for building large, cross-platform applications.'''},
    
#     {'id': 5, 'tittle': 'Learn something', 'name': '''The Power of Lifelong Learning: Why and How to Keep Growing
# Lifelong learning is the continuous, self-motivated pursuit of knowledge for personal or professional development. It involves gaining new skills, expanding your mind, and adapting to an ever-changing world.

# Key Benefits
# Adaptability: Staying curious and learning new skills helps you adapt to changes in technology, work, and life.

# Career Growth: Continuous learning makes you more competitive and opens up new career opportunities.

# Mental Health: Learning keeps your brain active, improving cognitive functions and promoting mental well-being.

# Personal Fulfillment: Gaining knowledge or mastering new skills leads to personal satisfaction and growth.

# How to Embrace Lifelong Learning
# Set Goals: Focus on specific areas of interest or career growth.
# Online Courses: Utilize platforms like Coursera, Udemy, or edX for flexible learning.
# Read Regularly: Books, articles, and research papers are great sources of new knowledge.
# Join Communities: Engage in discussions, forums, and learning groups to broaden perspectives.
# In summary, lifelong learning enhances your adaptability, career success, and personal fulfillment, making it a crucial part of growth in today’s fast-paced world.'''}
    
# ]

def home(request):
    topics = Topic.objects.all()
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    
    rooms = Room.objects.filter(topic__name__icontains = q)
    
    rooms_count = rooms.count()
    
    context= {'rooms': rooms, 'topics': topics, 'rooms_count': rooms_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=int(pk))
    print(room)
    # room = None
    # for r in rooms:
    #     if r['id'] == int(pk):
    #         room = r
            
    context = {'room': room }           

    return render(request, 'base/room.html',context)

def create_room(request):
    
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance= room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/update_room.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=int(pk))
    
    if request.method == 'POST':
        
        room.delete()
        return redirect('home')
    
    context = {'obj': room}

    return render(request, 'base/delete.html',context)