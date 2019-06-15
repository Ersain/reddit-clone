# Reddit Clone ![Alt text](/reddit/static/img/reddit.png)
![Alt text](/test/coverage.svg)


Simple Reddit clone made on [Flask](http://flask.pocoo.org/) using [Reddit API](https://www.reddit.com/dev/api/).

## Prerequisites
* Python
* Flask
* Pytest

Optional:
* [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/)
* [Coverage-badge](https://pypi.org/project/coverage-badge/)

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

## Running the tests
Go to the folder "tests" and type the following:
```sh
$ pytest test_<name>.py
```
Optional:
```sh
$ pytest test_<name>.py -v -s
```

Checking test coverage with coverage.py:
```sh
$ coverage run test_<name>.py
$ coverage report
```
In the output you should see something like this:
```sh
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
Absolute path                                                           11      0   100%
Absolute path                                                           16      0   100%
Absolute path                                                            8      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                   35      0   100%
```
## Optional
In order to save the report of the coverage test:
```sh
$ coverage html
```

In order to create a badge of covered tests, first install coverage-badge using pip:
```sh
$ pip install coverage-badge
```
After you installed the package, run coverage.py to generate the necessary coverage data.
```sh
$ coverage run test_<name>.py
$ coverage report
```
Then you can either return the badge SVG to stdout:
```sh
$ coverage-badge
```
…or write it to a file:
```sh
$ coverage-badge -o coverage.svg
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors
* [Ersain Dynmukhamed](https://github.com/MagiskBoy)
