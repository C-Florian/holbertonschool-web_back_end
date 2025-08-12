# Pagination

## Resources
**Read or watch**:

- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

---

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

---

## Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the **pycodestyle** style (version 2.5.*)
- The length of your files will be tested using `wc`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- Documentation is not just a word; it should be a full sentence explaining the purpose of the module, class, or method
- All functions and coroutines must be type-annotated
- Dataset file: `Popular_Baby_Names.csv`

---

## Dataset
You must use this data file for your project: **[Popular_Baby_Names.csv](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv)**

Download it and place it at the root of your project folder:
```bash
curl -L "https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv" -o Popular_Baby_Names.csv
