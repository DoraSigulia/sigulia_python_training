from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test1", header="test2", footer="test3"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
