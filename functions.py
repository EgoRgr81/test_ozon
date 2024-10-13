import requests


def get_api():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response_all = requests.get(url)
    return response_all


def get_tallest_hero(gender, has_work):

    if gender not in ['Male', 'Female']:
        raise ValueError("Параметр gender должен быть 'Male' или 'Female'.")

    if not isinstance(has_work, bool):
        raise ValueError("Параметр has_work должен быть булевым значением (True или False).")

    response = get_api()
    data = response.json()

    tallest_hero = None
    max_height = -1

    for hero in data:
        if hero['appearance']['gender'] == gender:
            if has_work and hero['work']['occupation'] == "-":
                continue
            elif not has_work and hero['work']['occupation'] != "-":
                continue
            height_cm = float(hero['appearance']['height'][1].split()[0])
            if height_cm > max_height:
                max_height = height_cm
                tallest_hero = hero

    return tallest_hero


