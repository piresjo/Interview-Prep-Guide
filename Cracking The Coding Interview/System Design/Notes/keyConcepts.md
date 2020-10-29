## Concepts To Consider

### Horizontal and Vertical Scaling
**Vertical Scaling** - Increasing resources of a specific node. For instance, adding more memory to a server.
**Horizontal Scaling** - Increasing the number of nodes. For instance, adding more servers.
### Load Balancer
When scaling, it'd be good to have something to balance the load evenly among all servers being used. This helps prevent servers from crashing, and taking down the system. However, this also requires us to have a bunch of servers with the same code and access to the same data.
### Database Denormalization and NoSQL
The more joins a relational database (like SQL) has, the slower it is. There are ways to mitigate this.

One way is to denormalize the databases. This entails adding redundant information so DB reads are sped up.

You could also not use a relational database (like a NoSQL database)
### Caching
In-memory cache can deliver rapid results. Simply, it's a key-val pair that sits between your app and data storage. An application will first find data in the cache. If it's not there, then the app will look at the data store.
### Async Processing and Queues
Slow ops should be done asynchronously. Ideally, we shouldn't have the user be waiting on a process.

Sometimes, what we can do is preprocess this. For instance, one could have a queue of jobs to be done that update some part of a website. One example of this is updating a forum. The preprocessing comes from having a using an almost-up-to-date cache for rendering the site, rather than waiting to re-render if someone added a new comment.

Sometimes, you'll just have to tell people to wait.
### Networking Metrics
- Bandwidth - Max amount of data that can be transferred in a given unit of time.
- Throughput - Actual amount of data that is transferred
- Latency - How long it takes for data to go from one end to another. In other words, it's the delay between the sender sending information and the receiver receiving it
### MapReduce

MapReduce algorithms have both a map step and a reduce step:

- The map step takes in some data and emits a <key,  value> pair
- The reduce step allows us to take a key and set of associated values and reduces them in some way, emitting a new key and value

This helps us because it allows us to do a lot of processing in parallel, and helps with scaling.