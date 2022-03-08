FROM python:3.9

WORKDIR /movie-recommender-backend
COPY ./requirements.txt /movie-recommender-backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /movie-recommender-backend/requirements.txt

COPY ./app /movie-recommender-backend/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
