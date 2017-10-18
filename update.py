import facebook
from time import strftime
import login_main_acc


def get_content_update(msg):
    content = ''

    lines = msg.splitlines()
    for line in lines[1:]:
        content += line

    return content


def post_update_status(msg):
    TOKEN = login_main_acc.token
    LINK_FB = 'https: // www.facebook.com /' + login_main_acc.id_
    LINK_GIT_HUB = 'https://github.com/dosontung007/DST-Bot'

    graph = facebook.GraphAPI(access_token=TOKEN, version="2.7")

    content = get_content_update(msg)
    attachment = {'name': 'Link name',
                  'link': LINK_FB,
                  'caption': 'Check out this example',
                  'description': 'no descri',
                  }

    message = '''
              {}
              {}
              {}
              '''.format(strftime("%a, %d %b %Y %H:%M:%S"),
                         content,
                         LINK_GIT_HUB)

    graph.put_wall_post(message=message,
                        attachment=attachment,
                        profile_id='me')
