def human_years_cat_years_dog_years(human_years):
    """test.assert_equals(human_years_cat_years_dog_years(10), [10,56,64])"""
    
    cat_years = 0
    dog_years = 0

    if human_years == 1:
        cat_years = dog_years = 15
    elif human_years == 2:
        cat_years = dog_years = 15 + 9
    elif human_years > 2:
        cat_years = dog_years = 15 + 9
        for _ in range(3, human_years+1):
            cat_years += 4
            dog_years += 5
    return [human_years, cat_years, dog_years]

