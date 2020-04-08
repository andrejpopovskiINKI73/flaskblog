import os
import secrets

from PIL import Image
from flask_mail import Message
from flask import url_for, current_app
from flaskblog import mail


# function for Account picture, we resize it to save space in out filesystem
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)  # if we have an unused variable, python programmers
    # use _ (underscore) to mark that variable
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)  # full path all the way to
    # package dir + static folder + pic folder + the filename of the pic
    output_size = (125, 125)  # size of compressed picture
    i = Image.open(form_picture)  # image we pass in the function
    i.thumbnail(output_size)  # we resize it
    i.save(picture_path)  # we save it resized

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request',
                  sender='andrej.popovskiot@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, then simply ignore this email and no changes will be made!
'''
    mail.send(msg)

