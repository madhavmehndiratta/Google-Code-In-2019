import requests
from ansible.module_utils.basic import *

def get_response(url):
	try:
		response = requests.get(url)
	except requests.HTTPError as error:
		return error.code
	return response.status_code

def main():

	module = AnsibleModule(argument_spec={'url':{'required': True, 'type': 'str'}})
	status_code = get_response(module.params['url'])
	response = {"status": status_code}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
