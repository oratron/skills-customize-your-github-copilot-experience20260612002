---
title: "Building REST APIs with FastAPI"
difficulty: "Intermediate"
estimated_time: "60-90 minutes"
---

# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI, define request and response models, validate input data, and handle common HTTP status codes.

## 📝 Tasks

### 🛠️ Define the API and data models

#### Description
Create a FastAPI app with a data model for items and define endpoints for listing and retrieving items.

#### Requirements
Completed assignment should:

- Create a FastAPI app instance in `starter-code.py`.
- Define a Pydantic model for the API resource.
- Implement a GET endpoint to return all items.
- Implement a GET endpoint to return a single item by ID.

### 🛠️ Add create and update behavior

#### Description
Add endpoints to create new items and update existing items using request validation.

#### Requirements
Completed assignment should:

- Implement a POST endpoint to add new items.
- Validate request payloads using Pydantic models.
- Implement a PUT endpoint to update an existing item by ID.
- Return appropriate response status codes for success and validation errors.

### 🛠️ Handle errors and missing resources

#### Description
Implement error handling for invalid requests and resources that do not exist.

#### Requirements
Completed assignment should:

- Return a `404` error when an item is not found.
- Return a `400` error for invalid input data.
- Provide clear error messages in JSON responses.

### 🛠️ Run and test the API

#### Description
Run the FastAPI application with Uvicorn and verify the endpoints work using the automatic API docs or a REST client.

#### Requirements
Completed assignment should:

- Use `uvicorn` to run the FastAPI app.
- Access the interactive docs at `/docs` or `/redoc`.
- Confirm that requests to each endpoint return the expected response.
