### Requirements

- Python 3.9+
- pip


### 1. Create and activate a virtual environment
Windows
```
python -m venv venv
venv\Scripts\activate
```

macOS / Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

Make sure you're inside the project folder, then run:

```
pip install -r requirements.txt
```

### 3. Run the application

Start the app with:

```
python app/app.py
```

Or, if you are disabling bytecode creation:
```
python -B app/app.py
```

The app will run on:
```
http://127.0.0.1:5000
```