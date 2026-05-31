# NetAdmin Tool

A Python-based remote administration tool that allows monitoring and managing Windows computers over a Local Area Network (LAN).

## Features

### Process Management

* View running processes on remote machine
* Start new processes remotely
* Terminate selected processes
* Refresh process list

### Application Management

* View running desktop applications
* Launch applications remotely
* Close selected applications

### Screenshot Capture

* Capture remote desktop screenshots
* Display screenshots in real time
* Save screenshots locally

### Keyboard Monitoring

* Start keyboard monitoring
* Stop keyboard monitoring
* View recorded keystrokes
* Clear log history

### Remote Shutdown

* Shutdown remote computer through LAN

---

## Technologies Used

### Backend

* Python 3.x
* Socket Programming (TCP)
* psutil
* winreg
* mss
* threading

### GUI

* Tkinter
* ttk widgets
* Pillow

### Architecture

The project is currently being refactored following the MVC (Model – View – Controller) architecture.

```
Client
│
├── controllers
├── services
├── models
├── views
├── network
└── main.py

Server
│
├── controllers
├── handlers
├── services
├── models
├── network
└── main.py
```

---

## System Architecture

```
+----------------+
| Client (GUI)   |
+----------------+
         |
         | TCP Socket
         |
+----------------+
| Server         |
+----------------+
         |
         +--> Process Service
         +--> Application Service
         +--> Screenshot Service
         +--> Keylogger Service
         +--> Registry Service
```

---

## Communication Protocol

### Process Management

Client:

```
PROCESS
VIEW
```

Server Response:

```
[4 bytes] Number of processes

For each process:
    [4 bytes] Data length
    [N bytes] Process information
```

### Kill Process

Client:

```
PROCESS
KILL
KILLID
1234
```

### Start Process

Client:

```
PROCESS
START
STARTID
notepad.exe
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/yourusername/NetAdmin-Tool.git
cd NetAdmin-Tool
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start Server

```bash
python server/main.py
```

Expected output:

```text
Server running on 0.0.0.0:5656
Waiting for clients...
```

### Start Client

```bash
python client/main.py
```

Enter the server IP address and click **Connect**.

---

## Screenshots

### Main Window

Add screenshot here:

```
docs/images/main-window.png
```

### Process Management

Add screenshot here:

```
docs/images/process-running.png
```

### Screenshot Capture

Add screenshot here:

```
docs/images/screenshot-feature.png
```

## Future Improvements

* Authentication system
* Encrypted communication
* Multi-client support
* File transfer
* Remote command execution
* Logging and auditing
* Cross-platform support

---

## Educational Purpose

This project was developed for learning purposes to practice:

* Socket Programming
* Multithreading
* Operating System Management
* Client-Server Architecture
* MVC Design Pattern
* Python GUI Development

---

## Author

Van Vinh Thai

GitHub: https://github.com/ThVVinh/NetAdmin-Tool
