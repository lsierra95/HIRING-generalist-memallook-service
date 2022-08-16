# "Memallook" Service

This service maintains a stateful record of memory allocations performed in a buffer and returns it when requested

## Requirements

Python 3.7+

## Running the Service

Before running the service, you will need two things on your machine:

FastAPI:
`$ pip install fastapi`

An ASGI web server. In this case I used Uvicorn:
`$ pip install uvicorn[standard]`

Now to run the app, enter the following command:
`uvicorn app:app --reload`

Now that your application has successfully started, you can open your browser to
http://127.0.0.1:8000/docs. This will take you to the interactive API
documentation

## The Approach
### Design Decisions

The biggest decision was, honestly, how to properly implement the service with the most appropriate data structures. I ended up reading up a lot on heap memory and it gave me more insight on how memory is managed and just how to take into consideraton all these factors for the memory allocation sim (i.e. accounting for previously deallocated blocks of memory)

### Frameworks & Libraries

I chose to use FastAPI over more popular Python web frameworks, like Flask, for a couple of reasons:

1. Performance - as stated in its name, it's fast
2. Data Validation - it's built to detect any invalid datatypes during the run and returns
3. API Documentation - FastAPI uses Swagger UI to document APIs in an interactive way 

### References
[FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)