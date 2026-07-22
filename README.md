# Personal Data Lab
> [!NOTE]  
> This project is being developed as a learning exercise to strengthen development and programming skills. As it evolves through successive stages, some features and implementation details may change.
## Overview
The **Personal Data Lab** is a CLI based application which is designed to
keep track of daily habits of the user by storing their personal data.

It asks the user to enter entries such as ***'sleep hours'***, ***'workout minutes'***, ***'expense'*** and ***'mood'*** regularly (which are used to form a **record**) in order to store, analyze and showcase user's productivity through mathematical operations and visualizations.
> [!IMPORTANT]  
> Any kind of data exploration (such as Analytics or Visualization) is still under development.
## Features
- **Add** new personal records.
- **View** previously saved records.
- **Edit** existing records.
## Project Structure
- `tests/` contains automated unit tests for application's components.
- `date_utils.py` handles date related operations.
- `input_handler.py` handles user inputs.
- `main.py` is an application entry point.
- `models.py` defines shared data models used throughout the application.
- `presentation.py` deals with the CLI output presentation.
- `records.py` manages record creation.
- `storage.py` handles all the storage related operations.
## How To Run
1. Clone this repository.  
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app.
```bash
python -m src.main
```
## Testing
Application testing covers:  
- Input validation 
- Storage operations
- Record management
- Date utilities
- Application workflows

Execute the following command from the project's **root directory** to run tests:
```bash
python -m pytest
```
## Roadmap
✅ Simple Data Entry Tool  
📍 Data Exploration  
⏳ Data Visualization  
⏳ Database Integration  
⏳ Predict Insights

## Technologies Used
- Python
- JSON
- Pytest
## Contributions
Author - [Uday Kashyap](https://github.com/uday-kashyap)