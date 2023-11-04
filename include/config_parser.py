import tomli


def parse_config(config_file_path, stylesheet_url, lang_attribute):
    try:
        with open(config_file_path, "rb") as config_file:
            config_data = tomli.load(config_file)

            stylesheet_url = config_data.get("stylesheet", stylesheet_url)
            lang_attribute = config_data.get("lang", lang_attribute)
    except FileNotFoundError:
        print(f"Config file not found: {config_file_path}")
    except tomli.TOMLDecodeError:
        print(f"Error parsing the config file: {config_file_path}")

    return stylesheet_url, lang_attribute
