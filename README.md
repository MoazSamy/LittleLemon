# Meta Back-End Developer Capstone

![Coursera](https://img.shields.io/badge/Coursera-0747a6?style=flat&logo=coursera&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=flat&logo=meta&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)

Building RESTful APIs using [Django Rest Framework](https://www.django-rest-framework.org/) connected to a [MySQL](https://dev.mysql.com/downloads/) as part of the [Meta Back-End Developer Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer) teached by [Meta](https://www.facebook.com/business/learn/back-end-back-end-developer-certificate-coursera).

<p align="center">
    <a href="https://www.credly.com/org/facebook-blueprint/badge/meta-back-end-developer-certificate">
        <img src="images/meta-backend-cert.png" width="30%" height="30%"/>
    </a>
</p>

## How to install this project?

1. Clone the project to your local folder using `git clone`.
2. Change the MYSQL credentials in the Settings.py file in the LittleLemon directory to match your credentials.
3. Make sure that you have `pipenv` installed using `pip install pipenv`.
4. Run `pipenv install` in the project directory. (Hint: the directory that includes the piplock file)
5. Run `pipenv shell` and ensure that you are in the virtual environment.
6. Run both the migrations commands `python manage.py makemigrations` and `python manage.py migrate`
7. Run the server using `python manage.py runserver`
8. Run the tests using `python manage.py test`

## Little Lemon Restaurant APIs 

1. ### Booking API

  - Use the following endpoint `/restaurant/` to see the static html page served. NOTE: this API only supports authenticated users.
  - Use the following endpoint `/restaurant/booking/tables` with GET method to see the current bookings, as well as add some new booking timings to the database using POST method . NOTE: this API only
     supports authenticated users.

2. ### Menu Items API
  
  - Use the following endpoint `/api/menu-items/` with GET method to see the available menu items, as well as add some new items to the menu using POST method. NOTE: this API only supports authenticated users.
  - Use the following endpoint `/api/menu-items/<int:pk>/` to see a singular menu item, as well as being able to update or remove it. NOTE: this API only supports
     authenticated users.

3. ### Authentication API (Djoser)

  - Use the following endpoint `/auth/users/` with GET method to view all the current registered users, as well as add a new user using POST method.
  - Use the following endpoint `/auth/users/me` with the GET method to view the details of the current logged in user.
  - Use the following endpoint `/auth/token/login` with POST method to get the token that is associated with the credentials given.
  - Use the following endpoint `/auth/token/logout` with POST method to delete the token that is associated with the credentials given.

## Testing

- Run the following command `python manage.py test` to test the tests written in the files [test_models.py](https://github.com/MoazSamy/LittleLemon/blob/main/LittleLemonAPI/test_models.py) and [test_views.py](https://github.com/MoazSamy/LittleLemon/blob/main/LittleLemonAPI/test_views.py). The tests include testing creating an object using the model and retrieving it, and testing the MenuItemsView.
