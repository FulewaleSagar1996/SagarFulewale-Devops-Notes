'''

what are the common metrics of promothious which is used by 
devops engg for monitoring and looking dashboard on grafana ?????

System Health:

Machine metrics: CPU usage (percentage and cores), memory usage (percentage and free memory), disk I/O (reads/writes, bytes transferred), network I/O (bytes transferred in/out).
Process metrics: Number of running processes, memory usage per process, CPU usage per process.
Load average: A measure of system load over a period, indicating potential bottlenecks.

General Monitoring:

Uptime: Total time a system or service has been running.
Error rates: Rate of encountering errors during operations.
Gauge metrics: Represent values that can fluctuate, like number of active users, open connections, or available disk space.


Container metrics: CPU and memory usage per container, network traffic, container restarts.
Kubernetes cluster metrics: Node resource utilization (CPU, memory, disk, network), 
pod health status, API server requests.
Cloud provider metrics: Depending on your cloud provider 
(e.g., AWS, Azure, GCP), metrics related to resources like virtual machines, storage, load balancers.


Remember, these are just a few examples. The specific metrics you choose will 
depend on your infrastructure, applications, and monitoring goals.
'''