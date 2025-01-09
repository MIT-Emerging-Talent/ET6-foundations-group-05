# **Solutions**

This folder contains solutions to various coding challenges completed as part
of the **Practice Code Review** for the **MIT Emerging Talent Program**.

Each solution includes:  

- A **Python implementation** of the challenge.  
- **Documentation** within the docstring to explain the function’s behavior,
input/output, constraints, raised exceptions, and doctests.  
- Corresponding **unit tests** in the `/tests` folder to verify correctness
and handle a variety of cases.

The goal of this repository is to **practice problem-solving skills**,
**enhance code review abilities**, **collaborate effectively in a team**,
and develop strong **asynchronous development workflows**.

You can learn more about the **learning goals** for this project by checking
out **[`learning_goals.md`](collaboration/learning_goals.md)**.

## **Folder Structure**

The repository is structured to keep the solutions and tests organized,
making it easier to maintain and review the code.

```text
solutions/
│
├── [solution files]        # Python functions solving coding challenges
├── README.md               # Project documentation
└── tests/
    └── [test files]        # Unit tests for corresponding solutions
```

- The **`solutions/`** folder contains the implementations of the
coding challenges.
- The **`tests/`** folder contains the corresponding unit tests for each
solution to ensure correctness and handle standard, edge, and defensive cases.

The folder structure supports a **test-driven development (TDD) approach**,
ensuring that every solution is tested and verified for various scenarios
before being finalized.

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
