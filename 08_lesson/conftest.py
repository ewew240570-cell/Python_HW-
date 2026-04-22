import pytest
import os


@pytest.fixture
def api_token():
    """Фикстура для API токена"""
    token = os.environ.get('YOUGILE_TOKEN')
    if not token:
        pytest.skip("YOUGILE_TOKEN not set. Please set environment variable")
    return token


@pytest.fixture
def base_url():
    """Базовый URL API YouGile"""
    return "https://yougile.com/api-v2"


@pytest.fixture
def api_client(api_token, base_url):
    """Фикстура для API клиента"""
    from api_client import YouGileAPIClient
    return YouGileAPIClient(base_url, api_token)


@pytest.fixture
def test_project_data():
    """Данные для создания тестового проекта"""
    return {
        "title": "Test Project API Auto"
    }
