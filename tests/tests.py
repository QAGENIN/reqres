import pytest
from model.pages.create_user_page import CreateUserPage
from model.pages.delete_user_page import DeleteUserPage
from model.pages.list_user_page import ListUserPage
from model.pages.single_user_page import SingleUserPage
from model.pages.update_user_page import UpdateUserPage


@pytest.mark.parametrize('name, job', [('John', 'trader'), ('Иван', 'инвестор')])
def test_create_user(name, job):
    create_user = CreateUserPage()

    create_user.test_user_create_success(name, job)
    create_user.test_user_create_success_without_name()
    create_user.test_user_create_success_without_job()
    create_user.test_user_create_success_without_params()
    create_user.test_user_create_success_schema_validate(name, job)


def test_delete_user():
    delete_user = DeleteUserPage()
    delete_user.test_user_delete_success()


@pytest.mark.parametrize('page', [1, 2])
def test_list_user(page):
    list_user = ListUserPage()

    list_user.test_users_list_page(page)
    list_user.test_users_list_data_count(page)
    list_user.test_users_list_schema_validate()


@pytest.mark.parametrize('user_id', [1, 2])
def test_single_user(user_id):
    single_user = SingleUserPage()

    single_user.test_get_user_success(user_id)
    single_user.test_user_not_found()
    single_user.test_user_json_schema_validate()


@pytest.mark.parametrize('name, job', [('John', 'trader'), ('Иван', 'инвестор')])
def test_update_user(name, job):
    update_user = UpdateUserPage()

    update_user.test_user_update_success(name, job)
    update_user.test_user_update_json_schema_validate()
