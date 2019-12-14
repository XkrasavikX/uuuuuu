#! /usr/bin/env python
# -*- coding: utf-8 -*-
# made by Krasav4ik VK @bess_arya
import logging
from func import *

with open("configs/token.json", "r") as read_file:
    configs = json.load(read_file)

token, group_id = configs["token"], configs["group_id"]
vk_session, session_api, longpoll = vk_api.VkApi(token=token), vk_session.get_api(), VkBotLongPoll(vk_session, group_id)
followers = session_api.messages.getConversations()

time = lambda: datetime.datetime.today().strftime("[%H:%M:%S]")

# Запуск логирования
logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.info(time() + "Bot start")

# Colors
r, g, b = '\033[31m', '\033[32m', '\033[34m'


# выбор делать рассылку о запуске бота или нет
if input('Тихий запуск? Y/n ').lower() == 'y':
    print(g + time() + '[i] Выполнен Тихий запуск')
    logging.info(time() + "Turn on silent start")
else:
    print(g + time() + '[i] Выполнен Обычный запуск')
    logging.info(time() + "Turn on normal start")
    mailing('Бот запущен на время')

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.obj.text.lower()
                if not event.obj.from_me:
                    print(g + time() + '[i] Новое сообщение от пользователя @id' + str(event.obj.peer_id))
                    logging.info(time() + "New message from @id" + str(event.obj.peer_id))
                    commands(event, msg)
    except:
        continue
        raise
