# LLM Youtube Videos Notes

## AT&T Text to SQL 

a. Data Curation
    1. Ambiguous or Abbreviated Names
        a. like aloc , aia
    2. Consistency in data

b. Data Profiling

c. Synthetic Data Generation

d. Hyperparameter Tuning
    1. Learning Rate
        1. kept very small learning rate 
    2. No. of epochs
        1. 1 or 2 epochs work fine they used 4

e. Track the training loss to converge (it shouldnt fluctuate)


## Why LLM Data Processing Pipelines Fail

- Prompt Iteration Process
  - Suffers because there gap in understanding data and intent gap
  - Remove as much as ambiguity in the prompt as possible


# Pointers
    - Create a database.py
      - creates a database
      - creates an engine to manage connections with the database
      - Creates a session factory
        - used for creating new sessions to conversate with the db
      - create a base class\
        - is the base class for all ORM models (database tables)
        - when we define a model it inherits base class
        - tells sqlalchemy how to map python classes to db tables
    - use model
      - define everything related to the table columns
    - To add data in database
      - create a get_db function
      - create a db_dependecy
        - combines sqlalchemy's Session with fastapi dependence injection
      - each api request get its own db session and is closed when request is finished