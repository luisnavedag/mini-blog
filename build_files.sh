echo "Build Start"
python3.10.7 -m pip install -r requirements.txt
python3.10.7 manage.py collectstatic --noinput --clear
echo "Build End"