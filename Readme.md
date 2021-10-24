Start the app:
    - Create python 3 virtual env, and activate it
    - pip install -r requirements.txt
    - export FLASK_APP = app
    - flask run

Run the tests:
    - pytest

Hi There!

Thank you for taking the time to read and assess my work. Just a quick headsup and my work.
You may notice certain patterns being utilized but lack the idea of abstraction. The reason for
this is because I am simply just exhausted and making an abstract strategy imlementation after 
work hours on when I know it will only be used once was kind of redundant to me. However, I would 
totally do that if this was production code. 

I had a good time and just for gags implemented an in memory cache with a doubly linked list and 
hash map. I try to keep my flask views fairly clean and only have parameter validation, everything else is dealt with via it's own service. I test my services, and Api end points separately and they can be found in my src.tests directory


