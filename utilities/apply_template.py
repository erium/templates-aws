from typing import Dict, Any, Union
from datetime import datetime
from cookiecutter.main import cookiecutter


def apply_template(
        repo_location: str,
        template_data: Dict[str, Any],
        checkout: Union[str, None] = None):
    """
    Apply a template.

    Parameters
    ----------
    repo_location : str
        The repository containing the template(s).
        Can be a location of disk or a repo URL.
    template_data : dict
        The template data from the templates.json
    checkout : str, optional
        the branch of the repository to check out.

    Returns
    -------

    """

    automatic_arguments = template_data["automaticArguments"]
    user_arguments = {} # these are ignored for now until we have specified their structure further

    arguments = {**automatic_arguments, **user_arguments}
    output_dir = arguments.pop("target_directory")
    # TODO: prepend the mount point to the output dir
    source_dir = arguments.pop("source_directory")
    arguments["timestamp"] = datetime.now().strftime('%Y-%m-%d')

    template_location = cookiecutter(
        repo_location,
        checkout=checkout,
        no_input=True,
        extra_context=arguments,
        replay=None,
        overwrite_if_exists=False,
        output_dir=output_dir,
        config_file=None,
        default_config=False,
        password=None,
        directory=source_dir,
        skip_if_file_exists=False,
        accept_hooks=True,
    )

    # TODO: remove mount point from template_location
    # TODO: process files to open to ensure their location?

    # TODO: the return should always be in accordance to the template wizard

    return template_location
