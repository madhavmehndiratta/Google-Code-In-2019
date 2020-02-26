# Ansible Role to Start or Stop a Service #
An ansible role written to start or stop a service.

## Requirements ##

I've added three services. Make sure you have all the three installed for the playbook to run without any errors.
- `httpd`
- `cups`
- `bluetooth`

## Usage ##

To start all the services:

```
$ ansible-playbook start.yml -K
```

To stop all the services:

```
$ ansible-playbook stop.yml -K
```

## Tutorial ##
[![asciicast](https://asciinema.org/a/KaiJMYPu6IlwPzYzi95e4gDJH.png)](https://asciinema.org/a/KaiJMYPu6IlwPzYzi95e4gDJH)
