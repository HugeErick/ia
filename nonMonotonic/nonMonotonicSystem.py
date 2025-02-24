# =====================================================
# Common Knowledge Base - Book Information
# =====================================================
bookDatabase = {
    "book1": {"title": "Dune", "author": "Frank Herbert", "genres": ["science fiction", "adventure"]},
    "book2": {"title": "The Shining", "author": "Stephen King", "genres": ["horror", "thriller"]},
    "book3": {"title": "Pride and Prejudice", "author": "Jane Austen", "genres": ["romance", "classic"]},
    "book4": {"title": "Murder on the Orient Express", "author": "Agatha Christie", "genres": ["mystery", "crime"]},
    "book5": {"title": "Neuromancer", "author": "William Gibson", "genres": ["science fiction", "cyberpunk"]},
}

# =====================================================
# APPROACH 1: Score-based Non-monotonic System
# =====================================================
class UserProfile:
    # constructor
    def __init__(self, userId):
        self.userId = userId
        self.readBooks = set()  # Books the user has read
        self.preferences = {
            "likedGenres": set(),
            "dislikedGenres": set(),
            "favoriteAuthors": set(),
        }
        self.exceptions = set()  # Books the user explicitly doesn't want

    def addReadBook(self, bookId):
        """Add a book to read history"""
        self.readBooks.add(bookId)

    def addGenrePreference(self, genre, liked=True):
        """Add genre preference with non-monotonic behavior"""
        if liked:
            self.preferences["likedGenres"].add(genre)
            # Non-monotonic behavior: Remove from disliked if now liked
            if genre in self.preferences["dislikedGenres"]:
                self.preferences["dislikedGenres"].remove(genre)
        else:
            self.preferences["dislikedGenres"].add(genre)
            # Non-monotonic behavior: Remove from liked if now disliked
            if genre in self.preferences["likedGenres"]:
                self.preferences["likedGenres"].remove(genre)

    def addFavoriteAuthor(self, author):
        """Add favorite author"""
        self.preferences["favoriteAuthors"].add(author)

    def addException(self, bookId):
        """Add exception (book user doesn't want to be recommended)"""
        self.exceptions.add(bookId)


class BookRecommender:
    def __init__(self, bookDatabase):
        self.bookDatabase = bookDatabase

    def recommendBooks(self, userProfile, maxRecommendations=3):
        """Generate recommendations based on user profile"""
        # Initial scoring of all books
        scoredBooks = self.scoreAllBooks(userProfile)
        
        # Filter out books the user has already read or explicitly excluded
        filteredBooks = [book for book in scoredBooks 
                        if book["id"] not in userProfile.readBooks 
                        and book["id"] not in userProfile.exceptions]
        
        # Sort by score and return top recommendations
        return sorted(filteredBooks, key=lambda x: x["score"], reverse=True)[:maxRecommendations]

    def scoreAllBooks(self, userProfile):
        """Score all books based on user preferences"""
        scoredBooks = []
        for bookId, book in self.bookDatabase.items():
            score = 0
            
            # Score based on genres
            for genre in book["genres"]:
                if genre in userProfile.preferences["likedGenres"]:
                    score += 2  # Positive score for liked genres
                elif genre in userProfile.preferences["dislikedGenres"]:
                    score -= 3  # Negative score for disliked genres (stronger than like)
            
            # Score based on author
            if book["author"] in userProfile.preferences["favoriteAuthors"]:
                score += 3  # High score for favorite authors
            
            scoredBooks.append({
                "id": bookId,
                "title": book["title"],
                "author": book["author"],
                "score": score
            })
        
        return scoredBooks


