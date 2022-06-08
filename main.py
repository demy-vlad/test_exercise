from parsing_bytes import test_data, device_settings, parsed_data, field1, field4 ,field8


def conversion_to_bynary():
    '''Преобразование в двоичный'''
    dec = int(test_data[0][0], 16)
    bynar = bin(dec)
    get_device_settings(bynar)


def get_device_settings(bynar):
    '''Получаем bynary, пробегаемся циклом и получаем значения ключей [size, 'field_name']'''
    serial_number = 2
    for page, device_settings_all in enumerate(device_settings):
        for i in device_settings_all:
            device_setting = device_settings[page][i]

            print(device_setting)
            device_setting_number = device_setting[0]
            field_name = device_setting[1]
            result = serial_number + device_setting_number
            # print(f'C: {serial_number} По: {result}') 
            print(device_settings_all)
            get_size(serial_number, result, bynar, field_name)
            serial_number = result


def get_size(serial_number, result, bynar, field_name):
    '''Получаем нужный диапазон чисел. Затем переводим в bynary'''
    print(f'C: {serial_number} По: {result}')
    all_pages=[]
    page = serial_number
    while page < result:
        all_pages.append(page)
        page = page + 1

    bins_array = ''
    for find_bin in all_pages:
        bins_array += str(bynar[find_bin])
    change_to_decimal(bins_array, field_name)


def change_to_decimal(bins_array, field_name):
    '''Изменить на десятичную'''
    change_to_decimal = int('0b'+bins_array, 0)
    print(f'change_to_decimal: {change_to_decimal}')
    get_data_from_payload(change_to_decimal, field_name)


def get_data_from_payload(change_to_decimal, field_name):
    '''Получаем параметры field'''
    if field_name == 'field1':
        parsed_data.update({field_name: field1[str(change_to_decimal)]})
    elif field_name == 'field4':
        parsed_data.update({field_name: field4[str(change_to_decimal)]})
    elif field_name == 'field8':
        parsed_data.update({field_name: field8[str(change_to_decimal)]})


def get_parsed_data() -> str:
    '''Получаем рузультат'''
    print(parsed_data)
    return parsed_data



if __name__ == '__main__':
    conversion_to_bynary()
    get_parsed_data()