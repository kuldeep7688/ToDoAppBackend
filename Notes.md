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

# Production Databases

## Why not SQLite for production

  - Sqlite3 provides local data storage for individual apps
  - it emphasizes economy, effeciency and simplicity
  - For most small/medium apps
  - focusses on different concepts
  - Production DBMS focus on stability , concurrency and control
  - if 10s of thousands of users
  - Run on a separate port and server

## POSTGRESQL

  - production ready
  - Open source relational database management system
  - Secure
  - Requires a server
  - Scalable


## MySQl
  - production ready
  - open source
  - requires server
  - secure
  - Scalable

## Alembic
- lightweight database migration tool when using SQLAlchemy
- Migration tools allow us to plan, transfer and upgrade resources withing database
- It allows us to change database table after it has been created
- SqlAlchemy just allows us to create a table but not update or change it. Alembic allows us to do that.

## Testing

### Unit Testing

- Validates that each unit of the software performs as designed
- Unit - Testable part of the application
- Tests are written during development
- Executed automatically using a framework like Pytest
- Identify bugs early in development.

### Integration Testing

- testing the interactions between different units or components
- testing multiple units together
- identifies problem in the entire solution
- Ex : call an api endpoint and make sure the correct solution is returned
- 