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


# def remove_sync(domain, sync_id):
#     url = "http://{}/rest/api/removesync/".format(domain)
#     values = {'username': username}
#     data = str(values).replace("'", '"')
#     response = requests.post(url, data=data)
#     return response


def get_token(domain, username):
    url = "http://{}/rest/api/get-token/{}".format(domain, username)
    response = requests.get(url)
    return response.json()['token']
