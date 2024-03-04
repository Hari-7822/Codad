# build_files.sh
pip install -r requirements.txt
rm -rf staticfiles
python3.9 manage.py collectstatic
