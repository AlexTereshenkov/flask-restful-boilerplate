# Overview

This is a boilerplate Flask app featuring use of `flask-restful` extension.
This app can be used as a template for building RESTful APIs.

# Development setup

The project requires Python 3.6+.

```bash
python3 -m venv appenv  # create a venv
source appenv/bin/activate  # activate the venv
(appenv) pip install -r requirements.txt  # install dependencies
(appenv) python src/app.py  # start the app
```

# Usage

To call the API endpoints, you need to get the application running following 
the development setup steps.
You can use any client capable of submitting HTTP requests and parsing responses.
The token value is required and is found in the `api/secrets.py` file 
to ease development and testing.
The port the API will be accessible at is defined in `src/config.py` and is `6040`.
[Postman](https://www.getpostman.com/) and [Insomnia](https://insomnia.rest/) 
are free clients providing a pleasant user interface and automation. 
To use the service from a command line, you can use `curl`:

```bash
# To print more detailed information about the response returned, pass `-i` flag.
curl -i 'http://localhost:6040/getSumValue?values=1,2,3,4,5' -H "token: h5ibqG91ZfISOdIJeCss"
# {"code": 200, "message": "Done", "result": 15}
```

and to do it programmatically, e.g. using Python, you can use any package capable of submitting HTTP requests such as `requests`:

```python
from requests import get
res = get(f'http://localhost:6040/getSumValue?values=1,2,3,4,5', headers={"token": "h5ibqG91ZfISOdIJeCss"})
print(res.json())
# {'code': 200, 'message': 'Done', 'result': 15}              
```

# Running tests

Tests expect to have the Flask web app up and running.

```
(appenv) pytest ./tests --tb=line -rA
```

# Running typechecks and linting

```bash
mypy .
flake8 .
```
