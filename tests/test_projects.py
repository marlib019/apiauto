"""
(c) Copyright Jalasoft. 2023

logger.py
    configuration of logger file
"""

import requests
import pytest


class TestProjects:
    """
    Class for something
    """
    def __init__(self):
        """Function that does something"""
        print("Setup class")
        # arrange of test
        self.token = "b410ca19bf765a9729b71f4c2ee0a23ade334f24"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        self.url_base = "https://api.todoist.com/rest/v2/projects"

    @pytest.fixture
    def test_get_all_projects(self):
        """
        test for get all projects
        :return:
        """
        # act
        response = requests.get(self.url_base, headers=self.headers, timeout=10)
        print(response.json())
        list_projects = response.json()
        id_project = list_projects[1]["id"]
        # assert
        assert response.status_code == 200
        return id_project

    @pytest.mark.smoke
    @pytest.mark.create
    @pytest.mark.parametrize("name", ["Project 2", "Project3", "Project 4"])
    def test_create_project(self, name):
        """
        test to verify creation of project
        :return:
        """
        body_project = {
            "name": name
        }
        response = requests.post(self.url_base, headers=self.headers, data=body_project, timeout=10)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_get_project(self, test_get_all_projects):
        """fixing method"""
        url = self.url_base + "/" + test_get_all_projects
        response = requests.get(url, headers=self.headers, timeout=10)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.update
    def test_update_project(self, test_get_all_projects):
        """updating method"""
        url = self.url_base + "/" + test_get_all_projects
        data_update = {
            "name": "Project 2",
            "color": "red"
        }
        response = requests.post(url, headers=self.headers, data=data_update, timeout=10)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_delete_project(self, test_get_all_projects):
        """something related to the method"""
        url = self.url_base + "/" + test_get_all_projects
        response = requests.delete(url, headers=self.headers, timeout=10)
        # print(response.json())
        assert response.status_code == 204

    @classmethod
    def teardown_class(cls):
        """teardown"""
        print("teardown")