def demonstrateScoreSystem():
    """Demonstrate the score-based recommendation system"""
    print("APPROACH 1: Score-based Book Recommendation System Demo")
    
    # Create user and initial preferences
    user = UserProfile("user1")
    user.addGenrePreference("science fiction", True)
    user.addGenrePreference("mystery", True)
    
    # Add read books
    user.addReadBook("book1")  # User has read Dune
    
    # Create recommender
    recommender = BookRecommender(bookDatabase)
    
    # Initial recommendation
    print("\n--- Initial Evidence ---")
    print("User likes: science fiction, mystery")
    print("User has read: Dune")
    
    recommendations = recommender.recommendBooks(user)
    print("\n--- Initial Conclusion (Recommendations) ---")
    for rec in recommendations:
        print(f"{rec['title']} by {rec['author']} (Score: {rec['score']})")
    
    # New evidence - user dislikes science fiction now
    print("\n--- New Evidence ---")
    print("User now dislikes science fiction (preference changed)")
    user.addGenrePreference("science fiction", False)
    
    # User explicitly doesn't want book4
    print("User explicitly doesn't want: Murder on the Orient Express")
    user.addException("book4")
    
    # User adds favorite author
    print("User adds favorite author: Jane Austen")
    user.addFavoriteAuthor("Jane Austen")
    
    # Revised recommendations
    recommendations = recommender.recommendBooks(user)
    print("\n--- Revised Conclusion (Recommendations) ---")
    for rec in recommendations:
        print(f"{rec['title']} by {rec['author']} (Score: {rec['score']})")
    
    # Handle error case - trying to recommend when no matching books
    print("\n--- Error Handling Example ---")
    # Add exceptions for all remaining books
    for bookId in bookDatabase:
        if bookId != "book1":  # Keep only the already read book
            user.addException(bookId)
    
    try:
        errorRecommendations = recommender.recommendBooks(user)
        if not errorRecommendations:
            print("No matching books found based on current preferences and exceptions.")
            print("Fallback: Recommending most popular books regardless of preferences.")
            
            # Reset exceptions for demo purposes
            user.exceptions = set()
            print("\n--- Final Decision After Error Handling ---")
            fallbackRecs = recommender.recommendBooks(user)
            for rec in fallbackRecs:
                print(f"{rec['title']} by {rec['author']} (Popular recommendation)")
    except Exception as error:
        print(f"Error in recommendation system: {error}")


# =====================================================
# APPROACH 2: Rule-based Non-monotonic System
# =====================================================
class BookKnowledgeBase:
    def __init__(self):
        self.books = bookDatabase
        self.facts = set()      # Known facts about user preferences
        self.rules = []         # Recommendation rules
        self.defaults = []      # Default assumptions
        self.exceptions = set()  # Exceptions to rules
    
    def addFact(self, fact):
        """Add a fact about user preferences"""
        self.facts.add(fact)
        print(f"Added fact: {fact}")
    
    def addRule(self, condition, conclusion):
        """Add a rule for recommendations"""
        self.rules.append({"condition": condition, "conclusion": conclusion})
    
    def addDefault(self, prerequisite, assumption, conclusion):
        """Add a default assumption"""
        self.defaults.append({
            "prerequisite": prerequisite, 
            "assumption": assumption, 
            "conclusion": conclusion
        })
    
    def addException(self, exception):
        """Add an exception"""
        self.exceptions.add(exception)
        print(f"Added exception: {exception}")
    
    def satisfiesCondition(self, condition):
        """Check if a condition is satisfied"""
        return condition in self.facts
    
    def applyRules(self):
        """Apply rules to get recommendations"""
        recommendations = set()
        
        # Apply regular rules
        for rule in self.rules:
            if self.satisfiesCondition(rule["condition"]):
                recommendations.add(rule["conclusion"])
        
        # Apply default rules (non-monotonic reasoning)
        for defaultRule in self.defaults:
            prerequisite = defaultRule["prerequisite"]
            assumption = defaultRule["assumption"]
            conclusion = defaultRule["conclusion"]
            
            if (self.satisfiesCondition(prerequisite) and 
                assumption not in self.exceptions):
                recommendations.add(conclusion)
        
        return list(recommendations)
    
    def getBookDetails(self, bookId):
        """Get book details by ID"""
        return self.books[bookId]
    
    def getBooksInGenre(self, genre):
        """Get all book IDs that match a genre"""
        return [bookId for bookId, book in self.books.items() 
                if genre in book["genres"]]
    
    def getBooksByAuthor(self, author):
        """Get all book IDs by an author"""
        return [bookId for bookId, book in self.books.items() 
                if book["author"] == author]


