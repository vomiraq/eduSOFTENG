from datetime import datetime as dt
from datetime import timedelta as td

def main():
    days_w = ['', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    today = dt.today()
    print(
        f"Сегодня {today.date()}. "
        f"День недели - {days_w[today.isoweekday()]}"
    )
    n = int(input('Введите количество дней: '))
    result = today + td(days = n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {days_w[result.isoweekday()]}"
    )

if __name__ == '__main__':
    main()