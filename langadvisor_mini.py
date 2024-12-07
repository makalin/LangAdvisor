def analyze_prompt(prompt):
    # Detailed keywords for each language
    prolog_keywords = [
        "logic", "ai", "inference", "rule", "nlp", "reasoning", "knowledge", "expert system",
        "symbolic", "facts", "rules", "queries", "logical inference", "pattern matching"
    ]
    python_keywords = [
        "data", "machine learning", "ml", "ai", "web", "automation", "script", "visualization", "beginner",
        "deep learning", "analysis", "nlp", "framework", "pandas", "numpy", "flask", "django", "prototype"
    ]
    rust_keywords = [
        "performance", "system", "safety", "memory", "concurrent", "embedded", "high-performance", "os",
        "real-time", "low-level", "game", "browser", "concurrency", "compile-time safety", "efficient",
        "hardware"
    ]

    # Scores for each language
    scores = {"Prolog": 0, "Python": 0, "Rust": 0}

    # Analyze the prompt
    words = prompt.lower().split()
    for word in words:
        if word in prolog_keywords:
            scores["Prolog"] += 1
        if word in python_keywords:
            scores["Python"] += 1
        if word in rust_keywords:
            scores["Rust"] += 1

    return scores

def recommend_language(scores):
    max_score = max(scores.values())
    recommended_languages = [lang for lang, score in scores.items() if score == max_score]

    if max_score == 0:
        return "No clear match found. Try providing more specific details in your prompt."
    if len(recommended_languages) == 1:
        return f"The best programming language for your use case is: {recommended_languages[0]}"
    else:
        return f"Multiple languages could work for your use case: {', '.join(recommended_languages)}"

def main():
    print("\n--- Programming Language Recommender ---")
    print("Enter a brief description of your project or use case, and this app will recommend a language.")
    while True:
        prompt = input("\nEnter your project description (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        scores = analyze_prompt(prompt)
        recommendation = recommend_language(scores)
        print("\n" + recommendation)

if __name__ == "__main__":
    main()
