# Use Windows Server Core as the base image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Install Chocolatey
RUN powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; \
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"

# Install Python using Chocolatey
RUN powershell -Command "choco install python --version=3.9.7 -y"

# Verify Python installation
RUN powershell -Command "python --version"

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY calc.py /app/
COPY test.py /app/
# Run dir to list files
RUN powershell -Command "dir"

# Set the entry point to run the Python script
ENTRYPOINT ["cmd"]


# No ports need to be exposed as this is a CLI application
