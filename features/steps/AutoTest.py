from behave import *
import random


def rand():
    rnd = random.randint(1, 10000)
    return rnd


url = "http://qa-assignment.oblakogroup.ru/board/:alexandr_vizgunov" + str(rand())


@given("Открыть страницу")
def step_impl(context):
    context.driver.get(url)


@then("Должна открыться страница")
def step_impl(context):
    heading = context.driver.find_element_by_class_name("title")
    assert heading.is_displayed()


@when("Нажать на кнопку +")
def step_impl(context):
    button = context.driver.find_element_by_id("add_new_todo")
    button.click()


@step("Ввести название задачи '{text}'")
def step_impl(context, text):
    task = context.driver.find_element_by_id("project_text")
    task.clear()
    task.send_keys(text)


@step("Выбрать категорию '{text}'")
def step_impl(context, text):
    category = context.driver.find_element_by_id("select2-select_category-container")
    category.click()
    category_name = context.driver.find_element_by_xpath('//*[contains(text(), "' + text + '")]')
    category_name.click()


@step("Нажать на кнопку OK")
def step_impl(context):
    ok_button = context.driver.find_element_by_id("submit_add_todo")
    context.driver.execute_script("arguments[0].click();", ok_button)


@then("На странице есть задача '{text}'")
def step_impl(context, text):
    tasks = context.driver.find_elements_by_id("todo_text")
    elements = list(filter(lambda x: x.find_element_by_tag_name("label").text == text, tasks))
    assert len(elements) == 1
    assert elements[0].is_displayed()


@step('Ввести название задачи (например "!@#$%^")')
def step_impl(context):
    task = context.driver.find_element_by_id("project_text")
    task.clear()
    task.send_keys("!@#$%^")


@step("Задача не выполнена '{text}'")
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue"]/ancestor::div//*[contains(text(), "' + text + '")]')
    id = task.get_attribute("id")
    task = context.driver.find_element_by_id(id)
    assert task.is_selected() is False


@when("Изменить статус задачи '{text}'")
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ id = "todo_check"]/ancestor::div//*[contains(text(), "' + text + '")]')
    task.click()


@then("Задача выполнена '{text}'")
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue checked"]/ancestor::div//*[contains(text(), "' + text + '")]')
    id = task.get_attribute("id")
    task = context.driver.find_element_by_id(id)
    assert task.is_selected()


@step("Задача выполнена '{text}'")
def step_impl(context, text):
    task = context.driver.find_element_by_xpath(
        '//*[ @ class = "icheckbox_square-blue checked"]/ancestor::div//*[contains(text(), "' + text + '")]')
    id = task.get_attribute("id")
    task = context.driver.find_element_by_id(id)
    assert task.is_selected()


@step("Ввести заголоваок категории '{text}'")
def step_impl(context, text):
    new_category = context.driver.find_element_by_id("project_title")
    assert new_category.is_displayed()
    new_category.clear()
    new_category.send_keys(text)


@then("На странице есть  категория '{text}'")
def step_impl(context, text):
    categories = context.driver.find_elements_by_class_name("shadow_todos")
    elements = list(filter(lambda x: x.find_element_by_tag_name("h2").text == text, categories))
    assert len(elements) == 1
    assert elements[0].is_displayed()
