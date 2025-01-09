# **Tests**

This folder contains unit tests for verifying the correctness of the solutions
provided in the `solutions/` folder.  
The tests are written using the **unittest** framework to cover a variety
of cases, including:

- ✅ Standard cases  
- ✅ Edge cases  
- ✅ Defensive cases  

## **Folder Structure**

The `tests/` folder mirrors the structure of the `solutions/` folder, with each
test file named to correspond with the solution it verifies. For example:

## **How to Run Tests**

To run all unit tests, navigate to the root directory of the repository and use
the following command:

```bash
python3 -m unittest -v
```

The `-v` flag stands for **verbose mode**, which provides detailed information
about each test case. It will display the **name of each test**, along with its
**status** (pass/fail), and any **error messages** if a test fails.
Using verbose   mode makes it easier to **debug and understand test results**.
