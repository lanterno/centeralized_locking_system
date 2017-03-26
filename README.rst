CLS
==============================

Centeralized Locking System


Main Concept
-------------
This locking system depends on the concept that each microservice has to get permission first, before
starting using any resource in the system, assuming that NO MICROSERVICE LOCKS TWO RESOURCES AT THE SAME TIME
OR THAT IT LOCKS ALL THE RESOURCES IT NEEDS ALL THE TIME OF THE PROCESS.

The system has a very basic architecture that consists of a database model that represents Resources, and a RestFul
API that has two endpoints, one to hold a resource, and another to release the resource.

To Run:
----------


    pip install -r requirements.txt
    
    python3 manage.py migrate
    
    python3 runserver
    

the endpoints available are

/api/resources/request/{PK}/

and

/api/resources/release/{PK}/

- You need the corresponding PK for the resource name.

Future Improvments
^^^^^^^^^^^^^^^^^^

- use names instead of PK for finding the resource.
- Add authentication that considers each microservice as a user.
- Consider that microservices would need to lock more than one resource at the same time.
