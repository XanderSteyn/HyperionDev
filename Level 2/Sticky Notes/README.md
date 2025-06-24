<h1 align="center">
  <img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Tasks/Sticky%20Notes.svg" alt="Sticky Notes"/><br>
</h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Features.svg" alt="Features" height="25px"/>

- **Create Notes:** Add new sticky notes with title and content
- **View Notes:** List and review saved notes in a clean, sorted view
- **Edit Notes:** Modify existing notes with pre-filled forms and validations
- **Delete Notes:** Safely remove notes with a confirmation prompt
- **User Friendly:** Intuitive design, built-in error handling, and seamless navigation
- **Well Tested:** Includes automated unit and integration test coverage
- **Clear Architecture:** RESTful URLs, structured app design, and supporting design diagrams
- **Admin Interface:** Manage notes through Django's built-in admin at `/admin/` (after creating a superuser)

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Technologies%20Used.svg" alt="Technologies Used" height="30px"/>

- **Python** – Core programming language
- **Django** – Web framework for rapid, secure development
- **SQLite** – Default development database (easy setup, portable)
- **HTML5 & CSS3** – Markup and styling for modern, responsive UI
- **Bootstrap & Font Awesome** – UI components and icons (included via CDN links in base template)
- **Django Test Framework (unittest)** – Automated unit and integration testing

<h2></h2>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Setup%20Instructions.svg" alt="Setup Instructions" height="30px"/>

#### 1. Clone the repository
```
git clone https://github.com/XanderSteyn/HyperionDev
```

#### 2. Change to the project directory
```
cd "HyperionDev\Level 2\Sticky Notes\sticky_notes_application"
```

#### 3. Create a virtual environment
- **Windows:**
  ```
  python -m venv venv
  ```
- **macOS/Linux:**
  ```
  python3 -m venv venv
  ```

#### 4. Activate the virtual environment
- **Windows (Command Prompt):**
  ```
  .\venv\Scripts\activate.bat
  ```
- **Windows (PowerShell):**
  ```
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```
  source .\venv/bin/activate
  ```

#### 5. Install dependencies
```
pip install -r requirements.txt
```

#### 6. Apply migrations
```
python manage.py migrate
```

#### 7. Create superuser
```
python manage.py createsuperuser
```

#### 8. Run the development server
```
python manage.py runserver
```

#### 9. Access the app
Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### 10. Access the Django Admin Interface
After creating a superuser, you can manage notes through the Django admin panel:

Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)<br>
Log in with your superuser credentials.

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/Repos/Running%20Tests.svg" alt="Running Tests" height="30px"/>

To run the full test suite and ensure everything works as expected:
```
python manage.py test notes
```

To run a specific test file, use the following command format:

- **Models Tests:**
  ```
  python manage.py test notes.tests.test_models
  ```

- **Views Tests:**
  ```
  python manage.py test notes.tests.test_views
  ```

- **Templates Tests:**
  ```
  python manage.py test notes.tests.test_templates
  ```

- **Admin Tests:**
  ```
  python manage.py test notes.tests.test_admin
  ```

- **Edge Cases Tests:**
  ```
  python manage.py test notes.tests.test_edge_cases
  ```

- **URLs Tests:**
  ```
  python manage.py test notes.tests.test_urls
  ```

Unit tests can be found within the `notes` app directory (`notes/tests`), following Django best practices.

<h1></h1>

<img src="https://github.com/XanderSteyn/xandersteyn/blob/main/IGNORE/Headers/License.svg" alt="License" height="25px"/>

This repository is protected by a custom license. See the [LICENSE](https://github.com/XanderSteyn/HyperionDev/blob/main/LICENSE) file for details.

Unauthorized copying or submission of this work for academic purposes is prohibited.
