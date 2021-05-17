## ToRead
A python cli to track your read, reading and completed reading books.

## Depends
1. Typer - CLI
2. Mongodb - Database
3. Pymongo - Mongodb driver 
   
## Install
```
pip install -r requirements.txt
or
poetry install
```

## Setup
**Mongodb**
   1. You need a mongod client
   2. Start your mongod client
       - Linux:
           ```
           systemctl start mongodb.service
           ```
**settings.json**
1. Create a file named settings.json 
```json
{
    "db_name": "db name here",
    "collection_name": "collection name here"
}
```

## Run
1. Retrieve:
   1. all books: ```python main.py get```
   2. book with passed in title: ```python main.py get "title"```

2. Create: 
   ```python main.py create```

3. Update:
   ```python main.py update "title" ```

4. Completed:
   ```python main.py completed "title"```

5. Delete:
   ```python main.py delete "title"```

