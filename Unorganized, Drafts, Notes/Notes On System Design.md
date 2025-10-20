# Notes From Notebook On System Design

Three system components

- Frontend
- Data
- Logic

What you want out of a system:

- Scalability
- Speed
- Resilience

Frontend:

- Whatever the client sees
  - In a restaurant setting, this would entail the seats, decor, menu, etc.

Logic:

- API (per the restaurant analogy, the menu would be the API) allows for users to interact with the backend
- Per the restaurant setting, the server is the waiter, handling requests from the customer.

Scalability:

- Per the analogy, with more customers, you'll need more servers. Those servers need a delegate (in a restaurant, a manager; in system design, a load balancer)

Speed:

- More servers -> less latency -> more speed

Persistence/Data Level:

- Data stored permanently
- Making calls to persistence layer is expensive
- Caching will speed up things

Resilience:

- Even if things go wrong, the service will still stay up
- Avoid single points of failure
