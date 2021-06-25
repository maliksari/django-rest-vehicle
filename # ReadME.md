# Project Structure

## URLS 
- /vehicle
    - /GET
    - /POST
- /vehicle-detail/id
    - /PUT
    - /DELETE

- /vehicle-model
    - /GET
    - /POST
- /vehicle-model-detail/id
    - /PUT
    - /DELETE

    ## -----------------------------------------

    -  /vehicle
        - /vehicle
            - /__init__py
            - /asgi.py
            - /settings.py
            - /urls.py
            - /wsgi.py
        - /vehicleapp
            - /api
                - /__init__py
                - /serializer.py
                - /urls.py
                - /views.py
            - /__init__py
            - /admin.py
            - /apps.py
            - /models.py
            - /tests.py
            - /urls.py
            - /views.py
        -/manage.py

