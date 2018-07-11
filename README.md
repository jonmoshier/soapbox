# soapbox
Large scale landing page generator


## install

You'll need virtualenv for the install process.

```
$ git clone https://github.com/jonmoshier/soapbox.git

$ cd soapbox

soapbox$ virtualenv -p python3 virt
> ...
> New python executable in soapbox/virt/bin/python3
> Also creating executable in soapbox/virt/bin/python
> Installing setuptools, pip, wheel...done.

soapbox$ source virt/bin/activate

(virt) soapbox$ pip install -r requirements.txt
> Collecting Django
> .... etc, etc ...
> Successfully installed Django
> .... etc, etc ...
```

At this point rename soapbox/soapbox/soapbox/secrets.py.template to be soapbox/soapbox/soapbox/secrets.py and grab a secret key from https://www.miniwebtool.com/django-secret-key-generator/

Edit secrets.py 

```
# secrets.py
SECRET_KEY = 'insert-your-secret-key'
```

to have a proper secret key.

```
(virt) soapbox$ cd soapbox
 
(virt) soapbox/soapbox$ ./manage.py makemigrations

(virt) soapbox/soapbox$ ./manage.py migrate
 
(virt) soapbox/soapbox$ ./manage.py createsuperuser

>> follow prompts

(virt) soapbox/soapbox$ ./manage.py runserver
```

and navigate your browser to localhost:8000

