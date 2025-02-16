# Room Finder Website for Students

A web application tailored for students to find affordable and convenient accommodations near their schools, colleges, or universities. The platform simplifies the process of connecting students with landlords offering budget-friendly rooms.
## Features

- Student-Friendly Search and Filters
- Property Listings
- Interactive Map
- Responsive Design
## Tech Stack

**Client:** HTML,Javascript,TailwindCSS

**Server:** Django
## Team Member

- Mahesh Kapadi
- Manoj Kumar Kanu Baniya
- Guru Prakash Gupta
- Abishek Kumar Gupta

## Setup Instructions

Follow these steps to set up the project on your local machine.


### 1. Clone the Repository
#### Clone this repository to your local system:
```bash
git clone https://github.com/manojbaniya68/Room-Finder.git
```
### 2. Create and Activate a Virtual Environment
#### Create a virtual environment and activate it:
On Windows:
```bash
python -m venv venv
.\venv\Scripts\Activate
```
On macOS/Linux:
```bash
python3 -m venv venv 
source venv/bin/activate
```
### 3. Install Dependencies
#### Install Django and other dependencies:
On Windows:
```bash
pip install django
pip install django-tailwind
pip install 'django-tailwind[reload]'
```
On macOS/Linux:
```bash
pip3 install django 
pip3 install django-tailwind
pip3 install 'django-tailwind[reload]' 

```
### 4. Run the Server
#### Start the development server:
On Windows:
```bash
cd .\Room-Finder
py .\manage.py runserver
```

On macOs/Linux:
```bash
cd Room-Finder  
python3 manage.py runserver 
```
### 5. Run the Tailwind Server
#### Run the TailwindCSS build process in a separate terminal:
On Windows:
```bash
.\venv\Scripts\Activate
cd .\Room-Finder
```
#### For first time setup only,install tailwind css
```bash
py manage.py tailwind install
```
#### Start the TailwindCSS build process:
```bash
py manage.py tailwind start
```

## Troubleshooting

If you encounter issues during setup, try the solutions below:

### 1. Python is Not Recognized
Ensure Python is installed and added to your PATH.
Verify the installation by running:
```bash
python --version
```
If Python is not installed, download it from python.org.
### 2. Error: Execution Policy Restricts Script Activation (Windows)
If you see an error like:
```bash
File cannot be loaded because running scripts is disabled on this system.
```
Open Windows PowerShell as Administrator and run:
```powershell
Set-ExecutionPolicy RemoteSigned
```
When prompted, confirm the change by typing Y and pressing Enter.
## Documentation

[Presentation Slide](https://linktodocumentation)
## Feedback

If you have any feedback, please reach out to us at studentroomfinder@gmail.com




