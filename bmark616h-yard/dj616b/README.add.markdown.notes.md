
add martor markdown editor.


z dj6

dc up

https://devdj.198.144.183.160.nip.io/admin2323/mark616/bookmk/45340/change/

https://github.com/agusmakmun/django-markdown-editor

add martor to requ...



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@  
#@  
#@  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2023-01-31[Jan-Tue]22-52PM 


albe@racknerd-4f4016:/ap/dkr/dkrcollection617a/bmark616h-yard/dj616b$ dc up
WARNING: Found orphan containers (dj616b_nginx_1, dj616b_djprod_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Recreating dj616b_djdev_1 ... done
Attaching to dj616b_djdev_1
djdev_1  | Docker container started entrypoint.sh
djdev_1  | Performing system checks...
djdev_1  |
djdev_1  | Traceback (most recent call last):
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/utils.py", line 66, in __getitem__
djdev_1  |     return self._engines[alias]
djdev_1  | KeyError: 'django'
djdev_1  |
djdev_1  | During handling of the above exception, another exception occurred:
djdev_1  |
djdev_1  | Traceback (most recent call last):
djdev_1  |   File "manage.py", line 15, in <module>
djdev_1  |     execute_from_command_line(sys.argv)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
djdev_1  |     utility.execute()
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/__init__.py", line 413, in execute
djdev_1  |     self.fetch_command(subcommand).run_from_argv(self.argv)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 354, in run_from_argv
djdev_1  |     self.execute(*args, **cmd_options)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/commands/runserver.py", line 61, in execute
djdev_1  |     super().execute(*args, **options)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 398, in execute
djdev_1  |     output = self.handle(*args, **options)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/commands/runserver.py", line 96, in handle
djdev_1  |     self.run(**options)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/commands/runserver.py", line 105, in run
djdev_1  |     self.inner_run(None, **options)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/commands/runserver.py", line 118, in inner_run
djdev_1  |     self.check(display_num_errors=True)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 423, in check
djdev_1  |     databases=databases,
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/checks/registry.py", line 76, in run_checks
djdev_1  |     new_errors = check(app_configs=app_configs, databases=databases)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/contrib/admin/checks.py", line 78, in check_dependencies
djdev_1  |     for engine in engines.all():
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/utils.py", line 90, in all
djdev_1  |     return [self[alias] for alias in self]
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/utils.py", line 90, in <listcomp>
djdev_1  |     return [self[alias] for alias in self]
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/utils.py", line 81, in __getitem__
djdev_1  |     engine = engine_cls(params)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/backends/django.py", line 25, in __init__
djdev_1  |     options['libraries'] = self.get_templatetag_libraries(libraries)
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/backends/django.py", line 43, in get_templatetag_libraries
djdev_1  |     libraries = get_installed_libraries()
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/backends/django.py", line 108, in get_installed_libraries
djdev_1  |     for name in get_package_libraries(pkg):
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/django/template/backends/django.py", line 121, in get_package_libraries
djdev_1  |     module = import_module(entry[1])
djdev_1  |   File "/usr/local/lib/python3.7/importlib/__init__.py", line 127, in import_module
djdev_1  |     return _bootstrap._gcd_import(name[level:], package, level)
djdev_1  |   File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
djdev_1  |   File "<frozen importlib._bootstrap>", line 983, in _find_and_load
djdev_1  |   File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
djdev_1  |   File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
djdev_1  |   File "<frozen importlib._bootstrap_external>", line 728, in exec_module
djdev_1  |   File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/rest_framework/templatetags/rest_framework.py", line 11, in <module>
djdev_1  |     from rest_framework.compat import apply_markdown, pygments_highlight
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/rest_framework/compat.py", line 72, in <module>
djdev_1  |     import markdown
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/markdown/__init__.py", line 29, in <module>
djdev_1  |     from .core import Markdown, markdown, markdownFromFile  # noqa: E402
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/markdown/core.py", line 26, in <module>
djdev_1  |     from . import util
djdev_1  |   File "/usr/local/lib/python3.7/site-packages/markdown/util.py", line 87, in <module>
djdev_1  |     INSTALLED_EXTENSIONS = metadata.entry_points().get('markdown.extensions', ())
djdev_1  | AttributeError: 'EntryPoints' object has no attribute 'get'
albe@racknerd-4f4016:/ap/dkr/dkrcollection617a/bmark616h-yard/dj616b$

=================================================


