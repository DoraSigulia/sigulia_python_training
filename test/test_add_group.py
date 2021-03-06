from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    simvols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(simvols) for i in range(random.randrange(maxlen))])

teatdate = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
]

@pytest.mark.parametrize("group", teatdate, ids=(repr(x) for x in teatdate))
def test_add_group(app, group):
    old_groups= app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
