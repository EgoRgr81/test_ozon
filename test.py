import pytest
from functions import get_tallest_hero, get_api


def test_check_response_is_200():
    response_status = get_api().status_code
    assert response_status == 200


def test_get_tallest_hero_male_with_job():
    hero = get_tallest_hero('Male', True)
    assert hero is not None
    assert hero['appearance']['gender'] == 'Male'
    assert hero['work']['occupation'] != '-'


def test_get_tallest_hero_male_without_job():
    hero = get_tallest_hero('Male', False)
    assert hero is not None
    assert hero['appearance']['gender'] == 'Male'
    assert hero['work']['occupation'] == '-'


def test_get_tallest_hero_female_with_job():
    hero = get_tallest_hero('Female', True)
    assert hero is not None
    assert hero['appearance']['gender'] == 'Female'
    assert hero['work']['occupation'] != '-'


def test_get_tallest_hero_female_without_job():
    hero = get_tallest_hero('Female', False)
    assert hero is not None
    assert hero['appearance']['gender'] == 'Female'
    assert hero['work']['occupation'] == '-'


def test_get_tallest_hero_invalid_gender():
    with pytest.raises(ValueError):
        get_tallest_hero('Non', True)


def test_get_tallest_hero_invalid_has_job():
    with pytest.raises(ValueError):
        get_tallest_hero('Male', 'Non')


def test_get_tallest_hero_invalid_all():
    with pytest.raises(ValueError):
        get_tallest_hero('Non', 'Non')
