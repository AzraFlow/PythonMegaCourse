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
         'help for methods in module objects': 'help([module].[object].[method])',
         }

# Opens a file in 'w' (truncate then write) mode using the with context manager
with open('cli_doc_notes.txt', 'w') as cli_file:
    for key, value in notes.items():
        cli_file.write(key + ': ' + value + '\n\n')
