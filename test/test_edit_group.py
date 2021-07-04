from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    app.group.edit_first(Group(name="тест", header="тестовый", footer="тестович"))
