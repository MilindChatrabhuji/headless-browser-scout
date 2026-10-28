from headless_browser_scout import extract_clean_dom, BrowserScoutConfig

def test_extract_clean_dom():
    html = "<html><head><script>alert(1);</script><style>body{color:red;}</style></head><body><h1>Content</h1></body></html>"
    clean = extract_clean_dom(html)
    assert "<script>" not in clean
    assert "<style>" not in clean
    assert "<h1>Content</h1>" in clean
