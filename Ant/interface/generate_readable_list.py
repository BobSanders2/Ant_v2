def generate_readable_list(list_to_process):
    processed_list = ["\"{}\"".format(item) for item in list_to_process]
    delimiter = ", "

    if len(processed_list) == 2:
        delimiter = " or "
    return delimiter.join(processed_list)
