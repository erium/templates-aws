import os
import inspect


this_file_path = inspect.getfile(inspect.currentframe())
template_repo_path = os.path.abspath(
    os.path.join(this_file_path, os.path.pardir, os.path.pardir))
print(template_repo_path)

