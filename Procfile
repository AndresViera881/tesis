web: gunicorn app:app --log-file - --log-level debug
python app.py collectstatic --noinput
app.py migrate