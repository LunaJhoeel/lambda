FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY src/ src/

CMD ["main.lambda_handler"]

