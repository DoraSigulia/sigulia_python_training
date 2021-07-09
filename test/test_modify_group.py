from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
