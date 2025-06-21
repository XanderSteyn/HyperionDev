<h1 align="center">
  <img src="/IGNORE/Sticky Notes/Heading.svg" alt="Sticky Notes"/><br>
</h1>

<img src="/IGNORE/Sticky Notes/Features.svg" alt="Features" height="25px"/>

- **Create Notes:** Add new sticky notes with title and content.
- **View Notes:** List and review saved notes in a clean, sorted view.
- **Edit Notes:** Modify existing notes with pre-filled forms and validations.
- **Delete Notes:** Safely remove notes with a confirmation prompt.
- **User Friendly:** Intuitive design, built-in error handling, and seamless navigation.
- **Well Tested:** Includes automated unit and integration test coverage.
- **Clear Architecture:** RESTful URLs, structured app design, and supporting design diagrams.

<h1></h1>

<img src="/IGNORE/Sticky Notes/Technologies Used.svg" alt="Technologies Used" height="30px"/>

- **Python** – Core programming language
- **Django** – Web framework for rapid, secure development
- **SQLite** – Default development database (easy setup, portable)
- **HTML5 & CSS3** – Markup and styling for modern, responsive UI
- **Bootstrap & Font Awesome** – UI components and icons (via CDN)
- **Django Test Framework (unittest)** – Automated unit and integration testing

<h2></h2>

<img src="/IGNORE/Sticky Notes/Setup Instructions.svg" alt="Setup Instructions" height="30px"/>

#### 1. Clone the repository
```bash
git clone https://github.com/XanderSteyn/HyperionDev/
```

#### 2. Change to the project directory
```bash
cd HyperionDev\Level 2\Sticky Notes
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

#### 6. Apply migrations
```bash
python manage.py migrate
```

#### 7. Run the development server
```bash
python manage.py runserver
```

#### 8. Access the app
Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

<h1></h1>

<img src="/IGNORE/Sticky Notes/Running Tests.svg" alt="Running Tests" height="30px"/>

To run the full test suite and ensure everything works as expected:
```bash
python manage.py test notes
```

<h1></h1><br>

<img src="/IGNORE/Header/License.svg" alt="License" height="25px"/>

This repository is protected by a custom license. See the [LICENSE](LICENSE) file for details.

Unauthorized copying or submission of this work for academic purposes is prohibited.
