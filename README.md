## How to Start the Server

You can run the application using `uvicorn`, an ASGI server.

- uvicorn <filename>:app --reload
- uvicorn main:app 
-   **To run the server for production:**
    This command starts the server. Replace `main` with your Python file's name if it's different.
    ```bash
    uvicorn main:app
    ```

-
-   **To run the server for development:**
    The `--reload` flag enables auto-reloading, which automatically restarts the server whenever you change a file. This is very useful during development.
    ```bash
    uvicorn main:app --reload
    ```


### FastAPI Key Concepts
-   **Path Operation**: In FastAPI, what is commonly called a "route" or an "endpoint" in other frameworks is referred to as a *path operation*.
-   **Path Operation Function**: The function that handles the request for a specific path operation. This is similar to what might be called a "controller" or a "view function" in other frameworks.