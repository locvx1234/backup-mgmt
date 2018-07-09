import requests


def add_agent(domain, username):
    url = "http://{}/rest/api/adduser/".format(domain)
    values = {'username': username}
    data = str(values).replace("'", '"')
    response = requests.post(url, data=data)
    return response


def list_agent():
    pass


def remove_agent(domain, username):
    url = "http://{}/rest/api/removeuser/".format(domain)
    values = {'username': username}
    data = str(values).replace("'", '"')
    response = requests.post(url, data=data)
    return response
