Access the app through this link: https://wa-74im.onrender.com

The app is aweather report application. Visitors can register and login. There is an option to search for any city around the world and get the city’s weather as a result. I added validation with javascript. I added a feature where the app greets the user in a welcome message on the home page when logged in. I also added visual upgrades to the weather report search in the form of a card style and weather icons. I added a feature that displays the last search the user did under the newest search. The feature remembers the user and it displays the correct information even after logging in and out, so if a user logs out and then back in they will get the last search from their previous session when they make a new search, but they have to make a search first. This new feature is working on the weather search page. I had limited time to work on this beacause of work, I know it’s not an excuse but I had other things distracting me from completing this project. Despite all this, I really hope you like my improvements. I also hosted a new database on render so the app works. Hope you like it.

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
DATABASE_URL: postgresql://wadb_9ggv_user:2VmjFl9TU1dZvuURuuWmEK9sG0LmuIlo@dpg-ct6s2t3qf0us738m0pa0-a/wadb_9ggv
SECRET_KEY: b0f3de4ca8a601d3da0a93985d23e39a
WEB_CONCURRENCY: 4
