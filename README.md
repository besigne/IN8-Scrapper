# IN8-Scrapper
Challenge

## Requirements

- Python 3.9
- requirements.txt

## How to install

Download the IN8-Scrapper and navigate through terminal until inside IN8-Scrapper file,
then run the following commands:

```angular2html
python3.9 -m venv venv
```
```angular2html
 source venv/bin/activate
```
```angular2html
pip install -r requirements.txt
```
```angular2html
export FLASK_APP=manage
```
```angular2html
export FLASK_ENV=development
```
After all this you can run the `flask run` and access this [Page](http://localhost:5000)
and see the json created by the scrapper, the json should content:
- Model
- Price
- Screen Size
- Processor
- RAM
- Storage
- OS
***************

 Matheus Boesing da Silva