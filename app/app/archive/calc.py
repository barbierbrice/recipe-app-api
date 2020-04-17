def add(x, y):
    """add two number together"""
    return x + y


def subtract(x, y):
    """ subtract two numbers"""
    return (y-x)

# dans le terminal :
# cd /Users/bricebarbier/Course/recipe-app-api
# docker-compose run app sh -c "python manage.py test && flake8"
# s'il manque quelque chose --> installer le build :
# docker-compose build
