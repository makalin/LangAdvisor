def analyze_prompt(prompt):
    # Detailed keywords for each language
    # Comprehensive keyword lists for different programming languages

    prolog_keywords = [
    # Core Concepts
    "logic", "ai", "inference", "rule", "nlp", "reasoning", "knowledge", "expert system",
    "symbolic", "facts", "rules", "queries", "logical inference", "pattern matching",
    
    # Technical Features
    "backtracking", "unification", "predicate logic", "first-order logic", "horn clauses",
    "declarative programming", "constraint logic", "term rewriting", "recursive rules",
    
    # Application Domains
    "expert systems", "natural language processing", "automated reasoning",
    "knowledge representation", "semantic web", "ontology modeling", "rule-based systems",
    "logical programming", "constraint satisfaction", "theorem proving",
    
    # Development Concepts
    "logic database", "knowledge base", "inference engine", "resolution principle",
    "symbolic computation", "meta-programming", "dynamic knowledge base",
    
    # Tools and Frameworks
    "swi-prolog", "gnu prolog", "visual prolog", "tau prolog", "prolog engines",
    "constraint handling rules", "definite clause grammars", "semantic frameworks",
    
    # Use Cases
    "decision support", "diagnostic systems", "planning systems", "scheduling",
    "symbolic ai", "logic puzzles", "expert consultation", "automated deduction",
    "intelligent agents", "cognitive modeling"
    ]

    python_keywords = [
    # Core Areas
    "data", "machine learning", "ml", "ai", "web", "automation", "script", "visualization",
    "beginner", "deep learning", "analysis", "nlp", "framework", "pandas", "numpy",
    "flask", "django", "prototype",
    
    # Data Science & ML
    "data science", "neural networks", "tensorflow", "pytorch", "scikit-learn",
    "data analysis", "big data", "statistical analysis", "predictive modeling",
    "data visualization", "computer vision", "time series", "reinforcement learning",
    
    # Web Development
    "web development", "fastapi", "rest api", "web scraping", "backend",
    "microservices", "api development", "wsgi", "asgi", "web frameworks",
    "full-stack", "serverless", "web security",
    
    # System & Automation
    "process automation", "task automation", "system administration", "devops",
    "scripting", "cli tools", "system integration", "batch processing",
    "workflow automation", "continuous integration",
    
    # Software Development
    "object-oriented", "functional programming", "testing", "debugging",
    "code quality", "package management", "async programming", "generators",
    "decorators", "context managers", "clean code",
    
    # Applications & Tools
    "gui development", "desktop applications", "database", "sqlite", "postgresql",
    "mongodb", "redis", "cloud computing", "aws", "google cloud", "azure",
    
    # Specialized Areas
    "cybersecurity", "cryptography", "blockchain", "iot", "raspberry pi",
    "image processing", "audio processing", "natural language generation",
    "recommendation systems", "anomaly detection"
    ]

    rust_keywords = [
    # Core Features
    "performance", "system", "safety", "memory", "concurrent", "embedded",
    "high-performance", "os", "real-time", "low-level", "game", "browser",
    "concurrency", "compile-time safety", "efficient", "hardware",
    
    # Systems Programming
    "systems programming", "zero-cost abstractions", "memory safety",
    "thread safety", "ownership model", "borrowing", "lifetimes",
    "unsafe rust", "ffi", "bare metal", "no_std", "embedded systems",
    
    # Performance & Optimization
    "zero-overhead", "cache-friendly", "simd", "vectorization",
    "memory optimization", "performance critical", "benchmarking",
    "profiling", "optimization", "runtime performance",
    
    # Concurrent & Parallel
    "async/await", "parallel processing", "thread pools", "channels",
    "mutex", "atomic operations", "lock-free", "message passing",
    "async runtime", "tokio", "rayon", "crossbeam",
    
    # Web & Network
    "webassembly", "wasm", "networking", "http server", "web frameworks",
    "actix", "rocket", "yew", "protocol implementation", "network programming",
    
    # Development Tools
    "cargo", "package management", "build system", "testing framework",
    "documentation", "error handling", "macro system", "procedural macros",
    "cross compilation", "toolchain management",
    
    # Application Domains
    "game development", "cryptography", "blockchain", "cli applications",
    "device drivers", "operating systems", "compilers", "parsers",
    "graphics programming", "audio processing", "real-time systems",
    
    # Industry Use Cases
    "cloud native", "microservices", "enterprise systems", "distributed systems",
    "infrastructure", "security critical", "financial systems", "automotive",
    "robotics", "industrial automation"
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
