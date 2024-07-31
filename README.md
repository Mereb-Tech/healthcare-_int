# healthcare-_int
###Assumptions:

- The Docker registry requires credentials for access.
- The repository URL and branch are accessible and correctly specified.
- Jenkins credentials (github-credentials-id and docker-registry-credentials) are set up properly.
- Python script is designed to handle input from the command line.
## Explanations for Choices:

Windows Server Core: Chosen due to user constraints and compatibility with the existing environment.
- Chocolatey for Python Installation: Simplifies the installation of Python on Windows.
Pipeline Stages:
- Checkout: Retrieves the source code from GitHub.
- Build: Builds the Docker image with the application.
- Test: Runs unit tests to ensure the application works correctly.
- Deploy: Pushes the Docker image to the registry and optionally deploys it.
- Cleanup: Removes unused Docker images to save space.

##  Notes
Credentials Management: Ensure that sensitive information like Docker registry credentials and GitHub tokens are managed securely within Jenkins.
