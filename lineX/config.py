
# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re, json, requests, urllib
class Config(object):
    LINE_HOST_DOMAIN            = 'https://gwx.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-jp.line-apps.com' #https://xcdn-cn-shp.line-apps.com
    LINE_TIMELINE_API           = 'https://gwx.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gwx.line.naver.jp/mh'
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'
    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '8.14.2',
        'IOS': '8.14.2',
        'ANDROIDLITE': '2.1.0',
        'BIZANDROID': '1.7.2',
        'BIZIOS': '1.7.5',
        'BIZWEB': '1.0.22',
        'DESKTOPWIN': '5.9.0',
        'DESKTOPMAC': '5.9.0',
        'IOSIPAD': '8.14.2',
        'CHROMEOS': '2.1.5',
        'WIN10': '5.5.5',
        'DEFAULT': '8.11.0',
        'CLOVAFRIENDS':'5.5.1'
    }

    APP_TYPE    = 'IOSIPAD'
    APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']        
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'InexBots'
    SYSTEM_VER  = '11.2.5'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    def __init__(self):
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER
