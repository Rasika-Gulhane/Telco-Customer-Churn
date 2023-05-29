FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install scikit-learn==1.0.2
EXPOSE 5000
CMD gunicorn --workers=4 --bind 0.0.0.0:5000 app:app