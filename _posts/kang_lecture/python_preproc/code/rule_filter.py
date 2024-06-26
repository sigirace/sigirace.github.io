import re

class Rule(object):
    def __init__(self, spam_keywords):
        self.spam_keywords = spam_keywords

    def check(self, mail_text):
        mail_text = set(re.findall(r'\b\w+\b', mail_text.lower()))
        common_words = mail_text.intersection(self.spam_keywords)
        if len(common_words) > 0:
            print("스팸입니다.")
            return True
        else:
            print("스팸이 아닙니다.")
            return False