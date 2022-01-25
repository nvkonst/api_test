def test_huawei(api):
    endpoint = "/js-test-task"
    search_product = "Huawei"
    sort_field = "price"
    response = api.get_response(endpoint, search_product, sort_field)
    assert response.status_code == 200
    response_body = response.json()
    product_list = [api.get_instance(e) for e in response_body["products"]]
    # проверка сортировки по полю price
    assert sorted(product_list, key=lambda x: x.price) == product_list
    # проверка содержания "Huawei" в названиях товаров
    assert api.check_text_in_list_attributes(product_list, search_product)
