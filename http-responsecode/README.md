# HTTP Status Response Code Ansible Module #

An ansible module to check the HTTP Status Response Code of a Website.

## Introduction ##

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

1. Informational responses (100–199),
2. Successful responses (200–299),
3. Redirects (300–399),
4. Client errors (400–499),
5. Server errors (500–599).

Here is a list of some common HTTP Status Response Codes:
1. 200 OK
2. 301 Moved Permanently
3. 302 Found
4. 304 Not Modified
5. 307 Temporary Redirect
6. 400 Bad Request
7. 401 Unauthorized
8. 403 Forbidden
9. 404 Not Found
10. 500 Internal Server Error
11. 503 Service Unavailable
12. 550 Permission denied

## Usage ##

Edit the url in the mail.yml

```
url: http://github.com/MR-M1M3
```

Save the file and then run the playbook.

```
$ ansible-playbook main.yml
```

## Tutorial ##
[![asciicast](https://asciinema.org/a/YGjaI7Hg1WflFaFUARjUUAZpk.png)](https://asciinema.org/a/YGjaI7Hg1WflFaFUARjUUAZpk)
