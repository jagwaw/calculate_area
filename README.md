# README #

This repo is for the calculation of area.

The static folder contains the static files (html,css,javascript)
The falcon folder contains the python files.

How to access the front-end in the browser:
-http://localhost/calculate_area/static/#!/

How to set-up the front-end:
- run npm install . 

How to set-up the back-end
-install the ff:
	-falcon
	-gunicorn
	-waitress
	-os
	-json

How to run the python file:
- install the requirements first
- run waitress-serve --port=8000 area:app in the falcon directory

How to run the unit test:
- run python -m unittest test_area.py in the falcon directory


Steps in calculation of area:
1. Select the shape
2. Select the output measurement
3. Select the corresponding value for each object and it's measurement.
4. You can select different measurement for each side,length,width,base,height,radius and it's output 
5. Click the compute button to get the area of the selected shape.