test_cases = [
    {
        "phone_book": ["119", "97674223", "1195524421"],
        "return": False,
    },
    {
        "phone_book": ["123", "456", "789"],
        "return": True,
    },
    {
        "phone_book": ["12", "123", "1235", "567", "88"],
        "return": False,
    },
    {
        "phone_book": ["21", "1235", "567", "88", "12"],
        "return": False,
    },
    {
        "phone_book": ["12", "1235", "567", "88"],
        "return": False,
    },
]
