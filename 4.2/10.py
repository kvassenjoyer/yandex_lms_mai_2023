def secret_replace(message, **kwargs):
    # Ключевой секрет

    for symbol, replace_tuple in kwargs.items():
        for i in range(message.count(symbol)):
            index = i % len(replace_tuple)
            message = message.replace(symbol, replace_tuple[index], 1)

    return message
