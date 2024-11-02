import requests
import time
import pandas as pd
from pandas import json_normalize
import numpy as np
from tqdm import tqdm
from random import randint
import datetime
from io import StringIO


class proxy:
    proxyHost = "u8804.5.tn.16yun.cn"
    proxyPort = "6441"
    proxyUser = "16IHUBEP"
    proxyPass = "727634"
    user_agents = []
    proxies = {}

    def __init__(self, proxyHost, proxyPort, proxyUser, proxyPass, user_agents):
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort
        self.proxyUser = proxyUser
        self.proxyPass = proxyPass
        self.user_agents = user_agents
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        self.proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }


def download_url(url, ifuse_proxy=False, proxy=None):
    if (ifuse_proxy):
        time.sleep(0.5)  # 调用多线程时不需要这一行
        random_agent = proxy.user_agents[
            randint(0, len(proxy.user_agents) - 1)]  # chose an user agent from the user agent list above
        tunnel = randint(1, 10000)  # generate a tunnel
        header = {
            "Proxy-Tunnel": str(tunnel),
            "User-Agent": random_agent
        }

    # print(header,proxy.proxies)

    try:
        if (ifuse_proxy):
            content = requests.get(url, timeout=100, headers=header, proxies=proxy.proxies)
        else:
            content = requests.get(url, timeout=100, proxies=proxy)
        ''' note that sometimes we only get error informations in the responses, and here are some really dumb quick fixes'''
        if (
                content.text == "<html><body><h1>502 Bad Gateway</h1>\nThe server returned an invalid or incomplete response.\n</body></html>\n" or content.text == "Too Many Requests.\n" or content.text == "{\"Message\":\"An error has occurred.\"}"):
            with open("./uncomtrade_data/serverError.csv", 'a', encoding="utf-8") as log:
                log.write(str(datetime.datetime.now()) + "," + str(url) + "\n")
                print("\n" + content.content.decode())
                if (ifuse_proxy):
                    download_url(url, ifuse_proxy=True, proxy=proxy)
                else:
                    download_url(url, ifuse_proxy=False, proxy=None)
        else:
            if ('json' in url):
                return json_normalize(content.json()['dataset'])
            elif ('csv' in url):
                return pd.read_csv(StringIO(content.text), on_bad_lines='skip')

    except requests.RequestException as e:
        ''' I have absolutely no knowledge about Request Exception Handling so I chose to write the error information to a log file'''
        print(type(e).__name__ + " has occurred, change proxy!")
        #         if(type(e).__name__=='JSONDecodeError'):
        #             print(content.content)
        with open("./uncomtrade_data/exp.csv", 'a', encoding="utf-8") as log:
            log.write(
                str(datetime.datetime.now()) + "," + str(type(e).__name__) + "," + str(url) + "\n")
        if (ifuse_proxy):
            download_url(url, ifuse_proxy=True, proxy=proxy)
        else:
            download_url(url, ifuse_proxy=False, proxy=None)


def get_data_un_comtrade(max_un=100000, r='156', freq='A', ps='2021', px='S4', p='all', rg='2', cc='TOTAL', fmt='json',
                         type_un='C', ifuse_proxy=False, proxy=None):
    '''
    max_un：最大返回数据量(默认为100000)；
    r：reportering area，选择所需要的目标国家；
    freq：选择数据为年度或月度（A,M）；
    ps：选择所需要的年份；
    px：选择分类标准，如常用的SITC Revision 3为S3；
    p：partner area，选择所需要的对象国家，如需要中国与俄罗斯的出口额，则目标为中国，对象为俄罗斯；
    rg：选择进口或出口（进口为1，出口为2）；
    cc：选择产品代码；
    fmt：选择输出文件格式，csv或json,默认使用json(实测中csv更快)；
    type_un：选择贸易类型，产品或服务;
    ifuse_proxy:是否使用代理；
    proxy:代理信息。

    return:{数据名称: 数据}{str:dataframe}
    '''
    pre_url = "http://comtrade.un.org/api//get/plus?max={}&type={}&freq={}&px={}&ps={}&r={}&p={}&rg={}&cc={}&fmt={}"
    url_use = pre_url.format(max_un, type_un, freq, px, ps, r, p, rg, cc, fmt)
    print("Getting data from:" + url_use)
    data = download_url(url_use, ifuse_proxy=ifuse_proxy, proxy=proxy)
    if (rg == 1):
        ex_or_in = 'IMPORT'
    else:
        ex_or_in = 'EXPORT'
    data_name = ps + "_" + r + "_" + p + "_" + px + "_" + cc + "_" + ex_or_in + "_" + freq
    return {data_name: data}


