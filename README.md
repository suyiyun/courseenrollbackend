# course-enroll
Back End Repo for the Full Stack Project course-enroll-management system
# Back-end
AWS endpoint: http://course-enroll-lb-740281198.us-east-2.elb.amazonaws.com:8000/courses/
Local host: http://localhost:8000/
# Virtual environment
mac: 
```
source env/bin/activate 
```
windows: 
```
source env/Scripts/activate
```
# Installation
```
pip install -r requirements.txt
```

check installation by 
```
pip freeze
```

migrate all the databases
```
python3 manage.py migrate 
```


# Quick start
> start server
```
python3 manage.py runserver
```
