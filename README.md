Bank OCR Kata
================

This is repository with solution to http://codingdojo.org/kata/BankOCR/

### How to run ###
```
docker build . -t kata && docker run --rm -it kata python app/main.py
```

### How to test ###
```
docker build . -t kata && docker run --rm -it kata pytest tests/
```
