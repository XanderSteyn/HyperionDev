<h1 align="center">
  <img src="/IGNORE/Sticky Notes/Heading.svg" alt="Sticky Notes"/><br>
</h1>

<img src="/IGNORE/Sticky Notes/Features.svg" alt="Features" height="20px"/>

- **Create Notes:** Add new sticky notes with a title and content. Validation ensures all required fields are filled and title length is within limits.
- **Read/View Notes:** See all notes in a list (newest first) and view full details of any note.
- **Update/Edit Notes:** Edit existing notes with pre-filled forms and validation.
- **Delete Notes:** Delete notes with a confirmation prompt to prevent accidental loss.
- **User-Friendly Interface:** Clean, modern UI with clear navigation and feedback messages.
- **Robust Validation:** Server-side validation for required fields and maximum title length.
- **Error Handling:** 404 error pages for non-existent notes (view, edit, delete).
- **Comprehensive Unit Tests:** Automated tests for all CRUD operations, validation, edge cases, and model methods.
- **RESTful URL Structure:** Clean, descriptive URLs for all note operations.
- **Design Diagrams:** Includes class, sequence, use case, and CRUD matrix diagrams for documentation.

<h1></h1>

<img src="/IGNORE/Sticky Notes/Technologies Used.svg" alt="Technologies Used" height="25px"/>

- **Python** – Core programming language
- **Django** – Web framework for rapid, secure development
- **SQLite** – Default development database (easy setup, portable)
- **HTML5 & CSS3** – Markup and styling for modern, responsive UI
- **Bootstrap & Font Awesome** – UI components and icons (via CDN)
- **Django Test Framework (unittest)** – Automated unit and integration testing

<h2></h2>

<img src="/IGNORE/Sticky Notes/Setup Instructions.svg" alt="Setup Instructions" height="25px"/>

#### 1. Clone the repository
```bash
git clone <your-repo-url>
```

#### 2. Change to the project directory
```bash
cd sticky_notes
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

<img src="/IGNORE/Sticky Notes/Running Tests.svg" alt="Running Tests" height="25px"/>

To run the full test suite and ensure everything works as expected:
```bash
python manage.py test notes
```

<h1></h1><br>

<p align="center">
  <img width="15px" alt="Thank You!" title="Thank You!" src="https://i.imgur.com/g5yEIOu.png" />
  <strong>Thank you for visiting. I look forward to connecting and creating meaningful value together.</strong>
</p>

<h1></h1>

<img src="/IGNORE/Header/License.svg" alt="License" height="25px"/>

This repository is protected by a custom license. See the [LICENSE](LICENSE) file for details.

Unauthorized copying or submission of this work for academic purposes is prohibited.
