# Reddit Clone
![GitHub Logo](/test/coverage.svg)

Simple Reddit clone made on [Flask](http://flask.pocoo.org/) using [Reddit API](https://www.reddit.com/dev/api/).

## Installation

Simply clone the repository or download zip: 
```sh
$ git clone git@github.com:MagiskBoy/RedditClone.git
```
After download, setup your virtual environment (I used Python venv)
<br>
Go to the folder with the project and type the following in your terminal:
```sh
$ python -m venv venv
```

Activate it:
```sh
$ source venv/bin/activate
```
For Windows Command Line:
```
>venv\Scripts\activate
or
>venv\Scripts\activate.bat
```

Next install requirements for the project and make sure that you are doing it in virtual environment:
```sh
$ pip install -r requirements.txt
```
Simply type to run the app:
```sh
$ python run.py
```
After that you should see something like:
```sh
 * Serving Flask app "reddit" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Navigate to your server address in your preferred browser.
```sh
http://127.0.0.1:5000/
```


##  Docker
If you have [Docker](https://www.docker.com/) installed on your machine type the following:
```sh
$ docker run -p 4000:80 ersain666/reddit-clone:1.0
```

After that you should see something like this in your terminal:
```sh
 * Serving Flask app "reddit" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```
Verify the deployment by navigating to your server address in your preferred browser.
```sh
http://0.0.0.0:80/
```


If you are troubling to connect the server try this:
```sh
http://192.168.99.100:4000
```


For windows users:
If you want to close the app, CTRL+C is not enough
<br>
You should type into command line:
```sh
$ docker container ls 
```
Result:
```sh
$ docker container ls
CONTAINER ID        IMAGE                        COMMAND             CREATED             STATUS              PORTS                  NAMES
29180bb6ba2f        ersain666/reddit-clone:1.0   "python run.py"     2 minutes ago       Up About a minute   0.0.0.0:4000->80/tcp   nostalgic_goodall
```
Simply type this to stop:
```sh
$ docker container stop <CONTAINER ID>
```




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors
* [Ersain Dynmukhamed](https://github.com/MagiskBoy)
