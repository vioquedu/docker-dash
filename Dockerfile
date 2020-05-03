FROM python:3.6

# Create a directory where the code is to be hosted
RUN mkdir /app
# Define the working directory in the container
WORKDIR /app 
# Copy and install the requirements.
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Define environment variables
ENV dash_port=8050
ENV dash_debug="True"

CMD ["python", "dash_app.py"]
