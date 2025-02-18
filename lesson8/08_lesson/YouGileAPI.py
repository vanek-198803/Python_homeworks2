import requests



class YouGileApi:

    def __init__(self, url):
        self.url = url

# получить ID компании
    def get_company_id(self, login, password, company_name):
        body = {
            "login": login,
            "password": password,
            "name": company_name
            }

        headers = {
            "Content-Type": "application/json"
            }

        response = requests.post(
            self.url + "/api-v2/auth/companies", headers=headers, json=body
        )
        data = response.json()
        content = data.get("content")
        company_id = content[0]["id"]
        return company_id

# Получить список ключей
    def get_auth_keys(self, login, password, company_id):
        auth_body = {
            "login": login,
            "password": password,
            "companyId": company_id
            }

        headers = {
            "Content-Type": "application/json"
            }

        response_auth = requests.post(
            self.url + "/api-v2/auth/keys/get", headers=headers, json=auth_body
        )
        auth_keys = response_auth.json()
        return auth_keys

# создать ключ
    def create_key(self, login, password, company_id):
        auth_body = {
            "login": login,
            "password": password,
            "companyId": company_id
        }

        headers = {
            "Content-Type": "application/json"
            }

        response_key = requests.post(
            self.url + "/api-v2/auth/keys", headers=headers, json=auth_body
        )

        return response_key.json()

    # получить список проектов
    def get_project_list(self, key=123):
        projects_url = self.url + "/api-v2/projects"
        headers = {
            "Content-Type": "application/json"
            }

        headers["Authorization"] = "Bearer " + key
        return requests.get(projects_url, headers=headers)

    # создать проект
    def create_project(self, project_name, key):
        create_project_data = {
            "title": project_name
            }

        headers = {
            "Content-Type": "application/json"
            }

        projects_url = self.url + "/api-v2/projects"
        headers["Authorization"] = "Bearer " + key
        requests.post(projects_url, headers=headers, json=create_project_data)

    # получить информацию о проекте
    def get_project_info(self, id, key):
        get_project_url = self.url + "/api-v2/projects" + "/" + id

        headers = {
            "Content-Type": "application/json"
            }

        headers["Authorization"] = "Bearer " + key

        get_project = requests.get(get_project_url, headers=headers)
        project_info = get_project.json()
        return project_info

    # изменить проект
    def change_project(self, id, auth_key, deleted=None, title=None):
        change_project_url = self.url + "/api-v2/projects" + "/" + id

        headers = {
            "Content-Type": "application/json"
        }

        headers["Authorization"] = "Bearer " + key

        changing = {
            "deleted": deleted,
            "title": title
        }

        change_project = requests.put(
            change_project_url, headers=headers, json=changing
        )
        return change_project.json()
