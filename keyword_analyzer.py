import re
from collections import Counter

def analyze_keywords(text, geo_keywords=None, app_keywords=None):
    """
    Analyzes text for general SEO, GEO, and AEO keywords.
    """
    # Normalize text to lowercase for case-insensitive matching
    text_lower = text.lower()

    # General SEO keyword analysis
    # Simple tokenization: split by non-alphanumeric characters
    words = re.findall(r'\b\w+\b', text_lower)
    seo_keyword_counts = Counter(words)

    # GEO keyword analysis (if provided)
    geo_keyword_results = {}
    if geo_keywords:
        for keyword in geo_keywords:
            # Count occurrences of the specific geo keyword
            geo_keyword_results[keyword] = text_lower.count(keyword.lower())

    # AEO keyword analysis (if provided)
    aeo_keyword_results = {}
    if app_keywords:
        for keyword in app_keywords:
            # Count occurrences of the specific app keyword
            aeo_keyword_results[keyword] = text_lower.count(keyword.lower())

    return {
        "seo_keyword_counts": dict(seo_keyword_counts),
        "geo_keyword_counts": geo_keyword_results,
        "aeo_keyword_counts": aeo_keyword_results
    }

if __name__ == "__main__":
    # Example SaaS website content
    website_content = """
    Our SaaS platform offers the best online invoicing software for small businesses in Turkey.
    Manage your projects efficiently with our cloud-based project management tool. 
    We also provide mobile app development services for startups.
    Find local accounting software solutions near Istanbul.
    Download our app from Google Play for seamless invoicing.
    """

    # Example keywords for GEO and AEO
    geo_targets = ["Turkey", "Istanbul", "local accounting software"]
    app_targets = ["mobile app", "Google Play", "download our app"]

    analysis_results = analyze_keywords(website_content, geo_keywords=geo_targets, app_keywords=app_targets)

    print("--- Keyword Analysis Results ---")

    print("\nGeneral SEO Keywords (Top 10):")
    # Display top 10 most frequent words as a proxy for general SEO keywords
    for word, count in sorted(analysis_results["seo_keyword_counts"].items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"- {word}: {count}")

    print("\nGEO Keywords:")
    # Display counts for specific geographic keywords
    for keyword, count in analysis_results["geo_keyword_counts"].items():
        print(f"- {keyword}: {count}")

    print("\nAEO Keywords:")
    # Display counts for specific app store keywords
    for keyword, count in analysis_results["aeo_keyword_counts"].items():
        print(f"- {keyword}: {count}")
