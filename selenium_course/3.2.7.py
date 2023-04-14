def test_input_text(expected_result , actual_result ):
    try:
        assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
    except AssertionError as e:
        print(e)

test_input_text('8', '11')
test_input_text('11', '11')
test_input_text('11', '15')

# def test_input_text(expected_result, actual_result):
#     try:
#         assert expected_result == actual_result, f"Ошибка: ожидаемый результат '{expected_result}' не совпадает с фактическим результатом '{actual_result}'."
#     except AssertionError as e:
#         print(e)

# # Пример использования
# test_input_text(5, 3)  # Это вызовет ошибку
# test_input_text("Hello", "Hello")  # Это пройдет без ошибок