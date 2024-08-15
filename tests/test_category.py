def test_category(first_category, second_category):
    assert first_category.name == "овощи"
    assert first_category.description == "свежие овощи"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
