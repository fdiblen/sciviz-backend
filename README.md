sciviz-frontend
==================
Backend for sciviz
https://github.com/fdiblen/sciviz-frontend

# How to start
1) Start the docker image
2) Install dependencies
3) Start the server


# 1) Start the PostreSQL server
```
docker-compose up --force-recreate
```

# 2) install Python dependencies
    $ python3 -m venv venv
    $ source ./venv/bin/activate
    $ pip3 install -r requirements.txt


# 3) Start the server
    $ python app.py
Now open your browser and go to http://localhost:5000/ui/ to see the API UI.


# Stop the PostreSQL server
```
docker-compose down --remove-orphans --volumes
```

## cleanup
```
docker-compose rm postgres
docker volume list
docker volume rm (docker volume list -q)
```

# Connection to PostreSQL server
```
psql -h 0.0.0.0 -U spock -W spock -p 5432 -d spock 
psql -h 0.0.0.0 -U postgres -W postgres -d postgres
```

## connect using default postgres user
```
psql -h 0.0.0.0 -U postgres -W postgres -d postgres
```
