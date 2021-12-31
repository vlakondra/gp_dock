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