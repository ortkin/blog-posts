# blog_posts/views_test.py
"""
AAA testing - arrange, act, assert
"""
def test_add():
    # ARRANGE
    num1 = 10
    num2 = 5

    #ACT
    total = num1 + num2
    
    #ASSERT
    assert total == 15


def test_subtract():
    assert 10 - 5 == 3


"""
; pytest.ini
[pytest]
norecursedirs = .* _* venv
DJANGO_SETTINGS_MODULE = blog_posts.settings
addopts =
    --browser=chromium
    --tb=short

browser flag says use chromium
tb is a short traceback
"""