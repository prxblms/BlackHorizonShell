import os, time, gettext, json

# load config.json.
with open('src\config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

config_lang = config['lang']

# get computer owner username.
username = os.getlogin()

# def DelayPrint2(text):
#     for x in text:
#         sys.stdout.write(x)
#         sys.stdout.flush()
#         time.sleep(0.02)

def delayPrint(text):
    for x in text:
        time.sleep(0.02)
        print(x, end='', flush=True)


# translator for different languages.
# command to convert .po to .mo:
# msgfmt messages.po -o LC_MESSAGES/messages.mo
def translator():
    lang = config_lang
    #lang = 'pt_BR'
    translation = gettext.translation('messages', localedir='locales', languages=[lang])
    translation.install()
    _lang_ = translation.gettext # set 'self._' to use translator.
    return _lang_