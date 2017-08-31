# Mash Place UI
[![Build Status](https://travis-ci.org/MashSoftware/place-ui.svg?branch=master)](https://travis-ci.org/MashSoftware/place-ui)
[![Requirements Status](https://requires.io/github/MashSoftware/place-ui/requirements.svg?branch=master)](https://requires.io/github/MashSoftware/place-ui/requirements/?branch=master)

## Getting Started

```
git clone git@github.com:MashSoftware/place-ui.git
cd place-ui
export SECRET_KEY=<your_secret_key>
export PLACE_API_URL=<your_api_url>
export FLASK_APP=mash_place_ui/__init__.py
export FLASK_DEBUG=1

```

## Mash Place API
You will also need a local instance of Mash Place API running, please see the [README](https://github.com/MashSoftware/place-api/blob/master/README.md) for setup instructions and ensure the above `PLACE_API_URL` variable is set.

## Running

```
flask run -p 5001
```
Go to [http://localhost:5001/](http://localhost:5001/)
