import tkinter as tk
import sqlite3

image_dict = {}

# Create a dictionary of static weather data for cities
weather_data = {
    "New York": {"temperature": "72°F", "suitable_for_travel": "Yes"},
    "Los Angeles": {"temperature": "85°F", "suitable_for_travel": "Yes"},
    "Chicago": {"temperature": "68°F", "suitable_for_travel": "No"},
    "Miami": {"temperature": "90°F", "suitable_for_travel": "Yes"},
    "Seattle": {"temperature": "60°F", "suitable_for_travel": "No"},
    "London": {"temperature": "63°F", "suitable_for_travel":"No"},
    "Paris": {"temperature": "71°F", "suitable_for_travel":"Yes"},
    "Tokyo": {"temperature": "82°F", "suitable_for_travel":"Yes"},
    "Sydney": {"temperature": "75°F", "suitable_for_travel":"Yes"},
    "Toronto": {"temperature": "69°F", "suitable_for_travel":"No"},
    "Mumbai": {"temperature": "86°F", "suitable_for_travel":"Yes"},
    "Delhi": {"temperature": "96°F", "suitable_for_travel":"Yes"},
    "Beijing": {"temperature": "79°F", "suitable_for_travel":"Yes"},
    "Cairo": {"temperature": "88°F", "suitable_for_travel":"Yes"},
    "Dubai": {"temperature": "95°F", "suitable_for_travel":"Yes"},
    "Moscow": {"temperature": "61°F", "suitable_for_travel":"Yes"},
    "Hyderabad": {"temperature": "63°F", "suitable_for_travel":"Yes"},
    "kolkatta": {"temperature": "71°F", "suitable_for_travel":"Yes"},
    "Agra": {"temperature": "82°F", "suitable_for_travel":"Yes"},
    "Jaipur": {"temperature": "75°F", "suitable_for_travel":"Yes"},
    "Chandigarh": {"temperature": "69°F", "suitable_for_travel":"No"},
    "Varanasi": {"temperature": "86°F", "suitable_for_travel":"Yes"},
    "Banglore": {"temperature": "96°F", "suitable_for_travel":"Yes"},
    "Bhopal": {"temperature": "79°F", "suitable_for_travel":"Yes"},
    "Madurai": {"temperature": "88°F", "suitable_for_travel":"Yes"},
    "Coimbatore": {"temperature": "95°F", "suitable_for_travel":"Yes"},
    "Patna": {"temperature": "61°F", "suitable_for_travel":"Yes"},
    "Pune": {"temperature": "77°F", "suitable_for_travel":"Yes"},
    "Kanpur": {"temperature": "73°F", "suitable_for_travel":"Yes"},
    "Lima": {"temperature": "68°F", "suitable_for_travel":"No"},
    "Nashik": {"temperature": "72°F", "suitable_for_travel": "Yes"},
    "Rajpur": {"temperature": "85°F", "suitable_for_travel": "Yes"},
    "Solapur": {"temperature": "68°F", "suitable_for_travel": "No"},
    "Thiruvananthapuram": {"temperature": "90°F", "suitable_for_travel": "Yes"},
    "Guntur": {"temperature": "60°F", "suitable_for_travel": "No"},
    "Warangal": {"temperature": "63°F", "suitable_for_travel":"No"},
    "Kochi": {"temperature": "71°F", "suitable_for_travel":"Yes"},
    "Durgapur": {"temperature": "82°F", "suitable_for_travel":"Yes"},
    "Nellore": {"temperature": "75°F", "suitable_for_travel":"Yes"},
    "Srinagar": {"temperature": "69°F", "suitable_for_travel":"No"},
    "Ladakh": {"temperature": "60°F", "suitable_for_travel":"No"},
    "Goa": {"temperature": "69°F", "suitable_for_travel":"No"},
    "Andaman": {"temperature": "59°F", "suitable_for_travel":"No"},
    "Bhimavaram": {"temperature": "88°F", "suitable_for_travel":"Yes"},
    "Gangtok": {"temperature": "59°F", "suitable_for_travel":"No"},
    "Udaypur": {"temperature": "61°F", "suitable_for_travel":"No"},
    "Vijayawada": {"temperature": "73°F", "suitable_for_travel":"Yes"},
    "Ongole": {"temperature": "94°F", "suitable_for_travel":"Yes"},
    "Visakhapatnam": {"temperature": "72°F", "suitable_for_travel":"Yes"}
}

def create_weather_database():
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        temperature TEXT NOT NULL,
        suitable_for_travel TEXT NOT NULL
    )
    """)

    for city, data in weather_data.items():
        cursor.execute("""
        INSERT INTO weather (city, temperature, suitable_for_travel)
        VALUES (?, ?, ?)
        """, (city, data["temperature"], data["suitable_for_travel"]))

    conn.commit()
    conn.close()

def show_weather(city):

    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT temperature, suitable_for_travel
    FROM weather
    WHERE city=?
    """, (city,))
    city_data = cursor.fetchone()

    if city_data:
        # Create a new window to display the weather information
        weather_window = tk.Toplevel(root)
        weather_window.title(f"Weather in {city}")

        # Create a label for city name
        city_label = tk.Label(weather_window, text=f"Weather in {city}", font=("Arial", 20))
        city_label.pack(pady=10)

        # Display temperature
        temp_label = tk.Label(weather_window, text=f"Temperature: {city_data[0]}", font=("Arial", 16))
        temp_label.pack(pady=10)

        # Display suitability for travel
        travel_label = tk.Label(weather_window, text=f"Suitable for Travel: {city_data[1]}", font=("Arial", 16))
        travel_label.pack(pady=10)

        #image
        img = tk.PhotoImage(file='travel.png')
        img_label = tk.Label(weather_window, image=img)
        img_label.image = img
        img_label.pack()

    conn.close()


# Create the main window
root = tk.Tk()
root.title("Travel Planner")
icon = tk.PhotoImage(file="travels.png")
root.iconphoto(False, icon)
# root.overrideredirect(True)

# Create a label for the title
title_label = tk.Label(root, text="City Weather Report", font=("Arial", 24))
title_label.pack(pady=20)

# Create an entry widget for the user to input the city
city_entry = tk.Entry(root, font=("Arial", 16))
city_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=lambda: show_weather(city_entry.get()))
submit_button.pack(pady=10)

# Create the weather database
create_weather_database()

#image
img = tk.PhotoImage(file='project.png')
img_label = tk.Label(root, image=img)
img_label.image = img
img_label.pack()

# Start the Tkinter main loop
root.mainloop()