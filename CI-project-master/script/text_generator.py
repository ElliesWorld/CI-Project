#!/usr/bin/env python3

def generate_text_file(signals, macros) -> str:
    file = ""

    title = {
        "name": "Signal",
        "type": "Type",
        "values": "Values",
        "comment": "Description"
    }

    size = {}
    for key in title:
        size[key] = len(title[key])

    for signal in signals:
        for key in signal:
            if key == 'values':
                length = len(str(macros[signal[key]]))
            else:
                length = len(str(signal[key]))
            if size.get(key, 0) < length:
                size[key] = length

    file += "{} | {} | {} | {}\n".format(
        title['name'].ljust(size['name']),
        title['type'].ljust(size['type']),
        title['values'].ljust(size['values']),
        title['comment'].ljust(size['comment'])
    )

    file += '=' * (sum(size.values())) + '\n'

    for signal in signals:
        data = {}
        for key, value in signal.items():
            if key == "range":
                data['values'] = str(value)
            elif key == "values":
                if value in macros:
                    data['values'] = macros[value]
                else:
                    data['values'] = value
            else:
                data[key] = value

        file += "{} | {} | {} | {}\n".format(
            data.get('name', '').ljust(size['name']),
            data.get('type', '').ljust(size['type']),
            str(data.get('values', '')).ljust(size['values']),
            data.get('comment', '').capitalize().ljust(size['comment'])
        )

    return file

