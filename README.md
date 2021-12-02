# CarPlates

    Application made in React.js and FASTAPI to search for a car model from a license plate using a serverless lamda function that communicates with a database in MySQL and a Redis cache.

## Requirements

1. docker
2. docker-compose
3. python (optional)

# How to run

1. Open a terminal and go to the CarPlates Directory
2. Run `make build` to build docker for the first time
3. Once the build finishes (it may take some time) go to http://localhost:4000/

# Plates format and generation

Plates are in the format `XXX yyy` where X is a leter `A-Z` and y is a number between `0-9`. For example 'XTS 538' is a valid plate to search for.
The proyect comes with a pre-generated 10000 entries functions/script/example.json file to be inserted into the database.
Its possible to generate a new one with more or less entries. Simply delete that file and:

1. Run `python3 functions/script/json_generator.py "NEWFILENAME.json" NRO_ENTRIES`
For example: `python3 functions/script/json_generator.py "new_entries.json" 100000`
2. Edit docker-compose.yml to indicate the new file to load:
line 49 command: python3 db_script.py example.json -> command: python3 db_script.py NEWFILENAME.json

Its also possible to just make one manually remembering that plates are alfanumeric with max 9 characters and models are alfanumeric with max 255 characters
