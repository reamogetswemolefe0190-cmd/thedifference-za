with open(".agents/teamwork/challenger_m1_2/test_suite.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('Filter query \'PS5\'')
print(text[idx-50:idx+800])
