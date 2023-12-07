# Install virtual environment in the root of the project
python3 -m venv venv or python -m venv venv (if you have it installed on your machine)

# Activate virtual environment 
- Linux and MacOS:
  source venv/bin/activate
- Microsoft Windows:
  venv\Scripts\activate

# Install packages
- One by one:
  pip install package_name (optional ==, >, >=, <, <= version)
- If there is requirements file:
  pip install -r requirements_file_name.txt

# Deactivate virtual environment
deactivate

# Generating requirements file
Once the venv is activated, type pip freeze > requirements_name_file.txt
