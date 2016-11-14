import datetime

class DateTimeSimple(object):
    
    def __init__(self, date_value=None):
        self.date_format = {'YYYY-MM-DD':'%Y-%m-%d', 'MM/DD/YYYY':'%m/%d/%Y', 'DD-Mon-YY':'%d-%b-%Y'}
        self.current_format = self.date_format['YYYY-MM-DD']
        self.mydate = None
        
        if date_value:
            for format_item in self.date_format:
                try:
                    self.mydate = datetime.datetime.strptime(date_value, self.date_format[format_item])
                except ValueError:
                    continue
            
            if not self.mydate:
                raise ValueError('{0} does not match expected formats: {1}'.format(date_value, self.date_format))
        else:
            self.mydate = datetime.date.today()
        

    def add_day(self, num_days=1):
        date_delta = datetime.timedelta(days=num_days)
        self.mydate = self.mydate + date_delta
        return self
    
    def add_week(self, num_weeks=1):
        self.add_day(num_days=7*num_weeks)
        
    def set_format(self, str_format):
        try:
            self.current_format = self.date_format[str_format]
        except KeyError:
            raise ValueError('{0} is not a supported format: {1}'.format(str_format, self.date_format.keys()))
    
                
    def __repr__(self):
        return self.mydate.strftime(self.current_format)
    
    def __add__(self, other):
        return self.add_day(other)

    def __sub__(self, other):
        return self.add_day(-1 * other)
    
def main():
    x=DateTimeSimple()
    print '1:', x

    x = DateTimeSimple('2016-06-06')
    print '2:', x

    x = DateTimeSimple('06-Jun-2016')
    print '3:', x

    x = DateTimeSimple('06/06/2016')
    print '4:', x

    try:
        x = DateTimeSimple('Jun-06-2016')
        print '5:', x
    except ValueError:
         print 'bad convertion'
        
    x = x + 1
    print x

    x = x - 5
    print x

    x.set_format('MM/DD/YYYY')
    print x

    x = x + 1
    print x

if __name__ == '__main__':       # value is '__main__' if this script is executed
                                 # value is 'datetime_simple' if this script is imported
    main()