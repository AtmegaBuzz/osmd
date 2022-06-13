<p><img src="https://raw.githubusercontent.com/AtmegaBuzz/osmd/main/screenshots/logo.png" alt="logo" width="20%" /></p>

# osmd-cab-app
 one source multiple destination cab app, client project
with integrated chat app , group chat
Created By DTU Student Divyanshu Jain(Algorithm Implementation) + Swapnil Shinde(Frontend + Backend Implementation). Freelance Project for Divyanshu Jain

-Client Requirements 
  1.given a algorithm based on bellman ford graph algorithm
  2.Create a django fullstack app and integrate the algorithm 
  
 Progress : 100% done
 
Technolologies used:
 - Django Backend
 - Html,Css,Js frontend
 - redis and websockets for realtime chat
 - django background processes
 - custom django login model

# How it Works
```This Algorithm for this app is created by NSIT Last year student colaborated with Swapnil Shinde for Implementation. Last year project NSIT```
1.It Is based on Bellman Ford algorith for shortest path | One source Multiple destination.
2.This app takes the Const Starting point which will be same for all users , it can be a organisation or a school.
3.then it optimises the path for one source to multiple destination

# Login
![DeepinScreenshot_select-area_20220207153128](https://user-images.githubusercontent.com/68425016/152768563-2832bac6-9097-4ddc-986d-0df97379b1cd.png)

# Booking Cab
![DeepinScreenshot_select-area_20220207153250](https://user-images.githubusercontent.com/68425016/152768627-17fb7908-3da2-421c-ad3c-7298d8b4b55a.png)

# Your Bookings 
![DeepinScreenshot_select-area_20220207153341](https://user-images.githubusercontent.com/68425016/152768780-d900ff3b-6d50-40f2-9f63-57a98df07017.png)

# Bookings accepted 
![DeepinScreenshot_select-area_20220207153528](https://user-images.githubusercontent.com/68425016/152768864-d36cdfc0-e45b-4d48-8965-b66697a478c4.png)

# Indidual Bookings Info (info of people who will be sitting on same shared cab).
![DeepinScreenshot_select-area_20220207153552](https://user-images.githubusercontent.com/68425016/152769026-09d94746-f7d9-4d7b-9852-8ffad5331587.png)

# Chat Functionality.
![DeepinScreenshot_select-area_20220207153749](https://user-images.githubusercontent.com/68425016/152769124-3713e000-bbe8-46b9-a6a3-2d3c3017045d.png)

#installation
 - clone the repo 
 - install requirements by ```pip install requirements.txt``` 
 - run ```python manage.py makemigrations```
 - run ```python manage.py migrate```
 - run ```python manage.py runserver```

