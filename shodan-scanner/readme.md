# SHODAN SCANNER #

A python based Shodan Scanning Script.

# Introduction #
Shodan is a search engine that lets the user find specific types of computers (webcams, routers, servers, etc.) connected to the internet using a variety of filters. Some have also described it as a search engine of service banners, which are metadata that the server sends back to the client.This can be information about the server software, what options the service supports, a welcome message or anything else that the client can find out before interacting with the server. 

# Requirements #
You can Install the Shodan in your Linux by typing the following command:

```
$ pip3 install shodan
```

Then verify your Private API key. For more information visit https://account.shodan.io

```
$ shodan init <your-api-key>
```

# Usage #
```
$ python3 shodan-scanner.py --help 

Usage: shodan-scanner.py [options]
Options:
  -h, --help     Show this help message and exit
  -k, --key      Specify your Shodan API key

```
Or you can specify your private API key inside the program.

```
$ python3 shodan-scanner.py

Enter you Shodan API key: 
```

After entering your private API key, choose your option.

```
1. Host scan
2. Search for your query
3. My IP
0. Exit
Enter choice :
```

# Tutorial #
[![asciicast](https://asciinema.org/a/6z3qC4Sm3dH6O6rkvwVrgJm61.png)](https://asciinema.org/a/6z3qC4Sm3dH6O6rkvwVrgJm61)
