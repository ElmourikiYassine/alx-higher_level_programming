# README.md

## Python Network Tasks

This repository contains Python scripts for various network-related tasks using packages like `urllib` and `requests`. Below is a brief overview of each task along with usage examples.

### Task 0: What's my status? #0
**Objective:** Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib` and displays information about the response.

**Usage:**
```bash
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

**File:** [0-hbtn_status.py](0x11-python-network_1/0-hbtn_status.py)

---

### Task 1: Response header value #0
**Objective:** Write a Python script that takes in a URL, sends a request, and displays the value of the `X-Request-Id` variable found in the header of the response using `urllib`.

**Usage:**
```bash
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
```

**File:** [1-hbtn_header.py](0x11-python-network_1/1-hbtn_header.py)

---

### Task 2: POST an email #0
**Objective:** Write a Python script that takes in a URL and an email, sends a POST request with the email as a parameter, and displays the body of the response (decoded in utf-8) using `urllib`.

**Usage:**
```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

**File:** [2-post_email.py](0x11-python-network_1/2-post_email.py)

---

### Task 3: Error code #0
**Objective:** Write a Python script that takes in a URL, sends a request, and displays the body of the response. Manage `urllib.error.HTTPError` exceptions and print the error code if an error occurs.

**Usage:**
```bash
$ ./3-error_code.py http://0.0.0.0:5000
Index
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

**File:** [3-error_code.py](0x11-python-network_1/3-error_code.py)

---

### Task 4: What's my status? #1
**Objective:** Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `requests` and displays information about the response.

**Usage:**
```bash
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```

**File:** [4-hbtn_status.py](0x11-python-network_1/4-hbtn_status.py)

---

### Task 5: Response header value #1
**Objective:** Write a Python script that takes in a URL, sends a request, and displays the value of the variable `X-Request-Id` in the response header using `requests`.

**Usage:**
```bash
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
```

**File:** [5-hbtn_header.py](0x11-python-network_1/5-hbtn_header.py)

---

### Task 6: POST an email #1
**Objective:** Write a Python script that takes in a URL and an email address, sends a POST request with the email as a parameter, and displays the body of the response using `requests`.

**Usage:**
```bash
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

**File:** [6-post_email.py](0x11-python-network_1/6-post_email.py)

---

### Task 7: Error code #1
**Objective:** Write a Python script that takes in a URL, sends a request, and displays the body of the response. If the HTTP status code is greater than or equal to 400, print the error code.

**Usage:**
```bash
$ ./7-error_code.py http://0.0.0.0:5000
Index
$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

**File:** [7-error_code.py](0x11-python-network_1/7-error_code.py)

---

### Task 8: Search API
**Objective:** Write a Python script that takes a letter, sends a POST request

 to `http://0.0.0.0:5000/search_user` with the letter as a parameter, and displays the response.

**Usage:**
```bash
$ ./8-json_api.py
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
```

**File:** [8-json_api.py](0x11-python-network_1/8-json_api.py)

---

### Task 9: My GitHub!
**Objective:** Write a Python script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user id.

**Usage:**
```bash
$ ./10-my_github.py papamuziko cisfun
2531536
$ ./10-my_github.py papamuziko wrong_pwd
None
```

**File:** [10-my_github.py](0x11-python-network_1/10-my_github.py)
