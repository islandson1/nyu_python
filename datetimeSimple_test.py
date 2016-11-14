import datetimeSimple as dts
import datetime
import pytest

def test_print_default():
    x = dts.DateTimeSimple()
    assert str(x) == str(datetime.date.today())


def test_add_one_day():
    x = dts.DateTimeSimple('2016-06-06')
    x = x + 1 
    y = datetime.datetime.strptime('2016-06-07', '%Y-%m-%d')
    assert str(x) == str(y.strftime('%Y-%m-%d'))

def test_minus_one_day():
    x = dts.DateTimeSimple('2016-06-06')
    x = x - 1 
    y = datetime.datetime.strptime('2016-06-05', '%Y-%m-%d')
    assert str(x) == str(y.strftime('%Y-%m-%d'))

def test_minus_one_week():
    x = dts.DateTimeSimple('2016-06-10')
    x.add_week(-1) 
    y = datetime.datetime.strptime('2016-06-03', '%Y-%m-%d')
    assert str(x) == str(y.strftime('%Y-%m-%d'))

def test_add_two_weeks():
    x = dts.DateTimeSimple('2016-06-10')
    x.add_week(2) 
    y = datetime.datetime.strptime('2016-06-24', '%Y-%m-%d')
    assert str(x) == str(y.strftime('%Y-%m-%d'))

def test_add_days_leap_year():
    x = dts.DateTimeSimple('2016-02-28')
    x = x + 3 
    y = datetime.datetime.strptime('2016-03-02', '%Y-%m-%d')
    assert str(x) == str(y.strftime('%Y-%m-%d'))

def test_formats():
    x = dts.DateTimeSimple()
    y = datetime.date.today()

    x.set_format('MM/DD/YYYY')
    assert str(x) == str(y.strftime('%m/%d/%Y'))

    x.set_format('DD-Mon-YY')
    assert str(x) == str(y.strftime('%d-%b-%Y'))

    x.set_format('YYYY-MM-DD')
    assert str(x) == str(y.strftime('%Y-%m-%d'))
    
   
def test_bad_constructor_format():
   with pytest.raises(ValueError):
       x = dts.DateTimeSimple('Jun-06-2016')
   
def test_bad_set_format():
   with pytest.raises(ValueError):
       x = dts.DateTimeSimple()
       x.set_format('Mon-DD-YYYY')

def main():
   pass

if __name__ == '__main__':
    main()
	