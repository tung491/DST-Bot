from getlink import (tinhte, fml, genk, kenh14, xkcd, PE,
                     pornhub, vnexpress, viettlot, openweathermap)
import bot_time_table

from threading import Thread
from fbchat import log, Client
from fbchat.models import ThreadType

import time
import schedule
import os
import json


class Main_Bot(Client):
    def onMessage(self, author_id, thread_id,
                  thread_type, message, **kwargs):
        report = '''
                 {}
                 Message from {} in {} ({}): {}
                 '''.format(time.strftime("%a, %d %b %Y %H:%M:%S"),
                            author_id, thread_id, thread_type.name, message)

        log.info(report)

    def chemistry(self):
        thread_id = '1966276660049452'
        thread_type = ThreadType.GROUP
        with open('msg_chemistry.json') as f:
            data = json.load(f)

        self.sendMessage(data['msg'],
                         thread_id=thread_id,
                         thread_type=thread_type)

        self.sendRemoteImage(data['img_scr'], thread_id=thread_id, thread_type=thread_type)


class Clone_Bot(Client):
    def onMessage(self, author_id, message,
                  thread_id, thread_type, **kwargs):
        report = '''
                 {}
                 Message from {} in {} ({}): {}
                 '''.format(time.strftime("%a, %d %b %Y %H:%M:%S"),
                            author_id, thread_id, thread_type.name, message)
        log.info(report)

        if author_id != self.uid:
            message = message.lower()

            if message == 'tinhte':
                title_n_link, url_src = tinhte()
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

            if message == 'pornhub':
                title_n_link, url_src = pornhub()
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

            if message == 'pe':
                num_n_content = PE()

                self.sendMessage('Problem ' + str(num_n_content[0]),
                                 thread_id=thread_id,
                                 thread_type=thread_type)

                self.sendMessage(num_n_content[1],
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'fml':
                title_n_link = fml()
                msg_rep = str(title_n_link[0]) + '\n' + str(title_n_link[1])

                self.sendMessage('Bài mới nhất trên FAMILUG',
                                 thread_id=thread_id,
                                 thread_type=thread_type)
                self.sendMessage(msg_rep,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'kenh14':
                title_n_link, url_src = kenh14()

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

            if message == 'genk':
                title_n_link, url_src = genk()

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

            if message == 'xkcd':
                data = xkcd()

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

            if 'tkb' in message or 'Thời khóa biểu' in message:
                rep_message_ = bot_time_table.rep_msg(message)

                self.sendMessage(rep_message_,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'viettlot':
                data = viettlot()
                rep_message_ = '''
                               {}.
                               Số trúng Jackpot là {}.
                               Giá trị Jackpot là {}
                               '''.format(data[0], data[1], data[2])

                self.sendMessage(rep_message_,
                                 thread_id=thread_id,
                                 thread_type=thread_type)

            if message == 'vnex':
                title_n_link, url_src = vnexpress()

                self.sendMessage('5 bài viết nổi bật trên Vnexpress',
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

            if message == 'weather':
                data = openweathermap()

                description = data['description']
                humidity = data['humidity']
                pressure = data['pressure']
                temp = data['temp']
                temp_max = data['temp_max']
                temp_min = data['temp_min']
                wind_speed = data['wind_speed']
                wind_deg = data['wind_deg']

                msg_rep = '''
                          Trạng thái: {}
                          Độ ẩm: {} %
                          Áp suất: {} hPa
                          Nhiệt độ: {} °C
                          Nhiệt độ cao nhất: {} °C
                          Nhiệt độ thấp nhất: {} °C
                          Vận tốc gió: {} m/s
                          Hưóng gió: {}°
                          '''

                msg_rep = msg_rep.format(description, humidity, pressure,
                                         temp, temp_max, temp_min, wind_speed,
                                         wind_deg)

                self.sendMessage('Thời tiết hiện tại ở Hà Nội',
                                 thread_id=thread_id,
                                 thread_type=thread_id)
                self.sendMessage(msg_rep,
                                 thread_id=thread_id,
                                 thread_type=thread_id)


def run_main_bot():
    main_username = os.getenv('MAIN_USERNAME', '')
    main_password = os.getenv('MAIN_PASSWORD', '')

    main_client = Main_Bot(main_username, main_password)
    main_client.listen()


def run_clone_bot():
    clone_username = os.getenv('CLONE_USERNAME', '')
    clone_password = os.getenv('CLONE_PASSWORD', '')

    clone_client = Clone_Bot(clone_username, clone_password)
    clone_client.listen()


if __name__ == '__main__':
    Thread(target=run_main_bot).start()
    Thread(target=run_clone_bot).start()

    schedule.every().day.at("2:34").do(Main_Bot.chemistry)

    while True:
        schedule.run_pending()
        time.sleep(1)
