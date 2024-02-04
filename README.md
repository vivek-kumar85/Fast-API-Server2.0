# FastAPI Server
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

A FastAPI server for handling CSV uploads and logging operations.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [HTML Interface](#html-interface)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload CSV files and save them with a timestamp.
- Receive log files and save them with a timestamp.
- HTML interface for a welcoming page.

## Project Structure
```
Your_Project_Dir/
├── app/
│ ├── init.py
│ ├── routers/
│ │ ├── init.py
│ │ ├── csv_handler.py
│ │ └── logging_handler.py
├── static/
│ └── index.html
├── main.py
├── requirements.txt
├── .gitignore
```


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vivek-kumar85/Fast-API-Server2.0.git
    ```

2. Change to the project directory:

    ```bash
    cd Fast-API-Server2.0
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the FastAPI server with the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 2121 --reload 

```

## Endpoints
``` Upload CSV: POST /csv/upload-csv ``` 

``` Receive Logfile: POST /logging/receive-logfile ```

## HTML Interface
The server provides a welcoming page at http://localhost:2121 displaying "Welcome to Server !!".

## Logging
Logs are saved in the server_logs.log file.

## Contributing
Feel free to contribute by opening issues or creating pull requests.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
