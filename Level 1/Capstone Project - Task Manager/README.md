<h1 align="center">
  <img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Tasks/Task%20Manager.svg" alt="Task Manager"/><br>
</h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Features.svg" alt="Features" height="25px"/>

- **User Authentication:** Secure login system with password masking
- **User Management:** Admin can register new users to the system
- **Task Management:** 
  - Add new tasks with title, description, assigned user, and due date
  - View all tasks in the system
  - View tasks assigned to the current user
  - View completed tasks (admin only)
  - Edit existing tasks (mark as complete, change due date)
  - Delete tasks (admin only)
- **Reporting System:** 
  - Generate comprehensive task overview reports
  - Generate detailed user overview reports
  - Display statistics with percentages and task counts
- **Data Persistence:** Stores data in text files (`tasks.txt`, `user.txt`)
- **Error Handling:** Robust error handling with user-friendly messages
- **Cross-Platform:** Works on Windows, macOS, and Linux

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Technologies%20Used.svg" alt="Technologies Used" height="30px"/>

- **Python** – Core programming language
- **maskpass** – For secure password input with masking
- **datetime** – Date validation and manipulation
- **Text Files** – Simple data storage (`tasks.txt`, `user.txt`)

<h2></h2>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Setup%20Instructions.svg" alt="Setup Instructions" height="30px"/>

#### 1. Clone the repository
```bash
git clone https://github.com/XanderSteyn/HyperionDev/
```

#### 2. Change to the project directory
```bash
cd HyperionDev\Level 1\Capstone Project - Task Manager
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
python task_manager.py
```

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/License.svg" alt="License" height="25px"/>

This repository is protected by a custom license. See the [LICENSE](LICENSE) file for details.

Unauthorized copying or submission of this work for academic purposes is prohibited.
