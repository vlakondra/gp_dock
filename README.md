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