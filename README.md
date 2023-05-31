# api_app

* Microservice project toturail

```bash
git clone https://github.com/hojat-gazestani/api_app.git

source ./api_env/bin/activate
cd api_project
docker build  -t api_app .
docker run -d --hostname ApiAPP40 -p 8040:8004 api_app
docker run -d --hostname ApiAPP42 -p 8041:8004 api_app
docker run -d --hostname ApiAPP42 -p 8042:8004 api_app
```

```bash
curl http://127.0.0.1:8040
curl -X POST -H "Content-Type: application/json" -d '{"name": "Hojat Gazestani", "age": 35}' http://0.0.0.0:8040/api/add/
```