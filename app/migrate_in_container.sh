#!/bin/bash
docker exec -it farm-planner-app sh -c "python manage.py migrate"