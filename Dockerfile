FROM python:3.8-slim-buster

# Install the security updates.
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install git libgl1-mesa-glx libglib2.0-0

# Remove all cached file. Get a smaller image.
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8501

# Copy the application.
COPY . /opt/app
WORKDIR /opt/app

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml

# Install the app librairies.
RUN pip install -r requirements.txt

# Start the app.
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "main.py" ]