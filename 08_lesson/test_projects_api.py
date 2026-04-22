import pytest


class TestProjectsAPI:
    """Тесты для API проектов YouGile"""

    # ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_positive(self, api_client, test_project_data):
        """
        Позитивный тест: POST /api-v2/projects
        Создание проекта с валидными данными
        """
        response = api_client.create_project(test_project_data)

        assert response.status_code == 201
        response_data = response.json()
        assert 'id' in response_data

        # Очистка: удаляем созданный проект
        project_id = response_data['id']
        api_client.delete_project(project_id)

    def test_get_project_positive(self, api_client, test_project_data):
        """
        Позитивный тест: GET /api-v2/projects/{id}
        Получение существующего проекта по ID
        """
        # Создаем проект для теста
        create_response = api_client.create_project(test_project_data)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        try:
            # Получаем проект
            response = api_client.get_project(project_id)

            assert response.status_code == 200
            response_data = response.json()
            assert response_data['id'] == project_id
            assert 'title' in response_data
        finally:
            # Очистка: удаляем проект
            api_client.delete_project(project_id)

    def test_update_project_positive(self, api_client, test_project_data):
        """
        Позитивный тест: PUT /api-v2/projects/{id}
        Обновление названия существующего проекта
        """
        # Создаем проект для теста
        create_response = api_client.create_project(test_project_data)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        try:
            # Обновляем проект
            new_data = {"title": "Updated Project Name"}
            response = api_client.update_project(project_id, new_data)

            assert response.status_code == 200
            response_data = response.json()
            assert response_data.get('title') == new_data['title']
        finally:
            # Очистка: удаляем проект
            api_client.delete_project(project_id)

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_negative_no_title(self, api_client):
        """
        Негативный тест: POST /api-v2/projects
        Создание проекта без обязательного поля title
        """
        invalid_data = {}
        response = api_client.create_project(invalid_data)

        # Ожидаем ошибку валидации (400 Bad Request)
        assert response.status_code == 400
        assert 'error' in response.json()

    def test_create_project_negative_empty_title(self, api_client):
        """
        Негативный тест: POST /api-v2/projects
        Создание проекта с пустым названием
        """
        invalid_data = {"title": ""}
        response = api_client.create_project(invalid_data)

        assert response.status_code == 400
        assert 'error' in response.json()

    def test_get_project_negative_not_exists(self, api_client):
        """
        Негативный тест: GET /api-v2/projects/{id}
        Получение несуществующего проекта
        """
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(fake_id)

        assert response.status_code == 404
        assert 'error' in response.json()

    def test_get_project_negative_invalid_id_format(self, api_client):
        """
        Негативный тест: GET /api-v2/projects/{id}
        Получение проекта с некорректным форматом ID
        """
        invalid_id = "not-a-uuid"
        response = api_client.get_project(invalid_id)

        # API может вернуть 400 или 404
        assert response.status_code in [400, 404]

    def test_update_project_negative_not_exists(self, api_client):
        """
        Негативный тест: PUT /api-v2/projects/{id}
        Обновление несуществующего проекта
        """
        fake_id = "00000000-0000-0000-0000-000000000000"
        update_data = {"title": "New Title"}
        response = api_client.update_project(fake_id, update_data)

        assert response.status_code == 404
        assert 'error' in response.json()

    def test_update_project_negative_empty_title(self, api_client, test_project_data):
        """
        Негативный тест: PUT /api-v2/projects/{id}
        Обновление проекта с пустым названием
        """
        # Создаем проект для теста
        create_response = api_client.create_project(test_project_data)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        try:
            # Пытаемся обновить с пустым названием
            invalid_data = {"title": ""}
            response = api_client.update_project(project_id, invalid_data)

            assert response.status_code == 400
            assert 'error' in response.json()
        finally:
            # Очистка: удаляем проект
            api_client.delete_project(project_id)
