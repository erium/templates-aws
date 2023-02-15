import json
import os


def collect_templates(repo_path):

    template_categories = {}

    for dirpath, dirnames, filenames in os.walk(repo_path):
        if ("cookiecutter.json" in filenames) and ("template.json" in filenames):
            with open(os.path.join(dirpath, "template.json"), "r") as f:
                template_data = json.load(f)

            # if the cookiecutter covers a whole template category
            if (("name" in template_data) and
                    ("description" in template_data) and
                    ("templates" in template_data)):
                category = {key: template_data[key] for key in ("name", "description")}
                category["templates"] = []

                templates = template_data["templates"]
            else:
                templates = [template_data]
                # if the cookiecutter is a single template, the parent dir must contain the category

                category_json = os.path.join(dirpath, os.pardir, "template_category.json")
                with open(category_json, "r") as f:
                    category = json.load(f)

            if category["name"] not in template_categories:
                template_categories[category["name"]] = category

            for template in templates:
                # inject directory_argument
                template["automaticArguments"]["source_directory"] = os.path.relpath(dirpath, start=repo_path)
                template["automaticArguments"]["target_directory"] = "{{directoryPath}}"
                template_categories[category["name"]]["templates"].append(template)

    all_templates = {"categories": []}
    for category in template_categories.values():
        all_templates["categories"].append(category)

    return all_templates


