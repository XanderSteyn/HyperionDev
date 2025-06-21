<h1 align="center">
  <img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Tasks/Databases.svg" alt="Bookstore Inventory Management"/><br>
</h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Features.svg" alt="Features" height="25px"/>

- **Add Books:** Add new books to inventory with title, author, and quantity validation
- **Update Books:** Modify existing book information including title, author, and quantity
- **Delete Books:** Safely remove books from inventory with confirmation prompts
- **Search Books:** Find books by ID or title with detailed search results
- **View All Books:** Display all books in both detailed and table formats
- **Author Management:** Manage author information with foreign key relationships
- **Data Validation:** Comprehensive input validation for IDs, titles, quantities, and author references
- **Error Handling:** Robust error handling for database operations and user input
- **User Friendly:** Intuitive console-based interface with clear navigation
- **Well Tested:** Includes comprehensive unit tests for all core functionality
- **Database Integrity:** Foreign key constraints and data validation ensure data consistency

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Technologies%20Used.svg" alt="Technologies Used" height="30px"/>

- **Python** – Core programming language for application logic
- **SQLite** – Lightweight, serverless database for data storage
- **tabulate** – Library for creating formatted tables in console output
- **unittest** – Python's built-in testing framework for automated testing
- **sqlite3** – Python's built-in SQLite database interface

<h2></h2>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Setup%20Instructions.svg" alt="Setup Instructions" height="30px"/>

#### 1. Clone the repository
```bash
git clone https://github.com/XanderSteyn/HyperionDev/
```

#### 2. Change to the project directory
```bash
cd HyperionDev\Level2\Databases
```

#### 3. Create a virtual environment
- **Windows:**
  ```powershell
  python -m venv venv
  ```
- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  ```

#### 4. Activate the virtual environment
- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 5. Install dependencies
```bash
pip install -r requirements.txt
```

#### 6. Run the application
```bash
python shelf_track.py
```

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Running%20Tests.svg" alt="Running Tests" height="30px"/>

To run the comprehensive test suite and ensure everything works as expected:
```bash
python test_shelf_track.py
```

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/License.svg" alt="License" height="25px"/>

This repository is protected by a custom license. See the [LICENSE](LICENSE) file for details.

Unauthorized copying or submission of this work for academic purposes is prohibited. 
