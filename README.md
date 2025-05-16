# Navisworks Automation API (Flask + Python.NET)

This project provides an automation API for Autodesk Navisworks Manage, built with Python and Flask, designed to streamline the creation of model reviews based on structured input data sent from a PHP system. It integrates a web environment (PHP) with the desktop environment of Navisworks through the Autodesk Automation API, accessed using `.NET` libraries (`controls.dll`, `api.dll`, `automation.dll`) via `pythonnet`.

---

## 📌 Project Overview

The goal is to automate the process of federating engineering models (e.g., `.dwg`) into a single `.nwd` file using Navisworks. A PHP server sends structured JSON data to this Python API, which processes the files and generates a federated model, returning a success or error response.

This is particularly useful in industrial projects where different disciplines (civil, electrical, piping, etc.) produce separate models that need to be merged periodically.

---

## 🔁 Workflow

### 1. Initial Check (PHP ➜ Python)
A PHP script performs a `GET` request to the `/status` endpoint to verify if the Python API is active.

### 2. Data Submission (PHP ➜ Python)
After validation, PHP sends a `POST` request containing the necessary model data in JSON format:
- Contract ID
- Project/discipline area (`os`)
- Folder structure per discipline (`pastas`)

### 3. Model Federation (Python ➜ Navisworks)
The `api-call.py` script receives and serializes this JSON, triggering `open-file.py`, which:
- Launches Navisworks via `NavisworksApplication`
- Recursively traverses folders for `.dwg` files
- Appends them into a unified session
- Saves the federated `.nwd` model to a target location

### 4. Response (Python ➜ PHP)
Once complete, the API returns a JSON response with:
- Return code
- Console output (stdout/stderr)
- Any errors encountered during processing

---

## 🧪 Example JSON Payload

```json
{
   "folder": 
      [
        "Civil", 
        "Electrical", 
        "Structural", 
        "Instrumentation", 
        "Mechanical", 
        "Piping"
      ], 
   "os": "ENG001", 
   "id": "2788"
}
