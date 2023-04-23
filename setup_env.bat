@echo off
pip install virtualenv
SET hcdrvenv_path=%cd%\hcdrvenv
if not exist %hcdrvenv_path% (
        virtualenv hcdrvenv
		echo %GenFile% 'hcdrvenv' virtual env has been created 
        goto:install_requriements
    ) else (
        echo %GenFile% here is virtual env
        goto:install_requriements
    )