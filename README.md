overall app arch: microservices
individual microservices: MVC backend
    - Separation of Concerns: Views only handle HTTP requests; all logic is in the services.py (controller).
    - Easier Testing: can unit-test services without worrying about Django views.
    - More Scalable: can swap Django REST views with GraphQL or another API layer without affecting business logic.
react frontend
![alt text](IMG20250210133845.jpg)