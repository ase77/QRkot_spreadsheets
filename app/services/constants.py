from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
TABLE_HEADER = [
    ['Отчет от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]

ROWS = 100
COLUMNS = 4
BODY_TABLE = dict(
    properties=dict(
        title=f'Отчет от {NOW_DATE_TIME}',
        locale='ru_RU',
    ),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(
            rowCount=ROWS,
            columnCount=COLUMNS,
        )
    ))]
)
