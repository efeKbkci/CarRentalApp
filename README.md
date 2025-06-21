# Car Rental Application

## Getting Started

Follow the steps below to set up and run the application in a virtual environment.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/efeKbkci/CarRentalApp
cd CarRentalApp
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Make sure you have `pip` installed, then run:

```bash
pip install -r requirements.txt
```

---

## Running the Application

To run the application:

```bash
python -B main.py
```

### Optional Command-Line Arguments:

| Argument | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| `-a`     | Starts the application with admin credentials pre-filled in the login window. |
| `-n`     | Starts the application with a non-admin test user credentials pre-filled.     |

Example usage:

```bash
python -B main.py -a
```

or

```bash
python -B main.py -n
```
