with open(".agents/teamwork/challenger_m1_2/test_suite.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update card count checks from == 8 to >= 8 (to support catalog scaling up to 50 and 200)
content = content.replace("initial_cards == 8", "initial_cards >= 8")
content = content.replace('Initial Catalog Card Count (8)', 'Initial Catalog Card Count (>= 8)')

content = content.replace("cleared_cards == 8", "cleared_cards >= 8")
content = content.replace("Clear Button resets grid to 8 cards", "Clear Button resets grid to full catalog")

content = content.replace("reset_cards == 8", "reset_cards >= 8")
content = content.replace("Empty state 'Reset Search' button restores 8 cards", "Empty state 'Reset Search' button restores full catalog")

content = content.replace("cards_after_esc == 8", "cards_after_esc >= 8")

content = content.replace("cnt == 8", "cnt >= 8")

# 2. Add Category Filter verification test right after Store Filter test
category_test = """
        # 5G. Category Tabs Verification (Black Friday Expansion)
        category_chips_count = page.locator(".cat-chip").count()
        cat_filter_ok = category_chips_count >= 7
        record("Category Navigation", "Category Navigation Bar rendered with >= 7 categories", cat_filter_ok, f"Categories count: {category_chips_count}")

        # Test clicking 'Gaming' category
        page.evaluate("filterByCategory('Gaming Consoles')")
        page.wait_for_timeout(100)
        gaming_cards = page.locator(".product-card").count()
        record("Category Navigation", "Filtering by 'Gaming Consoles' shows matching category deals", gaming_cards >= 5, f"Gaming cards: {gaming_cards}")

        # Reset category to ALL
        page.evaluate("filterByCategory('ALL')")
        page.wait_for_timeout(100)
"""

store_filter_marker = "record(\"Store Filters\", \"All store filter chips filter successfully\", filter_ok, \"All chips tested\")"
assert store_filter_marker in content, "store_filter_marker not found"

content = content.replace(store_filter_marker, store_filter_marker + "\n" + category_test, 1)

with open(".agents/teamwork/challenger_m1_2/test_suite.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated test_suite.py with category tests and flexible catalog scaling assertions!")
