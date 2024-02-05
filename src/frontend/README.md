# MedNet - Coding Challenge

This project is a user interface and an API that allows the user to converts a given number and his Unit of weight, height or distance to another unit of the same type.

Also allow to add or subtract two numbers on different units of weight, height or distance.

* This project does not have a swagger documentation and only is connected to the API if you use the docker-compose file explained in the main README.md file on the root of the project.
  
# Author

Hi everyone, I am Jordan Escarraga and I am a backend developer, focused on data-driven solutions.

# Local Setup

1. Create a virtual environment, if you don't have one already

        py -m venv mednet-coding-challenge-user-interface
        
or you can use python3

        python3 -m venv mednet-coding-challenge-user-interface

1. Activate the virtual environment

    On Windows powershell

        .\mednet-coding-challenge-user-interface\Scripts\activate

    On Windows using git bash

        source mednet-coding-challenge-user-interface/Scripts/activate

    On linux

        source mednet-coding-challenge-user-interface/bin/activate

2. Install the dependencies

       python3 -m pip install -r requirements.txt

3. **OPTIONAL** if you need add the required packages to the requirements.txt file, run the following command

        pip freeze > requirements.txt

4. **OPTIONAL** If you need to deactivate the virtual environment, run the following command
   
        deactivate

5. Set the environment variable

        export PYTHONPATH=$PWD

# Docker Setup

1 Build the image

        docker build --no-cache -t mednet-code-challenge-ui .

2 Run the container

        docker run -p 8501:8501 --name mednet-code-challenge-ui mednet-code-challenge-ui
