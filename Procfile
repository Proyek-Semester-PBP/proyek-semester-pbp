release: sh -c 'python manage.py migrate && python manage.py loaddata initial_news_data.json && python manage.py loaddata initial_redeem_data.json && python manage.py loaddata initial_product_data.json && python manage.py loaddata initial_vendor_data.json'
web: gunicorn proyek_semester_pbp.wsgi --log-file -
