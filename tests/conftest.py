from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture
def client():
    app_module.activities.clear()
    app_module.activities.update(deepcopy(INITIAL_ACTIVITIES))

    with TestClient(app_module.app) as test_client:
        yield test_client

    app_module.activities.clear()
    app_module.activities.update(deepcopy(INITIAL_ACTIVITIES))