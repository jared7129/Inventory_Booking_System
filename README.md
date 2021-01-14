# Inventory Booking System 

This app will allow you to add and update Members, Inventory Items and Bookings. You can also access the API endpoints to retreive data, and also cancel/delete bookings

### Processes and services:
 1. A booking is done with the member and inventory item attached to the booking.
 2. Once a booking is created, the booking count for the member will increase by 1, and the inventory for that inventory item will decrease by 1.
 3. A booking cannot be done if a member has a maximum of 2 bookings to their name, or if an inventory item has 0 in the remaining count. The validation for this is done in the models.py file.
 4. The app also allows for importing and exporting of data, however if using the system to import, the fields in the csv file will need to match the fields in the model. I have provided a Members.csv file and a Inventory.csv file.
 
 To run this in your system:
 
 Clone this repo in your system:
 ```
 git clone https://github.com/jared7129/Inventory_Booking_System.git
 ```
 Get inside the repo, type this is terminal:
 ```
 cd Inventory_Booking_System
 ```
 Create a virtual environment inside the repo:
 ```
 python3 -m venv .venv
 ```
 After that activate the virtual environment by typing:
 ```
 source .venv/bin/activate
 ```
 Next step is to install all the dependencies into your virtual environment:
 ```
pip3 install Django==3.0.1
pip3 install django-jsonfield==1.4.0
pip3 install django-import-export
 ```
You can also run the following if you are missing any dependencies:
 ```
pip install requirements.txt
 ```

 Next get into the project directory by typing:
 ```
 cd Ibs
 ```
 Type the following commands to run migrations:
 ```
 python3 manage.py makemigrations
 python3 manage.py migrate
 ```
 Now to access the admin page before running the server create a superuser:
 ```
 python3 manage.py createsuperuser
 fill the details :
 username: <ur choice>
 email: <optional>
 password: <password>
 confirm password: <confirm the password>
 ```
 After filling all these to run the project:
 ```
 python3 manage.py runserver
 ```
the app runs in the development mode.
Open http://127.0.0.1:8000/admin to view it in the browser.

The page will reload if you make edits.
You will also see any lint errors in the console.

### Accessing the API
The following urls will allow you to access the relevant data via the API:

 ```
 http://127.0.0.1:8000/inventory/ - View a list of inventory items
 ```

 ```
 http://127.0.0.1:8000/member/ - View a list of members
 ```

  ```
 http://127.0.0.1:8000/booking/ - View a list of bookings
 ```

  ```
 http://127.0.0.1:8000/booking_details/<pk> - View a single booking. pk indicates a reference number. From here you can also delete/cancel a booking
 ```

 ### Importing/Exporting data

 You can also use import and export data for members or inventory items via the backend, or you can run the following commands which are located in the management/commands folder:

```
pip install django-import-export
```

```
python manage.py import_inventory
 ```

```
python manage.py import_members
 ```







 
 
