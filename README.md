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
