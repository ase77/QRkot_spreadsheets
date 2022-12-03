from datetime import timedelta

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.services import constants as const


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    '''Функция создания таблицы'''
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=const.BODY_TABLE)
    )
    spreadsheet_id = response['spreadsheetId']
    print(spreadsheet_id)
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    '''Функция для предоставления прав доступа'''
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    '''Записывает полученную из БД информацию в документ с таблицами'''
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = const.TABLE_HEADER
    for project in projects:
        print(project, type(project))
        new_row = [
            str(project['name']),
            str(timedelta(project['_no_label'])),
            str(project['description'])
        ]
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }

    try:
        await wrapper_services.as_service_account(
            service.spreadsheets.values.update(
                spreadsheetId=spreadsheet_id,
                range='A1:D100',
                valueInputOption='USER_ENTERED',
                json=update_body
            )
        )
    except ValueError:
        print('Проверьте входящие данные')
