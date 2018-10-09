# Spock project

# Useful Tools
- Postman for api check


# How to start
1) Start the docker image
2) Start the backend


# Start the PostreSQL server
```
docker-compose up --force-recreate
```

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

## default user
```
psql -h 0.0.0.0 -U postgres -W postgres -d postgres
```