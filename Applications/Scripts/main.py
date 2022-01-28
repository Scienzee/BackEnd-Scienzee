from django.db import connection, reset_queries

"""
Docker
sudo docker-compose exec web python manage.py shell

Virtual Env
python manage.py shell
exec(open('Applications/Scripts/main.py').read())
"""


exec(open('Applications/Scripts/Groups.py').read())
exec(open('Applications/Scripts/PublicationCategory.py').read())
exec(open('Applications/Scripts/Area.py').read())
exec(open('Applications/Scripts/SubArea.py').read())
