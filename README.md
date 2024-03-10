# Docker Exercise

Base on the requirment here are the activities performed:

- [Dockerfile](./Dockerfile) available here.
- [docker-compose.yml](./docker-compose.yml) available here.

In `docker-compose.yml`, you can modify the following lines to add your custom message/greeting.

```
    environment:
      - GREETING=the custom greeting
```

To run docker-compose, run this command:

`docker-compose up --build`

`--build` ensures you are getting your latest code always.

# Scripting Exercise

- [script.py](./script.py) helps in acheiving this whole job, it creates `files` directory in current folder and also verifies the SHA256 match for each `id` and its `name` retrieved from our API.
the script has been writen in Python, and to have the result you have to run the following command in the directory
before that, you have to download all the dependencies listed in the requirment.txt file
```
    `pip install -r requirment.txt`
```
then run the below command to generate the file
```
    `Python script.py`
```

# Reverse Proxy 

- The proxy section in docker-compose file will run an nginx container to establish reverse proxy for our application.

- Nginx needs the [nginx.conf](./nginx.conf) file. In this file we are routing every request coming to nginx on port `80` to our application `app` (hostname == service name in docker-compose file) at port `5000`.
