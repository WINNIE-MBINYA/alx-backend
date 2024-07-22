
### Setup

All the files in this directory are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7. To set up the environment, ensure you have Python 3.7 installed.

### Requirements

- All Python files should end with a new line.
- The first line of all your Python files should be `#!/usr/bin/env python3`.
- A `README.md` file is mandatory at the root of the project folder.
- Your code should follow the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

### Tasks

#### Task 0: Simple Helper Function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`. The function should return a tuple containing the start index and end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

#### Task 1: Simple Pagination

Implement a `Server` class to paginate a database of popular baby names. The class should have a method named `get_page` that takes two integer arguments `page` and `page_size` with default values 1 and 10 respectively.

#### Task 2: Hypermedia Pagination

Implement a `get_hyper` method in the `Server` class. The method should return a dictionary containing pagination metadata such as `page_size`, `page`, `data`, `next_page`, `prev_page`, and `total_pages`.

#### Task 3: Deletion-Resilient Hypermedia Pagination

Implement a `get_hyper_index` method in the `Server` class. The method should return a dictionary with pagination metadata that is resilient to deletions in the dataset. It should handle cases where rows might be deleted between queries, ensuring the user does not miss items when paginating.

### Usage

To run the scripts, use the following commands:

```sh
# Make the script executable
chmod +x <script_name>.py

# Run the script
./<script_name>.py
