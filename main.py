#Following tutori
from flask import Flask, render_template
import random, string

#Flask Object - Flask(process_name, temp_folder, static_folder)
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

#sets all letters and digits equal to string
ok_chars = string.ascii_letters + string.digits
#ok_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


#.route('/(page-path)')
#On the next line, a function that doesnt take any arguments.
@app.route('/')  # '/' for the default page
def base_page():
    random_num = random.randint(1, 100000)  # Sets the random number
    #For render_template(template, context) 
    #Template file path, starting from the templates folder.
    # Sets the variable random_number in the template
    return render_template('base.html', random_number=random_num)


# def home():
# 	return "Wow this is a basic output!"


@app.route('/2')
def page_2():
    rand_ammnt = random.randint(10, 100)
    random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
    return render_template('site_2.html', random_str=random_str)


# Makes sure this is the main process
if __name__ == "__main__":
    # app.run(host, port)
    app.run(  # Starts the site
        # EStablishes the host, required for repl to detect the site
        host='0.0.0.0',
        # Randomly select the port the machine hosts on.
        port=random.randint(2000, 9000))

#------------------------------------
#new code fromat:	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))

