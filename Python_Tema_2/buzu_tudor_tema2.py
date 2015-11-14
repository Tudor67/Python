from datetime import date, timedelta



class DateRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_days(self):
        return (self.end - self.start).days

    days = property(get_days)

    def contains(self, zi):
        return self.start <= zi and zi <= self.end


    
class Car(object):
    def __init__(self, brand, model, daily_price):
        self.brand = brand
        self.model = model
        self.daily_price = daily_price

    def get_rental_price(self, period):
        return self.daily_price * period.days

    def __str__(self):
        return "Acesta este un {0} {1} si pretul la inchiriere este {2}".format(self.brand, self.model, self.daily_price)



class Limousine(Car):
    def __init__(self, nume, model, daily_price, driver_salary):
        super(Limousine, self).__init__(nume, model, daily_price)
        self._driver_salary = driver_salary
        
    def get_rental_price(self, period):
        return period.days * self.daily_price + self._driver_salary



class Person(object):
    def __init__(self, first_name, last_name, birthday):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthday = birthday
    
    def get_birthday(self):
        return self.__birthday

    birthday = property(get_birthday)



class CarRental(object):
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        self.__cars += [car]

    def get_cars(self, brand='', max_price=-1):
        self.sol = []
        for x in self.__cars:
            if (brand == x.brand or brand == '') and (x.daily_price <= max_price or max_price == -1):
                self.sol += [x]
        return self.sol

    def get_price(self, customer, car, period):
        self.__year = int(period.start.strftime('%Y'))
        self.__month = int(customer.birthday.strftime('%m'))
        self.__day = int(customer.birthday.strftime('%d')) 
        if period.contains(date(self.__year,self.__month,self.__day)) or period.contains(date(self.__year+1,self.__month,self.__day)):
            return 0.9 * car.get_rental_price(period)
        else:
            return car.get_rental_price(period)



class Point(object):
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __add__(self, p):
          return Point(self.x + p.x, self.y + p.y)

      def __sub__(self, p):
          return Point(self.x - p.x, self.y - p.y)


# Functia ajutatoare folosita la testare
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '
    print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)



# Functia care testeaza rezultatele
def main():
    print "\nTeste pentru clasa DateRange"
    start = date(2012, 6, 24)
    end = date(2014, 1, 1)
    dr = DateRange(start, end)
    test(dr.contains(date(2012, 6, 24)), True)
    test(dr.contains(date(2014, 1, 1)), True)
    test(dr.contains(date(2013, 6, 24)), True)
    test(dr.contains(date(2014, 6, 24)), False)
    test(dr.days, 556)
 

    print "\nTeste pentru clasa Car"
    c = Car('Volvo', 'S60', 500)
    dr = DateRange(date.today(), date.today()+timedelta(days=7))
    test(c.get_rental_price(dr), 3500)
    test(str(c), "Acesta este un Volvo S60 si pretul la inchiriere este 500")
    print "\nTeste pentru clasa Limousine"
    l = Limousine('Mercedes', 'Diplomat Edition', 1200, 800)
    dr = DateRange(date.today(), date.today()+timedelta(days=3))
    test(l.get_rental_price(dr), 4400)


    print "\nTeste pentru clasa CarRental"
    c2 = Car('Mercedes', 'C-Class', 700)
    cr = CarRental()
    cr.add_car(c)
    cr.add_car(l)
    cr.add_car(c2)
    test(cr.get_cars(), [c, l, c2])
    test(cr.get_cars('Mercedes'), [l, c2])
    test(cr.get_cars('Mercedes', 700), [c2])
    test(cr.get_cars(max_price=600), [c])
    test(cr.get_cars(max_price=400), [])

    p = Person('Jane', 'Geller', date(1992, 12, 5))
    p2 = Person('John', 'Stain', date(1990, 12, 15))
    dr = DateRange(date(2015, 12, 1), date(2015, 12, 10))
    test(cr.get_price(p, c, dr), 4050)
    test(cr.get_price(p2, c2, dr), 6300)


    print "\nTeste pentru clasa Point"
    p1 = Point(1, 2)
    p2 = Point(3, 3)
    p3 = p1 + p2
    test(p3.x, p1.x + p2.x)
    test(p3.y, p1.y + p2.y)
    p3 = p1 - p2
    test(p3.x, p1.x - p2.x)
    test(p3.y, p1.y - p2.y)

if __name__ == '__main__':
    main()

