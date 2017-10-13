import bot_rep
import getlink
import wish_choose
import wish_id_user
import time
import bot_time_table

from fbchat import log, Client

import login
import login_acc_clone


class Bot(Client):
    def log(self, author_id, thread_id, thread_type, message, **kwargs):
        report = '''{}
                Message from {} in {} ({}): {}
                '''.format(time.strftime("%a, %d %b %Y %H:%M:%S"),
                           author_id, thread_id, thread_type.name, message)
        log.info(report)

    def reply(self, author_id, thread_id, thread_type, message, **kwargs):
        if author_id != self.uid:
            msg_rep = bot_rep.rep_msg(message.lower())

            if type(msg_rep) is str:
                self.sendMessage(msg_rep,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                log.info('Declined invitation from {}'.format(author_id))

    def good_night(self):
        t0 = time.time()

        for id in wish_id_user.friend_list:
            Wish = wish_choose.choose_wish(id)

            log.info('Send message to {}'.format(id))

            self.sendMessage(Wish,
                             thread_id=id,
                             thread_type=ThreadType.USER)

            self.sendMessage('Được gửi từ Good Night-Bot with <3',
                             thread_id=id,
                             thread_type=ThreadType.USER)
        t1 = time.time()

        log.info('Message delivered to {} people in {}s'.format(
            len(wish_id_user.friend_list), t1 - t0))

        print('I\'m done my job. Good night my boss')

        log.info('All wish are delivered in {}s'.format(t1 - t0))


class Bot_Clone(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        if author_id != self.uid:
            if message.lower() == 'tinhte':
                title_n_link, url_src = getlink.tinhte()
                self.sendMessage('5 bài nổi bật trên Tinhte.vn',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)
                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
            
            if message.lower() == 'pornhub':
                title_n_link, url_src = getlink.pornhub()
                self.sendMessage('5 bộ phim nổi bật trên pornohub.su',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)

                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)

            if message.lower() == 'pe':
                num_n_content = getlink.PE(message.lower())
                self.sendMessage('Problem ' + str(num_n_content[0]),
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                
                self.sendMessage(num_n_content[1],
                                 thread_id=thread_id,
                                 thread_type=thread_type)
            
            if message.lower() == 'fml':
                title_n_link = getlink.fml()
                msg_rep = str(title_n_link[0]) + '\n' + str(title_n_link[1])
                
                self.sendMessage('Bài mới nhất trên FAMILUG',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendMessage(msg_rep,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message.lower() == 'kenh14':
                title_n_link, url_src = getlink.kenh14()
                self.sendMessage('5 bài viết nổi bật trên kênh14',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                    
                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)
                    
                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)        
            
            if message.lower() == 'genk':
                title_n_link, url_src = getlink.genk()
                self.sendMessage('5 bài viết nổi bật trên Genk.vn',                            
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                
                for i in range(5):
                    self.sendMessage(title_n_link[i][0],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                    
                    self.sendRemoteImage(url_src[i],
                                         thread_id=thread_id,
                                         thread_type=thread_type)
                    
                    self.sendMessage(title_n_link[i][1],
                                     thread_id=thread_id,
                                     thread_type=thread_type)
            
            if message.lower() == 'xkcd':
                data = getlink.xkcd()
                
                self.sendMessage('Bài viết mới nhất trên xkcd.com',                            
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendMessage(data[0],                            
                                 thread_id=thread_id,
                                 thread_type=thread_type)                
                self.sendRemoteImage(data[1],                            
                                     thread_id=thread_id,
                                     thread_type=thread_type)
                self.sendMessage(data[2],                            
                                 thread_id=thread_id,
                                 thread_type=thread_type)
            
            if message.lower() == 'good night':
                Bot.good_night()

            for key_word in ['tkb', 'thời khóa biểu']:
                if message.lower() == key_word:
                    if key_word in message.lower():
                        rep_message_ = bot_time_table.rep_message(message)

                        self.sendMessage(rep_message_,
                                         thread_id=thread_id,
                                         thread_type=thread_type)


clone_client = Bot_Clone(login_acc_clone.username, login_acc_clone.password)
clone_client.listen()
