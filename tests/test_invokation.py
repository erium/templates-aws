import pytest
from pathlib import Path
from copy import deepcopy

from utilities.collect_templates import collect_templates
from utilities.apply_template import apply_template

from tests.path_helper import template_repo_path


all_templates = collect_templates(template_repo_path)


replacements = {
    "{{user.name}}": "Tester McTestee",
    "{{user.initials}}": "TM",
}


@pytest.mark.parametrize(
    "template",
    sum([category["templates"] for category in all_templates["categories"]], [])
)
def test_invoke_template(template, tmpdir):
    # put in tmpdir as directoryPath in unix format
    outpath = Path(tmpdir).resolve().as_posix()
    local_replacements = {"{{directoryPath}}": outpath, **replacements}

    # put in replacements
    template = deepcopy(template)
    for key, value in template["automaticArguments"].items():
        for to_replace, replace in local_replacements.items():
            if to_replace in value:
                new_value = value.replace(to_replace, replace)
                template["automaticArguments"][key] = new_value

    # make source path into unix format
    template["automaticArguments"]["source_directory"] = (
        Path(template["automaticArguments"]["source_directory"]).as_posix())

    # apply template

    apply_template(template_repo_path, template)