countries = {'156': 'China', '344': 'China, Hong Kong SAR', '446': 'China, Macao SAR', '4': 'Afghanistan',
             '8': 'Albania', '12': 'Algeria', '20': 'Andorra', '24': 'Angola', '660': 'Anguilla',
             '28': 'Antigua and Barbuda', '32': 'Argentina', '51': 'Armenia',
             '533': 'Aruba', '36': 'Australia', '40': 'Austria', '31': 'Azerbaijan', '44': 'Bahamas', '48': 'Bahrain',
             '50': 'Bangladesh', '52': 'Barbados',
             '112': 'Belarus', '56': 'Belgium', '58': 'Belgium-Luxembourg', '84': 'Belize', '204': 'Benin',
             '60': 'Bermuda', '64': 'Bhutan', '68': 'Bolivia (Plurinational State of)', '535': 'Bonaire',
             '70': 'Bosnia Herzegovina', '72': 'Botswana', '92': 'Br. Virgin Isds', '76': 'Brazil',
             '96': 'Brunei Darussalam', '100': 'Bulgaria', '854': 'Burkina Faso', '108': 'Burundi', '132': 'Cabo Verde',
             '116': 'Cambodia',
             '120': 'Cameroon', '124': 'Canada', '136': 'Cayman Isds', '140': 'Central African Rep.', '148': 'Chad',
             '152': 'Chile',
             '170': 'Colombia', '174': 'Comoros', '178': 'Congo', '184': 'Cook Isds', '188': 'Costa Rica',
             '384': "Côte d'Ivoire", '191': 'Croatia', '192': 'Cuba', '531': 'Curaçao', '196': 'Cyprus',
             '203': 'Czechia',
             '200': 'Czechoslovakia', '408': "Dem. People's Rep. of Korea", '180': 'Dem. Rep. of the Congo',
             '208': 'Denmark', '262': 'Djibouti', '212': 'Dominica', '214': 'Dominican Rep.', '218': 'Ecuador',
             '818': 'Egypt', '222': 'El Salvador', '226': 'Equatorial Guinea', '232': 'Eritrea', '233': 'Estonia',
             '231': 'Ethiopia', '234': 'Faeroe Isds', '238': 'Falkland Isds (Malvinas)', '242': 'Fiji',
             '246': 'Finland',
             '251': 'France', '254': 'French Guiana', '258': 'French Polynesia', '583': 'FS Micronesia', '266': 'Gabon',
             '270': 'Gambia', '268': 'Georgia', '276': 'Germany', '288': 'Ghana', '292': 'Gibraltar',
             '300': 'Greece', '304': 'Greenland', '308': 'Grenada', '312': 'Guadeloupe', '320': 'Guatemala',
             '324': 'Guinea', '624': 'Guinea-Bissau', '328': 'Guyana', '332': 'Haiti',
             '336': 'Holy See (Vatican City State)',
             '340': 'Honduras', '348': 'Hungary', '352': 'Iceland', '699': 'India', '364': 'Iran', '368': 'Iraq',
             '372': 'Ireland', '376': 'Israel', '381': 'Italy', '388': 'Jamaica', '392': 'Japan',
             '400': 'Jordan', '398': 'Kazakhstan', '404': 'Kenya', '296': 'Kiribati', '414': 'Kuwait',
             '417': 'Kyrgyzstan', '418': "Lao People's Dem. Rep.", '428': 'Latvia', '422': 'Lebanon', '426': 'Lesotho',
             '430': 'Liberia', '434': 'Libya', '440': 'Lithuania', '442': 'Luxembourg', '450': 'Madagascar',
             '454': 'Malawi', '458': 'Malaysia', '462': 'Maldives', '466': 'Mali', '470': 'Malta',
             '584': 'Marshall Isds',
             '474': 'Martinique', '478': 'Mauritania', '480': 'Mauritius', '175': 'Mayotte', '484': 'Mexico',
             '496': 'Mongolia', '499': 'Montenegro', '500': 'Montserrat', '504': 'Morocco', '508': 'Mozambique',
             '104': 'Myanmar',
             '580': 'N. Mariana Isds', '516': 'Namibia', '524': 'Nepal', '530': 'Neth. Antilles',
             '532': 'Neth. Antilles and Aruba', '528': 'Netherlands', '540': 'New Caledonia', '554': 'New Zealand',
             '558': 'Nicaragua',
             '562': 'Niger', '566': 'Nigeria', '579': 'Norway', '512': 'Oman', '586': 'Pakistan', '585': 'Palau',
             '591': 'Panama', '598': 'Papua New Guinea', '600': 'Paraguay', '459': 'Peninsula Malaysia', '604': 'Peru',
             '608': 'Philippines',
             '616': 'Poland', '620': 'Portugal', '634': 'Qatar', '410': 'Rep. of Korea', '498': 'Rep. of Moldova',
             '638': 'Réunion', '642': 'Romania', '643': 'Russian Federation', '646': 'Rwanda', '647': 'Ryukyu Isd',
             '461': 'Sabah',
             '652': 'Saint Barthelemy', '654': 'Saint Helena', '659': 'Saint Kitts and Nevis', '662': 'Saint Lucia',
             '534': 'Saint Maarten', '666': 'Saint Pierre and Miquelon', '670': 'Saint Vincent and the Grenadines',
             '882': 'Samoa', '674': 'San Marino', '678': 'Sao Tome and Principe', '457': 'Sarawak',
             '682': 'Saudi Arabia', '686': 'Senegal', '688': 'Serbia', '690': 'Seychelles', '694': 'Sierra Leone',
             '702': 'Singapore',
             '703': 'Slovakia', '705': 'Slovenia', '90': 'Solomon Isds', '706': 'Somalia', '710': 'South Africa',
             '728': 'South Sudan', '724': 'Spain', '144': 'Sri Lanka', '275': 'State of Palestine',
             '729': 'Sudan', '740': 'Suriname', '748': 'Eswatini', '752': 'Sweden', '757': 'Switzerland',
             '760': 'Syria', '762': 'Tajikistan', '807': 'North Macedonia', '764': 'Thailand', '626': 'Timor-Leste',
             '768': 'Togo', '772': 'Tokelau', '776': 'Tonga', '780': 'Trinidad and Tobago', '788': 'Tunisia',
             '795': 'Turkmenistan', '796': 'Turks and Caicos Isds', '798': 'Tuvalu', '800': 'Uganda',
             '804': 'Ukraine', '784': 'United Arab Emirates', '826': 'United Kingdom', '834': 'United Rep. of Tanzania',
             '858': 'Uruguay', '850': 'US Virgin Isds', '842': 'USA', '860': 'Uzbekistan',
             '548': 'Vanuatu', '862': 'Venezuela', '704': 'Viet Nam', '876': 'Wallis and Futuna Isds', '887': 'Yemen',
             '894': 'Zambia', '716': 'Zimbabwe'}

temp = get_data_un_comtrade(max_un = 100000,r = '156',freq = 'A',ps = '2021',px = 'S4',p = 'all',rg = '2',cc = 'TOTAL',fmt = 'json',type_un ='C',ifuse_proxy = False ,proxy = None )
temp_name = list(temp.keys())[0]
print("DATA NAME IS "+temp_name)
temp[temp_name]
