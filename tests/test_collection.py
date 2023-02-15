from tests.json_structure import Template
from tests.expected_templates import expected_templates
from tests.path_helper import template_repo_path
from utilities.collect_templates import collect_templates


def test_collect_templates():
    collect_templates(template_repo_path)


def test_valid_template_categories():
    templates = collect_templates(template_repo_path)

    for category in templates["categories"]:
        assert set(category.keys()) == {"name", "description", "templates"}


def test_valid_template_data():
    templates = collect_templates(template_repo_path)

    for category in templates["categories"]:
        for template in category["templates"]:
            Template(**template)


def test_all_templates_found():
    templates = collect_templates(template_repo_path)

    category_names = {cat["name"] for cat in templates["categories"]}
    assert category_names == set(expected_templates.keys())

    for category in templates["categories"]:
        template_names = {temp["name"] for temp in category["templates"]}
        expected_names = set(expected_templates[category["name"]])
        assert template_names == expected_names
