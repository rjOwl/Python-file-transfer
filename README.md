# Python-file-transfer
Using socket programming in python to send and receive files between 2 PCs in the same network.

# How to run
* **First to run:** python ./serverFtp.py
* **Then run:** python ./clientFtp.py

# Limitations
* Server hosts only one client

# Things to improve
* Allow server to accept more than one client
* Navigating the pc that hosts the serverFtp.py through the client to get files you want to download and not typing 
them inside serverFtp
* Add gui to the client to make it user friendly
* Support resuming

# How to use it globally
**1- Setting up nowdns account**
* Go to now-dns.com and create an account
* Create a new Hostname
* Put the hostname inside clientFtp.py in the IP variable

**2- Open forwording port in your router**
* Open browser and type 192.168.1.1 and login
* Go To forwarding
* Choose a port
* Choose the app name, should be the same as the server, in our case, serverFtp.py
* In client set variable prot=the port you typed in the router settings

**3- Keep the host up-to-date using curl**

curl -u [email]:[password] "https://now-dns.com/update?hostname=[hostname]"

