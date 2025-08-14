# NoSQL - MongoDB with Python

## 📌 Description
This project introduces **NoSQL** databases and how to interact with them using **MongoDB** and **PyMongo** in Python.  
The goal is to understand the differences between relational (SQL) and non-relational (NoSQL) databases, learn core NoSQL concepts, and practice querying and manipulating data both from the Mongo shell and Python scripts.

## 🎯 Learning Objectives
By the end of this project, you should be able to:
- Explain what **NoSQL** means.
- Differentiate between **SQL** and **NoSQL**.
- Understand the **ACID** properties and how they differ from **BASE**.
- Explain what a **document store** is.
- Identify the **types** of NoSQL databases.
- List the **benefits** of NoSQL databases.
- **Query**, **insert**, **update**, and **delete** data from MongoDB.
- Use MongoDB with **PyMongo** in Python.

## 🗂 Project Structure
This project contains:
- **Mongo Shell scripts** (`.js`) to interact directly with MongoDB.
- **Python scripts** (`.py`) using **PyMongo**.

| File | Description |
|------|-------------|
| `0-list_databases` | Lists all databases |
| `1-use_or_create_database` | Uses or creates the `my_db` database |
| `2-insert` | Inserts a document into the `school` collection |
| `3-all` | Lists all documents in the `school` collection |
| `4-match` | Lists documents where `name="Holberton school"` |
| `5-count` | Displays the number of documents in `school` |
| `6-update` | Updates the `address` field for `Holberton school` |
| `7-delete` | Deletes documents with `name="Holberton school"` |
| `8-all.py` | Lists all documents in a collection |
| `9-insert_school.py` | Inserts a document into a collection |
| `10-update_topics.py` | Updates the topics of a school |
| `11-schools_by_topic.py` | Lists schools that match a specific topic |
| `12-log_stats.py` | Displays statistics from Nginx logs |

## 📦 Installation

### Requirements
- Ubuntu 20.04 LTS
- MongoDB 4.4
- Python 3.9
- PyMongo 4.8.0

### Install MongoDB
```bash
sudo apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org

