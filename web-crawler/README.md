# WEBSITE CRAWLER
A script that finds out all the directories present in the index page.

# Introduction
This is a program used to exploit the Directory Listing Vulnerability. Directory listing is a web server vulnerability that shows a list of all the files and folders present in the server in case an index file, such as index.php, index.html, or default.asp is not present. This might expose critical information to anyone who finds the location. A website spider(Web Crawler) crawls in the website to find all the directory that was mentioned in the index page.

# Requirements
```
1. python3
2. bs4
3. requests
```
# Usage
```
Usage: crawler.py [options]

Options:
  -h, --help         
          show this help message and exit
  -u, --url  
          Specify the URL

```
# Tutorial
[![asciicast](https://asciinema.org/a/TeQ225uxTGU3DbJmDtKnOvpNd.png)](https://asciinema.org/a/TeQ225uxTGU3DbJmDtKnOvpNd)

# Methods to Prevent Directory Listing Vulnerability

##### Note - All this information has been taken from [this blog.](https://www.netsparker.com/blog/web-security/disable-directory-listing-web-servers/) You can view the original blog for more information #####
As a security best practice it is recommended to disable directory listing. You can disable directory listing by creating an empty index file (index.php, index.html or any other extension your web server is configured to parse) in the relevant directory. Though in many cases this is not the best solution because such files are typically forgotten for example when migrating the web application from development to production environments, or when new directories are added.
So you should implement a permanent and secure solution by disabling directory listing at web server level.

#### Disabling Directory Listing on Nginx Server ####

The directory listing feature on Nginx is controlled by the ngx_http_index_module. Directory listing is disabled by default on the Nginx configuration file. However, it is possible to disable directory listing if it was enabled because of a regression or configuration changes.

The Nginx parameter, autoindex, is used together with the location segment to enable or disable the directory listing feature.
How Can We Disable It?

The default configuration file of a Nginx server is called nginx.conf and can be found in /usr/local/nginx/conf, /etc/nginx or /usr/local/etc/nginx. If the default value has been changed, you can see a setting similar to the following:
```
server {
        listen   80;
        server_name  domain.com www.domain.com;
        access_log  /var/...........................;
        root   /path/to/root;
        location / {
                index  index.php index.html index.htm;
        }
        location /somedir {
               autoindex on;
        }
 }
 ```
In this section, the determinant parameter is autoindex on; as we mentioned above. In the above example, the directory listing is configured only for the somedir directory. If no directory is specified (e.g. location / {autoindex on;}), the rule will be applied to all the folders. To disable directory listing, we need to switch the value of the autoindex to off. Do not forget to run the below command in order for changes to go into effect:

```
service nginx start
```
 # Additional Resources
 For more information about disabling Directory Listing Vulnerability, you can refer to this [blog](https://www.netsparker.com/blog/web-security/disable-directory-listing-web-servers/)
