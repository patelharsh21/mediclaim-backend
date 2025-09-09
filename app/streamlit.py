import subprocess
import sys
import os
import time

def main():
    """
    This script starts both the FastAPI backend and the Streamlit frontend.
    """
    # Command to start the FastAPI backend server
    backend_command = [
        "uvicorn",
        "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ]

    # Command to start the Streamlit frontend
    frontend_command = [
        "streamlit",
        "run",
        "app/POC_frontend.py",
        "--server.port", "8501",
        "--server.address", "0.0.0.0"
    ]

    print("--- Starting FastAPI Backend Server ---")
    # Start the backend as a background process
    backend_process = subprocess.Popen(backend_command)
    
    # Give the backend a moment to start up before launching the frontend
    time.sleep(5) 

    print("\n--- Starting Streamlit Frontend Server ---")
    # Start the frontend. This will run in the foreground.
    frontend_process = subprocess.Popen(frontend_command)

    try:
        # Wait for the user to stop the script (e.g., with CTRL+C)
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n--- Shutting down servers... ---")
    finally:
        # When the script is stopped, terminate both processes
        backend_process.terminate()
        frontend_process.terminate()
        backend_process.wait()
        frontend_process.wait()
        print("--- Servers shut down successfully. ---")

if __name__ == "__main__":
    main()
