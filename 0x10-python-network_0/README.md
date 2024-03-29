# alx-higher_level_programming - 0x10-python-network_0

## Task 0: cURL body size

### Description
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

- The size must be displayed in bytes.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```

#### File
- [0-body_size.sh](./0x10-python-network_0/0-body_size.sh)

## Task 1: cURL to the end

### Description
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

- Display only the body of a 200 status code response.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```

#### File
- [1-body.sh](./0x10-python-network_0/1-body.sh)

## Task 2: cURL Method

### Description
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```

#### File
- [2-delete.sh](./0x10-python-network_0/2-delete.sh)

## Task 3: cURL only methods

### Description
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```

#### File
- [3-methods.sh](./0x10-python-network_0/3-methods.sh)

## Task 4: cURL headers

### Description
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.

- A header variable X-School-User-Id must be sent with the value 98.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
```

#### File
- [4-header.sh](./0x10-python-network_0/4-header.sh)

## Task 5: cURL POST parameters

### Description
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

- A variable email must be sent with the value test@gmail.com.
- A variable subject must be sent with the value I will always be here for PLD.
- You have to use curl.
- Please test your script in the sandbox provided, using the web server running on port 5000.

#### Example
```bash
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
```

#### File
- [5-post_params.sh](./0x10-python-network_0/5-post_params.sh)

## Task 6: Find a peak

### Description
Write a function that finds a peak in a list of unsorted integers.

- Prototype: `def find_peak(list_of_integers)`.
- You are not allowed to import any module.
- Your algorithm must have the lowest complexity.
- `6-peak.py` must contain the function.
- `6-peak.txt` must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2).
- Note: there may be more than one peak in the list.

#### Example
```python
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
```

```bash
guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```

#### Files
- [6-peak.py](./0x10-python-network_0/6-peak.py)
- [6-peak.txt](./0x10-python-network_0/6-peak.txt)
