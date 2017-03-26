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


Future Improvments
^^^^^^^^^^^^^^^^^^
- Add authentication that considers each microservice as a user.
- Consider that microservices would need to lock more than one resource at the same time.
