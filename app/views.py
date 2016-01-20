from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/') 
@app.route('/index')
def index():
	user = {'name': 'siljeih'} #fake user
	reakler = [ # Fake reakler
	    {
		'name': 'roede',
		'antallTimer': 4
	    },
	    {
		'name': 'siljeih',
		'antallTimer': 4
	    },
	    {
		'name': 'hognely',
		'antallTimer': 6
	    },
	    {
		'name': 'frodesne',
		'antallTimer': 6
	    },
	    {
		'name': 'tormod',
		'antallTimer': 6
	    },
	    {
		'name': 'markus',
		'antallTimer': 6
	    }
	]
	
	return render_template('index.html',
				title='Uke 4',
				user=user,
				reakler=reakler)


@app.route('/login', methods=['GET', 'POST'])	# Accept borth GET and POST (without: only GET)
def login():
    form = LoginForm()
    if form.validate_on_submit():
	flash('Login requested for OpenID="%s", remember_me=%s' %
		(form.openid.data, str(form.remember_me.data)))
	return redirect('/index')
    return render_template('login.html',
				title='Logg inn',
				form=form,
				providers=app.config['OPENID_PROVIDERS'])	
