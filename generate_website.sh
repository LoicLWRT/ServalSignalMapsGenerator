#!/bin/bash  

echo Generating the base html using .trace files
python generator.py
echo Copying the html
cp *.html jekyll/

echo Using jekyll to generate the full website
cd jekyll/
jekyll
cd ../

echo Moving the website into local website directory
mv jekyll/_site/* website/

echo Cleaning up files
rm *.html
rm jekyll/*.html
