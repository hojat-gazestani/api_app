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