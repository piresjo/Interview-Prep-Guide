# System Design Interview - The Insider's Guide - Chapter 1 Notes

## Database Basics

Your web application will mostly require data storage. You **might** be able to get away with using cookies to store data, but that can't be used for any data that needs to be persisted. You will need a database.

### SQL vs. NoSQL

You have two families of databases to choose from: SQL or NoSQL.

SQL databases (aka relational databases) is a database system where data is represented in tables and relations can be formed between the various tables. This comes in the form of `join` statements.

NoSQL databases (aka non-relational databases) don't define relationships. So, `join` statements usually aren't possible. These databases usually get grouped into these categories:

- key-value stores
- graph stores
- column stores
- document stores

Your use case determines which DB is better. Some use cases for SQL databases are:

- You need to search for data that depends on other data (this is where `join` statements come in)
- General purpose web apps. Given the decades of use as an industry standard, SQL databases make for a good default.

As for NoSql databases, these are good if:

- Your app requires extremely low latency
- The data you have is unstructured
- The data has no relation with each other
- You only need t6o serialize and deserialize data
- You need to store significant amounts of data

### Database Replication

Having a single database creates a single point of failure. This can take the whole application down. We can better distribute the load for an optimal user experience by replicating databases.

This can be further optimized by establishing clear roles for the multiple databases. Since most web applications can be at least somewhat usable if the data reading related operations are still functional, it makes sense to have specific read-only databases and specific read-write databases. In this scenario, the read-write database is copied by the read-only databases. The app operations that only require searching for data can use the read-only databases, and the app operations that modify data can use the read-write database.

In terms of handling roles, if the read-write database goes down, a read-only database takes its place and a new read-only database gets added to the application. If a read-only database 

### Database Scaling

## Vertical vs. Horizontal Scaling

Vertical scaling entails increasing the power of a server or a database. Examples of this would be increasing the disk size of a database or using a more powerful processor for a server. This is a much simpler way to scale up, and it's quite good for applications with low traffic. As a basic example, if you have the code for a web application, build that, and get `localhost` up and running, you can scale up your "server" (in this case, your development computer) by using a more powerful computer.

However, if traffic increases, you'll need exponentially more powerful hardware. There is a hard limit to how much you can upgade the hardware of a singer server. This means that if traffic keeps increasing, you'll reach a point where users will experience slowdown. Furthermore, a singler server is a clear single source of failure; if it goes down, the whole application goes down.

This is where horizontal scaling comes in

## Load Balancing

Branching off horizontal scaling, the multiple servers will have to be managed so that no one server is getting excess load. This is where load balancers come in.

There are a few immediate benefits to a load balancer. First, users don't access the servers directly. Second, the single point of failure problem encountered in only doing vertical scaling doesn't exist anymore, since you can move load from one server to another if the former goes down. Finally, load balancers ensure that increased load is shared and no server is under disproportionate stress.

## Caching

A cache is a temporary storage area that stores the result of expensive responses, frequently encountered data, or both. This allows us to reduce latency by reducing the amount of database access, reducing the amount of times endpoints need to be run, or both.

Not all data is optimal for caching. For instance, data that should be persisted needs to be in the DB. Data that is used frequently but modified infrequently is partiocularly good for caching.

Good caching requires good expiration policies. If the expiration time is too small, that will lead to unnecessary database access. If it's too long, the data could become stale or get out of sync with the database. Speaking of removing data, a good cache has a good eviction policy. If the cache is full, to accomodate new entries, old entries are deleted. The policy determines how it's done (least frequerntly used or treating the cache like a queue are commonly used).

## CDNs

If you only have a single server, users farther from the server will encounter a slower experience. CDNs mitigate that by having servers hosting static content (html, javascript, images, etc.) in multiple places, ensuring users aren't that far from a server hosting static content.

An example process of using a CDN is as follows:

- User 1 uses your service to get an image
- The CDN doesn't have said image
- Request is then made to server to get the image
- Image sent to CDN to be stored, then sent to User 1
- User 2 also wants that image
- The CDN returns the stored image, bypassing any need to access the server

Here are some considerations:

- CDNs are run by third-party providers, and that incurs a cost. Consider whether or not your service needs a CDN. If you have a CDN, determine which data is worth storing (consider the principles of caching).
- Speaking of caching, you'll need a good expiration policy
- Need a way to bypass the CDN is the CDN fails.

## Stateless Web Tier

This is particularly helpful for horizontal server scaling. This entails not requiring the server to remember client data (i.e. the state) from one request to the next. This allows clients to use any server in a server cluster, rather than being tied to a specific server.

In a stateful architecture, a user's information is stored in the DB of a certain server. Depending on the client, requests get routed to one server or another. This requires the server to get state information to direct the request correctly. As we increase the number of servers and databases, this process can become convoluted.

This is where stateless architecture comes in. Here, storage is chared by all of the servers. This removes the routing issue in stateful archetecture and allows us to not have to deal with the state.

## Message Queue

Stored in memory, message queues allow us to support asynchronous comminication. It acts as a buffer and distributor of async messages. A producer (within a service, usually) generates the message and publishes it. This ends up in the message queue. Then the consumer (usually in another service), which is subscribed to the message queue, can consume the message.

## In Summary

- Keep web tier stateless
- Build redundancy in every tier
- Cache data as much as you can
- Support multiple data centers
- Host static assets in CDN
- Scale data tier by sharding
- Split tiers into individual services
- Monitor your system and use automation.
