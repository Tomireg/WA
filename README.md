Access the app through this link: https://wa-74im.onrender.com

The app is aweather report application. Visitors can register and login. There is an option to search for any city around the world and get the city’s weather as a result.

Deployment:
The website is deployed on render.com. It connects to a PostgreSQL database that is also hosted on render.com. It uses the following public repository on Github to deploy: https://github.com/Tomireg/WA

Settings for the web service on render:
Set name to: WA
Set region to: Frankfurt(EU central)
Set branch to: main
Set root directory to: weather_app
Set build command to: ./build.sh
Set start command to: python -m gunicorn weather_app.asgi:application -k uvicorn.workers.U
Set auto-deploy to: yes
Set deploy hook to: https://api.render.com/deploy/srv-cs577l23esus73aqngb0?key=7cE8zKQfpn0

Environment variables on render:
DATABASE_URL: postgresql://weatherdb_4sdn_user:tGzIzQbxqrxIZvNl9JsyEaAhWWumzsmP@dpg-cs573fi3esus73aqkp9g-a/weatherdb_4sdn
SECRET_KEY: b0f3de4ca8a601d3da0a93985d23e39a
WEB_CONCURRENCY: 4
