# gp_dock
Эксперименты GitpPod - Docker 

tasks:
  - before:
      pyenv virtualenv venv
  - init: pyenv activate venv
  command: pip install flask
flask грузится, но не в venv,  а в 3.8.12 - корень
-->виртуалenv - ставится, но не активируется    

tasks:
  - before: pyenv virtualenv venv 
  - init: pyenv activate venv
  - command: pip install flask


-->Работает!!
  tasks:
  - name: venv
    before: |
      pyenv virtualenv venv 
      # pyenv shell 3.8.12 ??
      pyenv shell venv
  # - init: source activate venv
  - command: pip install flask


  flask run --host=0.0.0.0


  ЗАРАБОТАЛО
  image:
  file: .gitpod.Dockerfile

github:
  prebuilds:
    # enable for the master/default branch (defaults to true)
    master: true
    # enable for all branches in this repo (defaults to false)
    branches: true
    # enable for pull requests coming from this repo (defaults to true)
    pullRequests: true
    # enable for pull requests coming from forks (defaults to false)
    pullRequestsFromForks: true
    # add a "Review in Gitpod" button as a comment to pull requests (defaults to true)
    addComment: true
    # add a "Review in Gitpod" button to pull requests (defaults to false)
    addBadge: false
    # add a label once the prebuild is ready to pull requests (defaults to false)
    addLabel: prebuilt-in-gitpod

tasks:
  - name: venv
    before: |
      pyenv virtualenv venv 
      source activate venv
      export FLASK_APP=test
      export FLASK_ENV=development
      pip install Flask

    # init: pip install Flask
    command: flask run --host=0.0.0.0


# List the ports to expose. Learn more https://www.gitpod.io/docs/config-ports/
ports:
  - port: 5000
    onOpen: open-preview



"The flask object implements a WSGI application and acts as the central\n    object.  It is passed the name of the module or package of the\n    application.  Once it is created it will act as a central registry for\n    the view functions, the URL rules, template configuration and much more.\n\n    The name of the package is used to resolve resources from inside the\n    package or the folder the module is contained in depending on if the\n    package parameter resolves to an actual python package (a folder with\n    an :file:`__init__.py` file inside) or a standard module (just a ``.py`` file).\n\n    For more information about resource loading, see :func:`open_resource`.\n\n    Usually you create a :class:`Flask` instance in your main module or\n    in the :file:`__init__.py` file of your package like this::\n\n        from flask import Flask\n        app = Flask(__name__)\n\n    .. admonition:: About the First Parameter\n\n        The idea of the first parameter is to give Flask an idea of what\n        belongs to your application.  This name is used to find resources\n        on the filesystem, can be used by extensions to improve debugging\n        information and a lot more.\n\n        So it's important what you provide there.  If you are using a single\n        module, `__name__` is always the correct value.  If you however are\n        using a package, it's usually recommended to hardcode the name of\n        your package there.\n\n        For example if your application is defined in :file:`yourapplication/app.py`\n        you should create it with one of the two versions below::\n\n            app = Flask('yourapplication')\n            app = Flask(__name__.split('.')[0])\n\n        Why is that?  The application will work even with `__name__`, thanks\n        to how resources are looked up.  However it will make debugging more\n        painful.  Certain extensions can make assumptions based on the\n        import name of your application.  For example the Flask-SQLAlchemy\n        extension will look for the code in your application that triggered\n        an SQL query in debug mode.  If the import name is not properly set\n        up, that debugging information is lost.  (For example it would only\n        pick up SQL queries in `yourapplication.app` and not\n        `yourapplication.views.frontend`)\n\n    .. versionadded:: 0.7\n       The `static_url_path`, `static_folder`, and `template_folder`\n       parameters were added.\n\n    .. versionadded:: 0.8\n       The `instance_path` and `instance_relative_config` parameters were\n       added.\n\n    .. versionadded:: 0.11\n       The `root_path` parameter was added.\n\n    .. versionadded:: 1.0\n       The ``host_matching`` and ``static_host`` parameters were added.\n\n    .. versionadded:: 1.0\n       The ``subdomain_matching`` parameter was added. Subdomain\n       matching needs to be enabled manually now. Setting\n       :data:`SERVER_NAME` does not implicitly enable it.\n\n    :param import_name: the name of the application package\n    :param static_url_path: can be used to specify a different path for the\n                            static files on the web.  Defaults to the name\n                            of the `static_folder` folder.\n    :param static_folder: The folder with static files that is served at\n        ``static_url_path``. Relative to the application ``root_path``\n        or an absolute path. Defaults to ``'static'``.\n    :param static_host: the host to use when adding the static route.\n        Defaults to None. Required when using ``host_matching=True``\n        with a ``static_folder`` configured.\n    :param host_matching: set ``url_map.host_matching`` attribute.\n        Defaults to False.\n    :param subdomain_matching: consider the subdomain relative to\n        :data:`SERVER_NAME` when matching routes. Defaults to False.\n    :param template_folder: the folder that contains the templates that should\n                            be used by the application.  Defaults to\n                            ``'templates'`` folder in the root path of the\n                            application.\n    :param instance_path: An alternative instance path for the application.\n                          By default the folder ``'instance'`` next to the\n                          package or module is assumed to be the instance\n                          path.\n    :param instance_relative_config: if set to ``True`` relative filenames\n                                     for loading the config are assumed to\n                                     be relative to the instance path instead\n                                     of the application root.\n    :param root_path: The path to the root of the application files.\n        This should only be set manually when it can't be detected\n        automatically, such as for namespace packages.\n 