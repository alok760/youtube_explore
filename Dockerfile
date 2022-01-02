# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN python -m pip install pipenv
RUN apt-get update && apt-get -y install cron
RUN apt install -y git

WORKDIR /app
COPY . /app
RUN pipenv install --system --deploy --ignore-pipfile

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN chmod 755 ./entrypoint.sh
RUN chmod 755 ./entrypoint_compose.sh
RUN chmod 755 ./wait-for-it.sh

ENTRYPOINT ["./entrypoint.sh"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'youtube_explore'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi"]
