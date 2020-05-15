#! python3
# File to capture notes on file read/write via code
# to write a text file containing notes about
# cli access to python doc

notes = {'list built in functions': 'dir(__builtins__)',
         'help with __builtins__': 'help(__builtins__)',
         'list all methods within function': 'dir([function])',
         'help with function': 'help([function])',
         'help on function methods': 'help([function].[method])',
         'load additional functions': 'import sys',
         'list modules in sys': 'sys.builtin_module_names',
         'import module': 'import[module name]',
         'list methods in module': 'dir([module])',
         'find python install directory': 'import sys -then- sys.prefix',
         'list objects in modules': 'dir([module])',
         'help for methods in modules': 'help([module].[object].[method])',
         'create virtual environment': 'in project dir -> python -m venv [venv name]',
         'interactive shell n venv': '[venv name]/Scripts/python',
         'activate venv': 'cd to Scripts in venv then -> . activate',
         'deactivate venv': 'type -> deactivate',
         'check path to python': 'where python',
         'see installed packages': 'pip list or pip freeze for requirements.txt format',
         'delete venv': 'delete venv directory or rmdir [venv name] /s',
         'install requirements.txt packages': 'pip install -r requirements.txt',
         'log in to heroku': 'heroku login',
         'define heroku app path': 'heroku git:remote --app azraflow',
         'deploy to heroku': 'git push heroku master (mbuhidar@gmail.com)',
         'open or get info  or logs for heroku app': 'heroku open or heroku info or heroku logs',
         'see class documentation': 'print([class instance].__doc__',
         }

# Opens a file in 'w' (truncate then write) mode using the with context manager
with open('cli_doc_notes.txt', 'w') as cli_file:
    for key, value in notes.items():
        cli_file.write(key + ': ' + value + '\n')
