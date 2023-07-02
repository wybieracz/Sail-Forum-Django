# Django-Sail-Forum
Django based discussion forum for Scripting Languages Lecture on Gdansk University of Technology.

## General information
* Classic discussion forum
* Admin users can create new boards.
* Users start new topic under existing boards.
* Users can post replies to existing topics.

## Technologies used
* Python
* Django

## Functionalities
* User signup
* User login
* Password reset
* Boards creation
* Topic creation
* Replies to topic
* Roles based avatars

## Database schema
![db](/ss/Database.png)

## Site map
![map](/ss/Map.png)

## Screenshots
![login](/ss/login.png)
![register](/ss/register.png)
![main](/ss/main.png)
![post](/ss/post.png)
![reply](/ss/reply.png)

## Instruction
1. Install Python 3, Git.
2. Clone repo.
3. Run run `pip install -r requirements.txt`.
4. Generate Django secret key for project. Run `python generate_secret_key.py` and copy the output string.
5. Paste it in .env file at `SECRET_KEY`.
6. Run `python manage.py migrate` to apply database migrations.
7. Create a user `python manage.py createsuperuser`.
8. Run live server `python manage.py runserver`.
9. Open in browser `127.0.0.1:8000/`.
