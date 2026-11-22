# 📁 Smart File Organizer

### ✨ Keep your files organized, automatically!

A lightweight Python CLI application that automatically scans, classifies, and organizes files into categorized folders based on their extensions.

---

## 🚀 About The Project

Tired of having a messy Downloads folder filled with different file types?

**Smart File Organizer** is a simple yet practical Python application designed to make file management easier.

It scans a selected directory, identifies supported file types, and automatically moves them into organized folders — keeping everything clean and structured.

🎯 **Main Goal:** Automate repetitive file organization tasks using Python and clean software design principles.

## 🌟 Key Features

| Feature | Description |
|---|---|
| 🔍 Automatic Scanning | Scans files in the selected directory |
| 🗂️ File Classification | Identifies file types based on extensions |
| 📦 Automatic Organization | Moves files into categorized folders |
| 🔠 Case-Insensitive Detection | Supports uppercase and lowercase extensions |
| 🛡️ Duplicate Protection | Prevents overwriting existing files |
| ⚠️ Unknown File Handling | Skips unsupported file types safely |
| ✅ Path Validation | Checks whether the provided path is valid |
| 🧪 Automated Testing | Includes unit and integration tests |

## 📂 Supported File Types

Files are automatically organized into the following categories:

| Category | Supported Extensions |
|---|---|
| 📄 Documents | `.pdf`, `.docx`, `.txt` |
| 🖼️ Images | `.jpg`, `.png` |
| 🎬 Videos | `.mp4` |
| 🎵 Audio | `.mp3` |

💡 Unsupported file types are skipped and remain in their original location.

## ⚙️ How It Works

The application follows a modular workflow:

```text
       👤 User
          |
          ▼
       main.py
          |
          ▼
      Validator
          |
          ▼
       Scanner
          |
          ▼
      Classifier
          |
          ▼
      Organizer
          |
          ▼
   📁 Organized Files
```

### 📌 Example

**Before Organization**

```text
Downloads/
├── report.pdf
├── photo.jpg
├── movie.mp4
├── song.mp3
└── data.xyz
```

**After Organization**

```text
Downloads/
├── 📄 Documents/
│   └── report.pdf
│
├── 🖼️ Images/
│   └── photo.jpg
│
├── 🎬 Videos/
│   └── movie.mp4
│
├── 🎵 Audio/
│   └── song.mp3
│
└── data.xyz
```

✨ Supported files are moved into their respective folders, while unsupported files remain untouched.

## 🏗️ Project Structure

```text
04-Smart-File-Organizer/
│
├── 📁 src/
│   ├── __init__.py
│   ├── validator.py
│   ├── scanner.py
│   ├── classifier.py
│   └── organizer.py
│
├── 📁 tests/
│   ├── __init__.py
│   ├── test_validator.py
│   ├── test_scanner.py
│   ├── test_classifier.py
│   ├── test_organizer.py
│   └── test_integration.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## 💻 Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd 04-Smart-File-Organizer
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Start the application:

```bash
python main.py
```

Enter the path of the directory you want to organize:

```text
input your path: D:\Downloads
```

**Example Output:**

```text
Moved: 3 Skipped: 1
```

📊 **Output Explanation:**

- `Moved`: Number of successfully organized files.
- `Skipped`: Number of unsupported files or files skipped due to duplicate filenames.

> ⚠️ Note: The application scans only files directly inside the selected directory. Subdirectories are not scanned recursively.

## 🧪 Testing

This project uses **pytest** for unit and integration testing.

Run the complete test suite:

```bash
pytest -v
```

### ✅ Test Results

```text
============================= test session starts =============================

collected 15 items

15 passed

============================== 15 passed ================================
```

**Test Scenarios:**

- ✔️ Valid and invalid directory paths
- ✔️ File scanning and missing directory handling
- ✔️ File extension classification
- ✔️ Unsupported file handling
- ✔️ Duplicate filename protection
- ✔️ Empty directory handling
- ✔️ Complete workflow integration testing

<details>
</details>

## 🛠️ Built With

- 🐍 **Python 3.10** — Core programming language
- 📂 **pathlib** — File and directory path handling
- 🔄 **shutil** — File operations and moving
- 🧪 **pytest** — Automated testing

## 🔮 Future Improvements

Some ideas for future versions:

- 🔍 Recursive directory scanning
- 🗃️ Support for more file extensions
- ⚙️ Customizable file categories
- 📝 Logging and detailed operation reports
- 🖥️ Graphical User Interface (GUI)

## 📜 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.

---

### 💙 Built with Python & a passion for clean code.
