# Remote Computer Management Application

## Overview

This project is a remote computer management application developed using Python, Tkinter, and Socket Programming.
The application allows a client machine to connect to another computer within the same Local Area Network (LAN) and perform several remote management operations.

The system follows a client-server architecture:

* **Server**: executes commands on the remote machine
* **Client**: provides a graphical interface for controlling and monitoring the remote machine

The project was refactored using a lightweight MVC-style architecture to improve maintainability and readability while keeping the original business logic.

---

# Features

## Process Management

* View running processes
* Kill selected processes
* Start new processes remotely
* Clear process list

## Application Management

* View running applications
* Kill applications
* Start applications remotely
* Refresh application list

## Screenshot Capture

* Capture remote screen
* Display screenshot in real time
* Save screenshot locally

## Keylogging

* Start keyboard hook
* Stop keyboard hook
* Display logged keystrokes
* Clear keylog data

## Registry Management

* Send `.reg` files remotely
* Create registry keys
* Delete registry keys
* Set registry values
* Delete registry values
* Read registry values

## System Control

* Shutdown remote computer
* Connect/disconnect from server

---

# Technologies Used

* Python
* Tkinter
* Socket Programming
* PIL (Pillow)
* MSS
* Threading

---

# Project Structure

```bash
client/
│
├── controller/
│   ├── main_controller.py
│   ├── apps_running_controller.py
│   ├── processes_running_controller.py
│   ├── keylog_controller.py
│   ├── screenshot_controller.py
│   └── registry_controller.py
│
├── ui/
│   ├── main_window.py
│   ├── apps_running_window.py
│   ├── processes_running_window.py
│   ├── keylog_window.py
│   ├── screenshot_window.py
│   └── registry_window.py
│
├── core/
│   └── client_core.py
│
└── main.py
```

---

# Architecture

The project uses a simplified MVC-inspired architecture:

## UI Layer

Contains only Tkinter widgets and layouts.

Example:

* Buttons
* Entry fields
* Treeviews
* Textboxes

## Controller Layer

Handles:

* Socket communication
* Business logic
* UI events

## Core Layer

Handles:

* Low-level socket operations
* Sending/receiving data
* Connection management

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd project-name
```

## Install Dependencies

```bash
py -3.11 -m venv venv 
venv\Scripts\activate
pip install -r requirements.txt 
```

---

# Running the Application

## Start Server

```bash
python -m server.main
```

## Start Client

```bash
python -m client.main
```

---

# Screenshots

## Main Window

Add screenshot here:

```bash
README_assets/main_window.png
```

## Process Management

Add screenshot here:

```bash
README_assets/process_window.png
```

## Screenshot Feature

Add screenshot here:

```bash
README_assets/screenshot_window.png
```

---

# Learning Outcomes

Through this project, I learned:

* Socket programming in Python
* Multi-window desktop applications using Tkinter
* Client-server communication
* Remote system management
* Lightweight MVC architecture
* Refactoring legacy code
* Threading for background tasks
* GUI event handling

---

# Future Improvements

* Authentication system
* Encrypted communication
* Multi-client support
* Better UI design
* Async socket communication
* Logging system
* Cross-platform support

---

# Disclaimer

This project was created for educational and research purposes only.
It should only be used in authorized environments and local networks.

---

# Author

Van Vinh Thai
