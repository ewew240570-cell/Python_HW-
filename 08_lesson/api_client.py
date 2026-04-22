import requests


class YouGileAPIClient:
    """Page Object для API YouGile"""

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def _request(self, method, endpoint, data=None):
        """Базовый метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=data
        )
        return response

    # Методы для работы с проектами

    def create_project(self, project_data):
        """
        POST /api-v2/projects
        Создание нового проекта
        """
        return self._request("POST", "/projects", project_data)

    def get_project(self, project_id):
        """
        GET /api-v2/projects/{id}
        Получение проекта по ID
        """
        return self._request("GET", f"/projects/{project_id}")

    def update_project(self, project_id, project_data):
        """
        PUT /api-v2/projects/{id}
        Обновление проекта
        """
        return self._request("PUT", f"/projects/{project_id}", project_data)

    def delete_project(self, project_id):
        """
        DELETE /api-v2/projects/{id}
        Удаление проекта (если API поддерживает)
        """
        return self._request("DELETE", f"/projects/{project_id}")
