
## Setup instructions

First, clone the repository to your local machine:

```bash
git clone https://github.com/Tanjib-Rafi/Local-Artwork-Showcase.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python3 manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at:
 http://127.0.0.1:8000/api/

## Database Setup

In the settings.py make sure database setup for Postgresql is correct:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'artwork',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

## API Endpoints

|ACTIONS|HTTP METHODS|ENDPOINTS|
|-----------------|---|--------------|
|REGISTER FOR AN ACCOUNT|POST|/api/register/|
|LOGIN WITH AN ACCOUNT|POST|/api/login/|
|LOGOUT OF AN ACCOUNT|GET|/api/logout/|
|View Artist Profile |GET|/api/profile/<int:pk>/|
|Create Artwork |POST|/api/artworks/|
|View, Delete, Update|POST|/api/artworks/<int:pk>/|

Json body data for Create artwork
```JSON
{
  "title": "Demo Title",
  "description": "This is demo description.",
  "creation_date": "2024-04-05T12:00:00Z",
  "image_url": "https://xyz.com/1.jpg"
}
```
>Artist/User Authentication:

-RegisterView handles user registration using a serializer.
-LoginView handles TokenObtainPairView for authentication and user ID extraction.
-LogoutView handles token blacklisting for secure logout.

>Artist Profile:

-ArtistProfileDetail uses RetrieveUpdateAPIView for retrieving and updating authenticating artist profiles.

>Autenticated Artist's Artwork:

-ArtworkListCreateView allows listing and creating artworks using ListCreateAPIView.
-ArtworkRetrieveUpdateDestroyView handles retrieving, updating, and deleting artworks using RetrieveUpdateDestroyAPIView.
