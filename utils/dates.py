# utils/dates.py

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from babel.dates import format_date

def first_day_previous_month_iso():
    """
    Retorna a data do primeiro dia do mês anterior no formato ISO (YYYY-MM-DD).
    """
    today = date.today()
    first_day_this_month = today.replace(day=1)
    last_day_previous_month = first_day_this_month - timedelta(days=1)
    first_day = last_day_previous_month.replace(day=1)
    return first_day.isoformat()

def last_month():
    """
    Retorna o nome do mês anterior no formato completo (ex: 'Outubro'), em português.
    """
    last_month_date = datetime.now() - relativedelta(months=1)
    return format_date(last_month_date, "MMMM", locale="pt_BR").capitalize()

def actual_month():
    """
    Retorna o nome do mês atual no formato completo (ex: 'Novembro'), em português.
    """
    return format_date(datetime.now(), "MMMM", locale="pt_BR").capitalize()

def obtain_dates():
    today = date.today()
    yesterday = today - timedelta(days=1)

    if today.month == 1:
        first_day_last_month = date(today.year - 1, 12, 1)
    else:
        first_day_last_month = date(today.year, today.month - 1, 1)

    low = first_day_last_month.strftime("%d%m%Y")
    high = yesterday.strftime("%d%m%Y")

    # NOVAS DATAS PARA KSB1
    low_ksb1 = (today - timedelta(days=3)).strftime("%d%m%Y")
    high_ksb1 = yesterday.strftime("%d%m%Y")

    return low, high, low_ksb1, high_ksb1, today

def validate_date(data: str) -> bool:
    """
    Valida uma data nos formatos:
    - ddmmyyyy
    - dd.mm.yyyy
    Retorna True se a data for válida, False caso contrário.
    """

    data = data.strip()

    # Aceita apenas dígitos e pontos
    for c in data:
        if not (c.isdigit() or c == '.'):
            return False
        
    # Tenta dd.mm.yyyy
    try:
        if "." in data:
            datetime.strptime(data, "%d.%m.%Y")
            return True
    except ValueError:
        pass

    # Tenta ddmmyyyy
    try:
        if len(data) == 8 and data.isdigit():
            datetime.strptime(data, "%d%m%Y")
            return True
    except ValueError:
        pass

    return False

def january(year: int) -> str:
    return f'0101{year}'