
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



INSTALLED_EXTENSIONS = metadata.entry_points().get markdown.extensions attributeError EntryPoints object has no attribute get

=================================================


Creating dj616b_djdev_run ... done
Docker container started entrypoint.sh
APScheduler==3.10.0
asgiref==3.6.0
backports.zoneinfo==0.2.1
bleach==6.0.0
certifi==2022.12.7
charset-normalizer==3.0.1
Django==3.2
django-cors-headers==3.13.0
django-environ==0.9.0
django-extensions==3.2.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
gunicorn==20.1.0
idna==3.4
importlib-metadata==6.0.0
Markdown==3.3.4
martor==1.6.16
mysqlclient==2.1.1
PyJWT==2.6.0
pytz==2022.7.1
pytz-deprecation-shim==0.1.0.post0
requests==2.28.2
six==1.16.0
sqlparse==0.4.3
typing_extensions==4.4.0
tzdata==2022.7
tzlocal==4.2
urllib3==1.26.14
webencodings==0.5.1
zipp==3.12.0

albe@racknerd-4f4016:/ap/dkr/dkrcollection617a/bmark616h-yard/dj616b$


=================================================




# Choices are: "semantic", "bootstrap"
MARTOR_THEME = 'bootstrap'

# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False

# Imgur API Keys
# MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
# MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

# Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'     # from webfx
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'                  # default from github
MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://davegg.com'                                      # please change this to your domain

# If you need to use your own themed "bootstrap" or "semantic ui" dependency
# replace the values with the file in your static files dir
# MARTOR_ALTERNATIVE_JS_FILE_THEME = "semantic-themed/semantic.min.js"   # default None
# MARTOR_ALTERNATIVE_CSS_FILE_THEME = "semantic-themed/semantic.min.css" # default None
# MARTOR_ALTERNATIVE_JQUERY_JS_FILE = "jquery/dist/jquery.min.js"        # default None

# URL schemes that are allowed within links
ALLOWED_URL_SCHEMES = [
    "file", "ftp", "ftps", "http", "https", "irc", "mailto",
    "sftp", "ssh", "tel", "telnet", "tftp", "vnc", "xmpp",
]

# https://gist.github.com/mrmrs/7650266
ALLOWED_HTML_TAGS = [
    "a", "abbr", "b", "blockquote", "br", "cite", "code", "command",
    "dd", "del", "dl", "dt", "em", "fieldset", "h1", "h2", "h3", "h4", "h5", "h6",
    "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
    "li", "ol", "optgroup", "option", "p", "pre", "small", "span", "strong",
    "sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul"
]

# https://github.com/decal/werdlists/blob/master/html-words/html-attributes-list.txt
ALLOWED_HTML_ATTRIBUTES = [
    "alt", "class", "color", "colspan", "datetime",  # "data",
    "height", "href", "id", "name", "reversed", "rowspan",
    "scope", "src", "style", "title", "type", "width"
]

# end martor


=================================================