class RuleBasedRecommender:
    def __init__(self, knowledgeBase):
        self.kb = knowledgeBase
        self.readBooks = set()
    
    def addReadBook(self, bookId):
        """Add a book that's been read"""
        self.readBooks.add(bookId)
        print(f"Added read book: {self.kb.getBookDetails(bookId)['title']}")
    
    def getRecommendations(self):
        """Get recommendations"""
        try:
            # Get book IDs from rules
            recommendedBookIds = self.kb.applyRules()
            
            # Filter out books already read
            filteredIds = [id for id in recommendedBookIds if id not in self.readBooks]
            
            # Get full details
            recommendations = [self.kb.getBookDetails(id) for id in filteredIds]
            
            # Handle empty recommendations
            if not recommendations:
                print("Warning: No books match the current criteria")
                return self.getFallbackRecommendations()
            
            return recommendations
        except Exception as error:
            print(f"Error in recommendation process: {error}")
            return self.getFallbackRecommendations()
    
    def getFallbackRecommendations(self):
        """Fallback recommendations if no matches"""
        print("Using fallback recommendation strategy")
        # Simply recommend books not yet read
        allBooks = list(self.kb.books.keys())
        unreadBooks = [id for id in allBooks if id not in self.readBooks]
        return [self.kb.getBookDetails(id) for id in unreadBooks[:3]]


def demonstrateRuleBasedSystem():
    """Demonstrate the rule-based recommendation system"""
    print("\n\nAPPROACH 2: Rule-Based Book Recommendation System Demo")
    
    # Create knowledge base
    kb = BookKnowledgeBase()
    
    # Set up recommender
    recommender = RuleBasedRecommender(kb)
    
    # Add initial facts and rules
    print("\n--- Initial Evidence ---")
    kb.addFact("likes_scifi")
    kb.addFact("likes_mystery")
    
    # Add recommendation rules
    kb.addRule("likes_scifi", "book1")  # Recommend Dune for sci-fi fans
    kb.addRule("likes_scifi", "book5")  # Recommend Neuromancer for sci-fi fans
    kb.addRule("likes_mystery", "book4")  # Recommend Murder on the Orient Express
    
    # Add a default rule (if likes classics, recommend Pride and Prejudice unless exception)
    kb.addDefault("likes_romance", "dislikes_classics", "book3")
    
    # Mark books as read
    recommender.addReadBook("book1")  # User already read Dune
    
    # Get initial recommendations
    print("\n--- Initial Conclusion (Recommendations) ---")
    initialRecs = recommender.getRecommendations()
    for book in initialRecs:
        print(f"{book['title']} by {book['author']} ({', '.join(book['genres'])})")
    
    # New evidence
    print("\n--- New Evidence ---")
    kb.addFact("dislikes_scifi")  # User now dislikes sci-fi (contradicts earlier preference)
    kb.addException("dislikes_classics")  # User actually likes classics despite general rule
    kb.addFact("likes_romance")  # User likes romance
    
    # Add exception for specific book
    kb.addException("recommend_book4")  # Don't recommend book4 despite liking mystery
    
    # Get revised recommendations
    print("\n--- Revised Conclusion (Recommendations) ---")
    revisedRecs = recommender.getRecommendations()
    for book in revisedRecs:
        print(f"{book['title']} by {book['author']} ({', '.join(book['genres'])})")
    
    # Demonstrate error handling
    print("\n--- Error Handling Example ---")
    # Add all books as read to force empty recommendations
    for bookId in kb.books:
        if bookId not in recommender.readBooks:
            recommender.addReadBook(bookId)
    
    # Try to get recommendations when all books are read
    print("\n--- Final Decision After Error Handling ---")
    finalRecs = recommender.getRecommendations()
    if finalRecs:
        for book in finalRecs:
            print(f"{book['title']} by {book['author']} (Fallback recommendation)")
    else:
        print("No recommendations available")


# Main function to run both demonstrations
def runNonMonotonics():
    print("BOOK RECOMMENDATION SYSTEM - NON-MONOTONIC REASONING")
    print("=" * 50)
    
    # Run the first approach demonstration
    demonstrateScoreSystem()
    
    # Run the second approach demonstration
    demonstrateRuleBasedSystem()

# IF RUNNING IN GOOGLE COLLAB PLS UNCOMMENT THE FOLLOWING
#runNonMonotonics()
