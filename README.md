# Python Domain Driver Design Basic Template

## Stack

- Python 3.11+
- Prisma for Python
- FastAPI
- MySQL

# Getting Started

### Install Requirements:

```pip install -r requirements.txt```

### Run with:

```uvicorn main:app --host 0.0.0.0 --port 5000 --reload```

## Built in endpoints

#### Client

| METHOD 	|  RESOURCE  	|          FULL URL         	|
|:------:	|:----------:	|:-------------------------:	|
| POST   	| CREATE     	| /api/v1/client/create     	|
| GET    	| GETCURRENT 	| /api/v1/client/getCurrent 	|

#### User

| METHOD 	|  RESOURCE  	|          FULL URL         	|
|:------:	|:----------:	|:-------------------------:	|
| POST   	| LOGIN      	| /api/v1/user/login      	|
| GET    	| GETCURRENT 	| /api/v1/user/getCurrent 	|
