# LittleLemon

## How to install this project?

1. Clone the project to your local folder using `git clone`.
2. Make sure that you have `pipenv` installed using `pip install pipenv`.
3. Run `pipenv install` in the project directory. (Hint: the directory that includes the piplock file)
4. Run `pipenv shell` and ensure that you are in the virtual environment.
5. Run the server using `python manage.py runserver`
6. Run the tests using `python manage.py test`

## APIs

### Little Lemon Restaurant APIs

1. Booking API

  1. Use the following endpoint `/restaurant/` to see the static html page served. NOTE: this API only supports authenticated users.
  2. Use the following endpoint `/restaurant/booking/tables` with GET method to see the current bookings, as well as add some new booking timings to the database using POST method . NOTE: this API only
     supports authenticated users.

2. Menu Items API
  
  1. Use the following endpoint `/api/menu-items/ ` with GET method to see the available menu items, as well as add some new items to the menu using POST method. NOTE: this API only supports authenticated users.
  2. Use the following endpoint `/api/menu-items/<int:pk>/` to see a singular menu item, as well as being able to update or remove it. NOTE: this API only supports
     authenticated users.

3. Authentication API (Djoser)

  1. Use the following endpoint `/auth/users/` with GET method to view all the current registered users, as well as add a new user using POST method.
  2. Use the following endpoint `/auth/users/me` with the GET method to view the details of the current logged in user.
  3. Use the following endpoint `/auth/token/login` with POST method to get the token that is associated with the credentials given.
  4. Use the following endpoint `/auth/token/logout` with POST method to delete the token that is associated with the credentials given.

## Testing

- Run the following command `python manage.py test` to test the tests written in the files [test_models.py](https://github.com/MoazSamy/LittleLemon/blob/main/LittleLemonAPI/test_models.py) and [test_views.py](https://github.com/MoazSamy/LittleLemon/blob/main/LittleLemonAPI/test_views.py). The tests include testing creating an object using the model and retrieving it, and testing the MenuItemsView.
