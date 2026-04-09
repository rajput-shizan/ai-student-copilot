"""
MODE 1: AI Assistant - Provides definitions, explanations, and study tips
"""

# Sample knowledge base for keyword-based responses
KNOWLEDGE_BASE = {
    "machine learning": "Machine Learning is an AI technique that enables systems to learn from data and improve performance over time without being explicitly programmed.",
    "artificial intelligence": "Artificial Intelligence (AI) is the simulation of human intelligence processes by computer systems, including learning, reasoning, and self-correction.",
    "deep learning": "Deep Learning is a subset of machine learning that uses neural networks with multiple layers to process and learn from large amounts of data.",
    "python": "Python is a high-level, interpreted programming language known for its simplicity and readability, widely used in data science and web development.",
    "database": "A database is an organized collection of structured data stored and accessed electronically, managed by a Database Management System (DBMS).",
}

STUDY_TIPS = [
    "Break down complex topics into smaller, manageable chunks.",
    "Use active recall - test yourself without looking at notes.",
    "Practice problems regularly to reinforce concepts.",
    "Create mind maps to visualize relationships between topics.",
    "Teach the concept to someone else to identify gaps in understanding.",
]

def get_ai_response(user_query):
    """Generate response based on user query using keyword matching"""
    user_query_lower = user_query.lower()
    
    for key, value in KNOWLEDGE_BASE.items():
        if key in user_query_lower:
            return f"📚 **Definition**: {value}\n\n💡 **Study Tip**: {STUDY_TIPS[hash(key) % len(STUDY_TIPS)]}"
    
    return (
        "I'm not sure about that topic yet. Try asking me about:\n"
        "- Machine Learning\n"
        "- Artificial Intelligence\n"
        "- Deep Learning\n"
        "- Python\n"
        "- Databases\n\n"
        "Or rephrase your question for better results!"
    )

def add_to_knowledge_base(topic, definition):
    """Dynamically add new topics to the knowledge base"""
    KNOWLEDGE_BASE[topic.lower()] = definition
