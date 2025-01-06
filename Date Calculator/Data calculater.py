from sly import Lexer, Parser
import datetime
class DateLexer(Lexer):
    tokens = { DATE, PLUS,NUMBER, MINUS }
    ignore = ' \t\n'
    DATE = r'(?:0?[1-9]|[12][0-9]|3[01])/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}'
    PLUS = r'\+'
    MINUS = r'-'
    NUMBER=r'[0-9]+'


class DateParser(Parser):
    tokens = DateLexer.tokens

    day_dict = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_dict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    @_('DATE')
    def date(self, p):
        return p.DATE

    @_('date PLUS NUMBER')
    def date(self, p):
        day, month, year = p.date.split('/')
        day = int(day)
        year = int(year)

        month_num = self.month_dict[month.lower()]
        day += int(p.NUMBER)
        while(day > self.day_dict[month_num]):
            if day > self.day_dict[month_num]:
                day -= self.day_dict[month_num]
                month_num += 1
            if month_num > 12:
                month_num -= 12
                year += 1
            
        return f'{day:02d}/{month_num}/{year}'
        # {list(self.month_dict.keys())[list(self.month_dict.values()).index(month_num)].capitalize()}
    @_('date MINUS NUMBER')
    def date(self, p):
        day, month, year = p.date.split('/')
        day = int(day)
        year = int(year)

        month_num = self.month_dict[month.lower()]
        day -= int(p.NUMBER)
        if day == 0:
            day += self.day_dict[month_num]
            month_num -= 1
            if month_num < 1:
                month_num += 12
                year -= 1
        while(day < 0):
        
            day += self.day_dict[month_num]
            month_num -= 1
            if month_num < 1:
                month_num += 12
                year -= 1
        # return f'{day:02d}/{list(self.month_dict.keys())[list(self.month_dict.values()).index(month_num)].capitalize()}/{year}'
        return f'{day:02d}/{month_num}/{year}'

    @_('date MINUS date')
    def date(self,value):
        day1, month1, year1 = value.date0.split('/')
        day2, month2, year2 = value.date1.split('/')
        day1 = int(day1)
        year1 = int(year1)
        day2 = int(day2)
        year2 = int(year2)

        month_num1 = self.month_dict[month1.lower()]
        month_num2 = self.month_dict[month2.lower()]
        # a=t[0].split('/')
        # b=t[2].split('/')
        
        # print(a)
        date1=datetime.date(year1,month_num1,day1)
        date2=datetime.date(year2,month_num2,day2)
        # print(date1)
        # print(date2)
        # print(abs((date1-date2).days))
        return abs((date1-date2).days)

lexer = DateLexer()
parser = DateParser()

data = '''
            10/Nov/2023-365
            '''
tokens = lexer.tokenize(data)
# for token in tokens:
#     print(token.type, token.value)


result = parser.parse(tokens)
print(result)
