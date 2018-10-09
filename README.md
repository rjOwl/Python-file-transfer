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

# How to use it Over the internet (globally)
**1- Setting up nowdns account**
* Go to now-dns.com and create an account
* Create a new Hostname
* Open clientFtp.py and set serverIP="the hostname you created"

**2- Setting up your router**
* Open browser and type 192.168.1.1 and login
* Go To port forwarding
* Choose a port number
* In both clientFtp.py and serverFtp.py set variable serverPort=the port number you typed in the previous step
* Choose an app name, should be the same as the server file name, in our case it's serverFtp.py
* Save and exit

**3- Keep the host up-to-date using curl**
* curl -u < email >:< password > "https://now-dns.com/update?hostname=< hostname >"
* For more info go to https://now-dns.com/?m=api


If I missed anything I'll add it.
