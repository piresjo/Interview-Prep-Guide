# System Design Interview - The Insider's Guide - Chapter 2 Notes

## Reference Latency Numbers

| Operation                                	| Time             	|
|------------------------------------------	|------------------	|
| L1 Cache Reference                       	| 0.5 nanoseconds  	|
| Branch mispredict in CPU                 	| 5 nanoseconds    	|
| L2 cache reference                       	| 7 nanoseconds    	|
| Mutex lock/unlock                        	| 100 nanoseconds  	|
| Main memory reference                    	| 100 nanoseconds  	|
| Compress 1K bytes                        	| 10 microseconds  	|
| Send 2K bytes over 1 Gbps                	| 20 microseconds  	|
| Read 1 MB in memory                      	| 100 microseconds 	|
| Round trip of CDN                        	| 100 microseconds 	|
| Disk seek                                	| 10 millisecond   	|
| Read 1 MB from network                   	| 10 milliseconds  	|
| Read 1 MB from disk                      	| 30 milliseconds  	|
| Send package from CA to Holland and back 	| 150 milliseconds 	|

There are some takeaways of this:

- Memory is fast
- The disk is slow
- Simple compression is fast
- Compress data before sending over the internet
- Avoid disk seeks where possible
- Depending on the location of the data center, there is added latency

## SLAs and Availability Numbers

You want to prioritize availability of your servers. Anything below 99% is unacceptable. Usually, services are up between 99% and 100% of the time, never really reaching 100% exactly. Most service would like at least 99.99% availability (see below for why)

For service providers, the availability you want is defined in an SLA (Service Level Agreement)


| Availability Percentage 	| Downtime Per Day   	| Per Week            	| Per Month     	| Per Year      	|
|-------------------------	|--------------------	|---------------------	|---------------	|---------------	|
| 99                      	| 14.1 minutes       	| 1.68 hours          	| 7.31 hours    	| 3.65 days     	|
| 99.9                    	| 1.44 minutes       	| 10.08 minutes       	| 43.83 minutes 	| 8.77 hours    	|
| 99.99                   	| 8.64 seconds       	| 1.01 minutes        	| 4.38 minutes  	| 52.60 minutes 	|
| 99.999                  	| 864 milliseconds   	| 6.05 seconds        	| 26.30 seconds 	| 5.26 minutes  	|
| 99.9999                 	| 86.40 milliseconds 	| 604.80 milliseconds 	| 2.63 seconds  	| 31.56 seconds 	|

## Tips

- Back-of-the-envelope calculations is more about the process than exact numbers. Round as needed
- Keep your thought process in check by writing your numbers down. Make sure you use units.
- Common asked situations include queries per second, peak QPS, storage, cache, number of servers and similar. It's worth practicing this.