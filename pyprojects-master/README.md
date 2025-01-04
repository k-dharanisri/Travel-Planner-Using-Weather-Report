 Travel Planner
==============

This is a simple travel planner application built using the tkinter library for the GUI and sqlite3 library to store and retrieve weather data for different cities. The application allows users to input a city and displays the current temperature and whether it is suitable for travel or not.

Created by:
----------
1. Lakshmi Mythryee Kuruguntla
2. Sai Sri Sathvika Chodavarapu
3. Dharani Sri Kolikapogu
4. Chandana Kodari
5. Jyothirmai Kolla
 

Features
--------

* Displays the current temperature and suitability for travel for a given city
* Stores weather data in a SQLite database
* User-friendly graphical user interface

Usage
-----

1. Run the script to start the application
2. Enter the name of the city in the entry widget
3. Click the "Submit" button to display the weather information for the city

Setup
-----

1. Make sure you have Python 3.x installed
2. Install the required libraries by running `pip install tk` in the terminal
3. Run the script using `python travel_planner.py` in the terminal

Dependencies
------------

* Python 3.x
* tkinter
* sqlite3

Screenshots
-----------

![Travel Planner Screenshot](screenshot.png)

Limitations
-----------

* The weather data is static and not updated in real-time
* The application only supports cities that are already in the weather\_data dictionary

Future Improvements
-------------------

* Add real-time weather data using an API
* Add support for more cities
* Add error handling for invalid city inputs
* Add support for different units of temperature (e.g. Celsius, Fahrenheit)
* Add support for different languages

