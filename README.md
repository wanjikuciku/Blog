# ReadPress
This is a website that allows users to post blogs and comment on them 19th february 2019
### By Lorna wanjiku

## Description
This is a website that allows app's users to post blogs and view blogs.

## Specifications
Users can view most recent blog posts
Users can comment on blog posts
Users can register and login to become writers
Writers can create new blog posts

## Setup/Installation Requirements
To start using this project use the following commands:

* git clone https://github.com/wanjikuciku/blog.git
* cd Blog
* atom .
* code . (this is if Visual Studio Code is your preferred text editor)

 To run this program
* Create a virtual environment by python3.6 -m venv --without-pip virtual then activate the virtual environment
* Read the specs and requirements files and install all requirements by pip install -r requirements.txt
* create a start.sh file and hide it in gitignore
* Edit the start.sh file with your email account and password and add python3.6 manage.py server so as to serve
* enter the code chmod a+x start.sh then ./start.sh to serve

* access the application on this localhost address http://127.0.0.1:5000

## Behaviour Driven Development
|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| Home | - | - |
|Click on login button | fill credentials | blogs |
|view blogs | click on view | All posts are displayed starting with the most recent|
|Delete Blog| Click on Delete | Post is deleted|
|Write Blogs | Click on New Blog |	A form for a new blog is displayed|

## Prerequisites
You need the following to work on the project: -Python version 3.6 -Flask -Pip -virtualenv -A text Editor

## Link to Live Website https://git.heroku.com/lony-blog.git

## Known Bugs
None known at the moment.

## Technologies Used
* Python
* HTML
* Flask micro-framework
* Bootstrap(used for styling)

## License
MIT License

Copyright (c) 2019 LORNA WANJIKU

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
