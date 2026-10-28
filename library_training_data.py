"""
LIBRARY AI CHATBOT — COMPLETE FRAME KNOWLEDGE BASE & TRAINING DATA
Based on the official 26-page Complete Frame Knowledge Base document.

Use this file to:
1. Inspect the complete 80-book simulated catalogue.
2. Update Cell 2 and Cell 3 in `chatbot_training.ipynb` in Google Colab.
3. Run the Flask server locally or via Colab ngrok.
"""

# =====================================================================
# FRAME 1: BOOK_INFORMATION (All 80 Books, 8 Shelves, 5 Copies Each)
# =====================================================================

BOOKS_DATA = [
    # ── SHELF 1: FICTION ─────────────────────────────────────────────
    # Row 1
    {
        "id": "B01",
        "title": "Harry Potter",
        "author": "Rowling",
        "category": "Fiction",
        "shelf": 1,
        "row": 1,
        "copies": 5,
        "keywords": "Harry Potter, Rowling, fiction"
    },
    {
        "id": "B02",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "Fiction",
        "shelf": 1,
        "row": 1,
        "copies": 5,
        "keywords": "The Hobbit, Tolkien, fantasy, adventure, fiction"
    },
    {
        "id": "B03",
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "category": "Fiction",
        "shelf": 1,
        "row": 1,
        "copies": 5,
        "keywords": "The Little Prince, Saint-Exupéry, fantasy, adventure, fiction"
    },
    {
        "id": "B04",
        "title": "Alice's Adventures in Wonderland",
        "author": "Lewis Carroll",
        "category": "Fiction",
        "shelf": 1,
        "row": 1,
        "copies": 5,
        "keywords": "Alice's Adventures in Wonderland, Lewis Carroll, fantasy, fiction"
    },
    {
        "id": "B05",
        "title": "The Chronicles of Narnia",
        "author": "C.S. Lewis",
        "category": "Fiction",
        "shelf": 1,
        "row": 1,
        "copies": 5,
        "keywords": "The Chronicles of Narnia, C.S. Lewis, fantasy, adventure, fiction"
    },
    # Row 2
    {
        "id": "B06",
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "category": "Fiction",
        "shelf": 1,
        "row": 2,
        "copies": 5,
        "keywords": "The Hunger Games, Suzanne Collins, dystopian, adventure, fiction"
    },
    {
        "id": "B07",
        "title": "The Maze Runner",
        "author": "James Dashner",
        "category": "Fiction",
        "shelf": 1,
        "row": 2,
        "copies": 5,
        "keywords": "The Maze Runner, James Dashner, mystery, adventure, fiction"
    },
    {
        "id": "B08",
        "title": "Wonder",
        "author": "R.J. Palacio",
        "category": "Fiction",
        "shelf": 1,
        "row": 2,
        "copies": 5,
        "keywords": "Wonder, R.J. Palacio, friendship, family, fiction"
    },
    {
        "id": "B09",
        "title": "The Giver",
        "author": "Lois Lowry",
        "category": "Fiction",
        "shelf": 1,
        "row": 2,
        "copies": 5,
        "keywords": "The Giver, Lois Lowry, dystopian, society, fiction"
    },
    {
        "id": "B10",
        "title": "Charlie and the Chocolate Factory",
        "author": "Roald Dahl",
        "category": "Fiction",
        "shelf": 1,
        "row": 2,
        "copies": 5,
        "keywords": "Charlie and the Chocolate Factory, Roald Dahl, chocolate, fantasy, fiction"
    },

    # ── SHELF 2: COMICS ──────────────────────────────────────────────
    # Row 1
    {
        "id": "B11",
        "title": "Spider-Man: Blue",
        "author": "Jeph Loeb",
        "category": "Comics",
        "shelf": 2,
        "row": 1,
        "copies": 5,
        "keywords": "Spider-Man, Jeph Loeb, superhero, Marvel, comics"
    },
    {
        "id": "B12",
        "title": "Batman: Year One",
        "author": "Frank Miller",
        "category": "Comics",
        "shelf": 2,
        "row": 1,
        "copies": 5,
        "keywords": "Batman, Frank Miller, superhero, DC Comics, comics"
    },
    {
        "id": "B13",
        "title": "Superman: Red Son",
        "author": "Mark Millar",
        "category": "Comics",
        "shelf": 2,
        "row": 1,
        "copies": 5,
        "keywords": "Superman, Mark Millar, superhero, DC Comics, comics"
    },
    {
        "id": "B14",
        "title": "One Piece, Volume 1",
        "author": "Eiichiro Oda",
        "category": "Comics",
        "shelf": 2,
        "row": 1,
        "copies": 5,
        "keywords": "One Piece, Eiichiro Oda, manga, adventure, comics"
    },
    {
        "id": "B15",
        "title": "Naruto, Volume 1",
        "author": "Masashi Kishimoto",
        "category": "Comics",
        "shelf": 2,
        "row": 1,
        "copies": 5,
        "keywords": "Naruto, Masashi Kishimoto, manga, ninja, adventure, comics"
    },
    # Row 2
    {
        "id": "B16",
        "title": "Dragon Ball, Volume 1",
        "author": "Akira Toriyama",
        "category": "Comics",
        "shelf": 2,
        "row": 2,
        "copies": 5,
        "keywords": "Dragon Ball, Akira Toriyama, manga, martial arts, adventure, comics"
    },
    {
        "id": "B17",
        "title": "Detective Conan, Volume 1",
        "author": "Gosho Aoyama",
        "category": "Comics",
        "shelf": 2,
        "row": 2,
        "copies": 5,
        "keywords": "Detective Conan, Gosho Aoyama, manga, mystery, detective, comics"
    },
    {
        "id": "B18",
        "title": "Doraemon, Volume 1",
        "author": "Fujiko F. Fujio",
        "category": "Comics",
        "shelf": 2,
        "row": 2,
        "copies": 5,
        "keywords": "Doraemon, Fujiko F. Fujio, manga, science fiction, comedy, comics"
    },
    {
        "id": "B19",
        "title": "My Hero Academia, Volume 1",
        "author": "Kohei Horikoshi",
        "category": "Comics",
        "shelf": 2,
        "row": 2,
        "copies": 5,
        "keywords": "My Hero Academia, Kohei Horikoshi, manga, superheroes, action, comics"
    },
    {
        "id": "B20",
        "title": "Attack on Titan, Volume 1",
        "author": "Hajime Isayama",
        "category": "Comics",
        "shelf": 2,
        "row": 2,
        "copies": 5,
        "keywords": "Attack on Titan, Hajime Isayama, manga, action, fantasy, comics"
    },

    # ── SHELF 3: ENCYCLOPEDIAS ───────────────────────────────────────
    # Row 1
    {
        "id": "B21",
        "title": "The World Book Encyclopedia",
        "author": "World Book, Inc.",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 1,
        "copies": 5,
        "keywords": "World Book Encyclopedia, world knowledge, history, science, reference"
    },
    {
        "id": "B22",
        "title": "Encyclopaedia Britannica",
        "author": "Encyclopaedia Britannica, Inc.",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 1,
        "copies": 5,
        "keywords": "Encyclopaedia Britannica, general knowledge, history, science, reference"
    },
    {
        "id": "B23",
        "title": "The New Children's Encyclopedia",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 1,
        "copies": 5,
        "keywords": "children's encyclopedia, DK, facts, science, geography, reference"
    },
    {
        "id": "B24",
        "title": "The Science Encyclopedia",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 1,
        "copies": 5,
        "keywords": "science encyclopedia, DK, physics, chemistry, biology, reference"
    },
    {
        "id": "B25",
        "title": "The Kingfisher Science Encyclopedia",
        "author": "Kingfisher",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 1,
        "copies": 5,
        "keywords": "Kingfisher, science, technology, nature, reference"
    },
    # Row 2
    {
        "id": "B26",
        "title": "The Encyclopedia of Animals",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 2,
        "copies": 5,
        "keywords": "animals, wildlife, mammals, birds, nature, reference"
    },
    {
        "id": "B27",
        "title": "The Encyclopedia of Space",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 2,
        "copies": 5,
        "keywords": "space, planets, astronomy, universe, reference"
    },
    {
        "id": "B28",
        "title": "The Encyclopedia of History",
        "author": "Philip Wilkinson",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 2,
        "copies": 5,
        "keywords": "history, ancient civilizations, historical events, world history, reference"
    },
    {
        "id": "B29",
        "title": "The Encyclopedia of Geography",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 2,
        "copies": 5,
        "keywords": "geography, countries, maps, Earth, environment, reference"
    },
    {
        "id": "B30",
        "title": "The Encyclopedia of Technology",
        "author": "DK",
        "category": "Encyclopedias",
        "shelf": 3,
        "row": 2,
        "copies": 5,
        "keywords": "technology, inventions, computers, engineering, innovation, reference"
    },

    # ── SHELF 4: ECONOMICS ───────────────────────────────────────────
    # Row 1
    {
        "id": "B31",
        "title": "Economics",
        "author": "Paul A. Samuelson and William D. Nordhaus",
        "category": "Economics",
        "shelf": 4,
        "row": 1,
        "copies": 5,
        "keywords": "economics, Samuelson, Nordhaus, economic theory, microeconomics, macroeconomics"
    },
    {
        "id": "B32",
        "title": "Principles of Economics",
        "author": "N. Gregory Mankiw",
        "category": "Economics",
        "shelf": 4,
        "row": 1,
        "copies": 5,
        "keywords": "principles of economics, Mankiw, supply, demand, markets, economics"
    },
    {
        "id": "B33",
        "title": "Freakonomics",
        "author": "Steven D. Levitt and Stephen J. Dubner",
        "category": "Economics",
        "shelf": 4,
        "row": 1,
        "copies": 5,
        "keywords": "Freakonomics, Levitt, Dubner, behavioral economics, incentives, decision making"
    },
    {
        "id": "B34",
        "title": "The Wealth of Nations",
        "author": "Adam Smith",
        "category": "Economics",
        "shelf": 4,
        "row": 1,
        "copies": 5,
        "keywords": "The Wealth of Nations, Adam Smith, classical economics, markets, trade"
    },
    {
        "id": "B35",
        "title": "Capital in the Twenty-First Century",
        "author": "Thomas Piketty",
        "category": "Economics",
        "shelf": 4,
        "row": 1,
        "copies": 5,
        "keywords": "Capital in the Twenty-First Century, Thomas Piketty, income inequality, wealth, economic growth"
    },
    # Row 2
    {
        "id": "B36",
        "title": "The Undercover Economist",
        "author": "Tim Harford",
        "category": "Economics",
        "shelf": 4,
        "row": 2,
        "copies": 5,
        "keywords": "The Undercover Economist, Tim Harford, everyday economics, markets, prices"
    },
    {
        "id": "B37",
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "category": "Economics",
        "shelf": 4,
        "row": 2,
        "copies": 5,
        "keywords": "Thinking, Fast and Slow, Daniel Kahneman, behavioral economics, psychology, decision making"
    },
    {
        "id": "B38",
        "title": "The Big Short",
        "author": "Michael Lewis",
        "category": "Economics",
        "shelf": 4,
        "row": 2,
        "copies": 5,
        "keywords": "The Big Short, Michael Lewis, financial crisis, banking, investment"
    },
    {
        "id": "B39",
        "title": "Poor Economics",
        "author": "Abhijit V. Banerjee and Esther Duflo",
        "category": "Economics",
        "shelf": 4,
        "row": 2,
        "copies": 5,
        "keywords": "Poor Economics, Banerjee, Duflo, poverty, development economics, policy"
    },
    {
        "id": "B40",
        "title": "The Economics Book",
        "author": "DK",
        "category": "Economics",
        "shelf": 4,
        "row": 2,
        "copies": 5,
        "keywords": "The Economics Book, DK, economic ideas, financial systems, economic history"
    },

    # ── SHELF 5: SCIENCE ─────────────────────────────────────────────
    # Row 1
    {
        "id": "B41",
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "category": "Science",
        "shelf": 5,
        "row": 1,
        "copies": 5,
        "keywords": "A Brief History of Time, Stephen Hawking, universe, cosmology, physics, science"
    },
    {
        "id": "B42",
        "title": "The Selfish Gene",
        "author": "Richard Dawkins",
        "category": "Science",
        "shelf": 5,
        "row": 1,
        "copies": 5,
        "keywords": "The Selfish Gene, Richard Dawkins, evolution, genetics, biology, science"
    },
    {
        "id": "B43",
        "title": "Cosmos",
        "author": "Carl Sagan",
        "category": "Science",
        "shelf": 5,
        "row": 1,
        "copies": 5,
        "keywords": "Cosmos, Carl Sagan, astronomy, planets, universe, science"
    },
    {
        "id": "B44",
        "title": "On the Origin of Species",
        "author": "Charles Darwin",
        "category": "Science",
        "shelf": 5,
        "row": 1,
        "copies": 5,
        "keywords": "On the Origin of Species, Charles Darwin, evolution, natural selection, biology"
    },
    {
        "id": "B45",
        "title": "The Elegant Universe",
        "author": "Brian Greene",
        "category": "Science",
        "shelf": 5,
        "row": 1,
        "copies": 5,
        "keywords": "The Elegant Universe, Brian Greene, physics, string theory, universe, science"
    },
    # Row 2
    {
        "id": "B46",
        "title": "Astrophysics for People in a Hurry",
        "author": "Neil deGrasse Tyson",
        "category": "Science",
        "shelf": 5,
        "row": 2,
        "copies": 5,
        "keywords": "Astrophysics for People in a Hurry, Neil deGrasse Tyson, stars, galaxies, space, science"
    },
    {
        "id": "B47",
        "title": "The Gene: An Intimate History",
        "author": "Siddhartha Mukherjee",
        "category": "Science",
        "shelf": 5,
        "row": 2,
        "copies": 5,
        "keywords": "The Gene, Siddhartha Mukherjee, genetics, DNA, heredity, biology"
    },
    {
        "id": "B48",
        "title": "Silent Spring",
        "author": "Rachel Carson",
        "category": "Science",
        "shelf": 5,
        "row": 2,
        "copies": 5,
        "keywords": "Silent Spring, Rachel Carson, environment, ecology, pesticides, nature"
    },
    {
        "id": "B49",
        "title": "The Body: A Guide for Occupants",
        "author": "Bill Bryson",
        "category": "Science",
        "shelf": 5,
        "row": 2,
        "copies": 5,
        "keywords": "The Body, Bill Bryson, human body, anatomy, biology, health science"
    },
    {
        "id": "B50",
        "title": "Six Easy Pieces",
        "author": "Richard P. Feynman",
        "category": "Science",
        "shelf": 5,
        "row": 2,
        "copies": 5,
        "keywords": "Six Easy Pieces, Richard Feynman, physics, energy, matter, scientific principles"
    },

    # ── SHELF 6: LITERATURE ──────────────────────────────────────────
    # Row 1
    {
        "id": "B51",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "category": "Literature",
        "shelf": 6,
        "row": 1,
        "copies": 5,
        "keywords": "Pride and Prejudice, Jane Austen, classic literature, romance, society"
    },
    {
        "id": "B52",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Literature",
        "shelf": 6,
        "row": 1,
        "copies": 5,
        "keywords": "To Kill a Mockingbird, Harper Lee, justice, racism, classic literature"
    },
    {
        "id": "B53",
        "title": "1984",
        "author": "George Orwell",
        "category": "Literature",
        "shelf": 6,
        "row": 1,
        "copies": 5,
        "keywords": "1984, George Orwell, dystopian, political fiction, society"
    },
    {
        "id": "B54",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Literature",
        "shelf": 6,
        "row": 1,
        "copies": 5,
        "keywords": "The Great Gatsby, F. Scott Fitzgerald, American literature, wealth, society"
    },
    {
        "id": "B55",
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "category": "Literature",
        "shelf": 6,
        "row": 1,
        "copies": 5,
        "keywords": "Jane Eyre, Charlotte Brontë, classic literature, romance, independence"
    },
    # Row 2
    {
        "id": "B56",
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "category": "Literature",
        "shelf": 6,
        "row": 2,
        "copies": 5,
        "keywords": "Wuthering Heights, Emily Brontë, classic literature, romance, tragedy"
    },
    {
        "id": "B57",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "category": "Literature",
        "shelf": 6,
        "row": 2,
        "copies": 5,
        "keywords": "The Catcher in the Rye, J.D. Salinger, coming of age, society, classic literature"
    },
    {
        "id": "B58",
        "title": "Animal Farm",
        "author": "George Orwell",
        "category": "Literature",
        "shelf": 6,
        "row": 2,
        "copies": 5,
        "keywords": "Animal Farm, George Orwell, political satire, revolution, classic literature"
    },
    {
        "id": "B59",
        "title": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "category": "Literature",
        "shelf": 6,
        "row": 2,
        "copies": 5,
        "keywords": "The Old Man and the Sea, Ernest Hemingway, courage, struggle, classic literature"
    },
    {
        "id": "B60",
        "title": "Les Misérables",
        "author": "Victor Hugo",
        "category": "Literature",
        "shelf": 6,
        "row": 2,
        "copies": 5,
        "keywords": "Les Misérables, Victor Hugo, French literature, justice, redemption"
    },

    # ── SHELF 7: PHILOSOPHY ──────────────────────────────────────────
    # Row 1
    {
        "id": "B61",
        "title": "The Republic",
        "author": "Plato",
        "category": "Philosophy",
        "shelf": 7,
        "row": 1,
        "copies": 5,
        "keywords": "The Republic, Plato, justice, political philosophy, ideal society"
    },
    {
        "id": "B62",
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "category": "Philosophy",
        "shelf": 7,
        "row": 1,
        "copies": 5,
        "keywords": "Meditations, Marcus Aurelius, Stoicism, self-discipline, wisdom"
    },
    {
        "id": "B63",
        "title": "The Art of War",
        "author": "Sun Tzu",
        "category": "Philosophy",
        "shelf": 7,
        "row": 1,
        "copies": 5,
        "keywords": "The Art of War, Sun Tzu, strategy, leadership, military philosophy"
    },
    {
        "id": "B64",
        "title": "Beyond Good and Evil",
        "author": "Friedrich Nietzsche",
        "category": "Philosophy",
        "shelf": 7,
        "row": 1,
        "copies": 5,
        "keywords": "Beyond Good and Evil, Friedrich Nietzsche, morality, ethics, philosophical thought"
    },
    {
        "id": "B65",
        "title": "Critique of Pure Reason",
        "author": "Immanuel Kant",
        "category": "Philosophy",
        "shelf": 7,
        "row": 1,
        "copies": 5,
        "keywords": "Critique of Pure Reason, Immanuel Kant, knowledge, reason, epistemology"
    },
    # Row 2
    {
        "id": "B66",
        "title": "Nicomachean Ethics",
        "author": "Aristotle",
        "category": "Philosophy",
        "shelf": 7,
        "row": 2,
        "copies": 5,
        "keywords": "Nicomachean Ethics, Aristotle, ethics, virtue, happiness"
    },
    {
        "id": "B67",
        "title": "Tao Te Ching",
        "author": "Lao Tzu",
        "category": "Philosophy",
        "shelf": 7,
        "row": 2,
        "copies": 5,
        "keywords": "Tao Te Ching, Lao Tzu, Taoism, harmony, wisdom"
    },
    {
        "id": "B68",
        "title": "The Social Contract",
        "author": "Jean-Jacques Rousseau",
        "category": "Philosophy",
        "shelf": 7,
        "row": 2,
        "copies": 5,
        "keywords": "The Social Contract, Rousseau, political philosophy, freedom, government"
    },
    {
        "id": "B69",
        "title": "An Enquiry Concerning Human Understanding",
        "author": "David Hume",
        "category": "Philosophy",
        "shelf": 7,
        "row": 2,
        "copies": 5,
        "keywords": "An Enquiry Concerning Human Understanding, David Hume, empiricism, knowledge, reason"
    },
    {
        "id": "B70",
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "category": "Philosophy",
        "shelf": 7,
        "row": 2,
        "copies": 5,
        "keywords": "Man's Search for Meaning, Viktor Frankl, meaning of life, purpose, human existence"
    },

    # ── SHELF 8: ARTIFICIAL INTELLIGENCE ─────────────────────────────
    # Row 1
    {
        "id": "B71",
        "title": "Artificial Intelligence: A Modern Approach",
        "author": "Stuart Russell and Peter Norvig",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 1,
        "copies": 5,
        "keywords": "Artificial Intelligence, Russell, Norvig, machine learning, intelligent agents"
    },
    {
        "id": "B72",
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio, and Aaron Courville",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 1,
        "copies": 5,
        "keywords": "Deep Learning, neural networks, machine learning, Goodfellow, AI"
    },
    {
        "id": "B73",
        "title": "Machine Learning",
        "author": "Tom M. Mitchell",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 1,
        "copies": 5,
        "keywords": "Machine Learning, Tom Mitchell, algorithms, prediction, AI"
    },
    {
        "id": "B74",
        "title": "Life 3.0",
        "author": "Max Tegmark",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 1,
        "copies": 5,
        "keywords": "Life 3.0, Max Tegmark, future of AI, intelligent machines, technology"
    },
    {
        "id": "B75",
        "title": "Human Compatible",
        "author": "Stuart Russell",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 1,
        "copies": 5,
        "keywords": "Human Compatible, Stuart Russell, AI safety, human values, intelligent systems"
    },
    # Row 2
    {
        "id": "B76",
        "title": "Superintelligence",
        "author": "Nick Bostrom",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 2,
        "copies": 5,
        "keywords": "Superintelligence, Nick Bostrom, advanced AI, AI safety, future technology"
    },
    {
        "id": "B77",
        "title": "The Alignment Problem",
        "author": "Brian Christian",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 2,
        "copies": 5,
        "keywords": "The Alignment Problem, Brian Christian, machine learning, AI ethics, alignment"
    },
    {
        "id": "B78",
        "title": "Prediction Machines",
        "author": "Ajay Agrawal, Joshua Gans, and Avi Goldfarb",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 2,
        "copies": 5,
        "keywords": "Prediction Machines, AI economics, machine learning, business, automation"
    },
    {
        "id": "B79",
        "title": "AI Superpowers",
        "author": "Kai-Fu Lee",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 2,
        "copies": 5,
        "keywords": "AI Superpowers, Kai-Fu Lee, China, United States, AI industry"
    },
    {
        "id": "B80",
        "title": "Co-Intelligence",
        "author": "Ethan Mollick",
        "category": "Artificial Intelligence",
        "shelf": 8,
        "row": 2,
        "copies": 5,
        "keywords": "Co-Intelligence, Ethan Mollick, generative AI, AI tools, human collaboration"
    }
]

# Category Location Mapping (FRAME 2)
CATEGORY_MAP = {
    "Fiction": {"shelf": 1, "total_books": 10},
    "Comics": {"shelf": 2, "total_books": 10},
    "Encyclopedias": {"shelf": 3, "total_books": 10},
    "Economics": {"shelf": 4, "total_books": 10},
    "Science": {"shelf": 5, "total_books": 10},
    "Literature": {"shelf": 6, "total_books": 10},
    "Philosophy": {"shelf": 7, "total_books": 10},
    "Artificial Intelligence": {"shelf": 8, "total_books": 10}
}

# =====================================================================
# FRAME 9: DISCUSSION & STUDY ROOMS (6 Rooms)
# =====================================================================
ROOMS_DATA = [
    {
        "id": "R01",
        "name": "Discussion Room Alpha",
        "type": "Discussion Room",
        "capacity": "4-6 pax",
        "floor": "Level 2 (East Wing)",
        "equipment": "55-inch 4K Smart TV, Glass Whiteboard, Conference Speakerphone, Wireless Presentation",
        "suitable_for": "Group presentations, team discussions, group assignments"
    },
    {
        "id": "R02",
        "name": "Discussion Room Beta",
        "type": "Discussion Room",
        "capacity": "4-6 pax",
        "floor": "Level 2 (East Wing)",
        "equipment": "Ultra-wide Monitor, Glass Whiteboard, International Power Hubs, USB-C Docking",
        "suitable_for": "Group coding, data projects, peer tutoring"
    },
    {
        "id": "R03",
        "name": "Collaborative Studio Hub",
        "type": "Conference Room",
        "capacity": "6-8 pax",
        "floor": "Level 2 (North Wing)",
        "equipment": "Dual 4K Displays, PTZ Conference Camera, Ceiling Omnidirectional Mic Array, Mobile Whiteboards",
        "suitable_for": "Large group collaboration, student committee meetings, workshops"
    },
    {
        "id": "R04",
        "name": "Silent Focus Pod 1",
        "type": "Silent Pod",
        "capacity": "1-2 pax",
        "floor": "Level 3 (Quiet Study Commons)",
        "equipment": "Herman Miller Ergonomic Chair, Acoustic Soundproof Paneling, LED Task Light, Fast Qi Charger",
        "suitable_for": "Deep research, dissertation writing, thesis prep"
    },
    {
        "id": "R05",
        "name": "Silent Focus Pod 2",
        "type": "Silent Pod",
        "capacity": "1-2 pax",
        "floor": "Level 3 (Quiet Study Commons)",
        "equipment": "Motorized Standing Desk, Dual Monitor Arms with 27-inch Displays, ANC Headphones",
        "suitable_for": "Individual intensive revision, exam preparation"
    },
    {
        "id": "R06",
        "name": "Digital Media & Podcast Lab",
        "type": "Media Lab",
        "capacity": "2-4 pax",
        "floor": "Level 1 (Creative Commons)",
        "equipment": "Shure SM7B Microphones, Rodecaster Pro II Audio Console, Studio Lighting, 4K Video Editing Rig",
        "suitable_for": "Podcast recording, presentation video editing, multimedia assignments"
    }
]

# =====================================================================
# FRAME 10: LIBRARY OPERATING HOURS
# =====================================================================
LIBRARY_HOURS = {
    "weekdays": "Monday – Friday: 08:30 AM – 09:00 PM",
    "saturday": "Saturday: 09:00 AM – 05:00 PM",
    "sunday": "Sunday & Public Holidays: 10:00 AM – 04:00 PM",
    "silent_commons": "Level 3 Silent Commons: 24/7 access during semester weeks",
    "exam_period": "Final Exam Period: Extended hours until 11:00 PM (Levels 1-2) / 24 Hours (Level 3)",
    "counter_services": "Circulation, Reference, Fine Payment & Room Keys counter closes 30 minutes before library closing."
}

# =====================================================================
# FRAME 11: OVERDUE FINES & POLICIES
# =====================================================================
OVERDUE_FINES = {
    "general_rate": "RM 0.50 per day per book (for general collection books B01-B80)",
    "reserve_rate": "RM 1.00 per hour per book (for Red Spot / High-Demand 2-hour loans)",
    "grace_period": "1 calendar day grace period before fines begin accumulating",
    "maximum_cap": "RM 25.00 maximum fine per book",
    "lost_book_charge": "Replacement cost of the book + RM 20.00 administrative fee",
    "payment_channels": "Student Portal e-Payment, Library Service Counter, Touch 'n Go eWallet, Credit/Debit card",
    "privilege_suspension": "Borrowing and room booking privileges are automatically suspended if unpaid fines exceed RM 10.00."
}


def build_training_pairs():
    """Generates comprehensive Q&A training pairs for TF-IDF / Colab training."""
    pairs = []

    # Greetings
    pairs.extend([
        ("hello", "Hello! Welcome to the Library AI Chatbot. I can assist you with searching our catalogue, finding book locations, browsing categories, checking availability, and simulating borrowing or returns. How may I help you today?"),
        ("hi", "Hi there! I am your Library AI Assistant. How can I help you navigate our simulated catalogue today?"),
        ("good morning", "Good morning! Welcome to the library. Looking for a book, shelf location, or library policy?"),
        ("help", "I can help you with:\n1. 🔍 Search books by title, author, keyword, or Book ID\n2. 📚 Browse categories across Shelves 1-8\n3. 📍 Find exact shelf and row locations\n4. 📖 Simulate borrowing books (up to 5 books)\n5. 🔄 Simulate book returns\n6. 📜 View your borrowing history\n7. 📋 Library policy rules"),
        ("who are you", "I am the Library AI Chatbot for our simulated library assignment. I provide accurate catalogue information from our 80-book collection across 8 categories."),
    ])

    # Chinese Greetings & Help
    pairs.extend([
        ("你好", "您好！欢迎使用图书馆 AI 助手。我可以帮您检索图书、查询书架位置、浏览类别、借书、还书以及查询借阅历史。请问今天有什么可以帮您？"),
        ("帮助", "我可以为您提供以下服务：\n1. 🔍 检索图书（书名、作者、编号、关键词）\n2. 📚 浏览各分类图书（书架 1 至 8）\n3. 📍 查询精确书架与排号（Row / Shelf）\n4. 📖 模拟借阅图书（每位学生最多 5 本，借期 1 个自然月）\n5. 🔄 模拟归还图书\n6. 📜 查询个人借书记录\n7. 📋 图书馆借阅规则"),
        ("借书规则", "图书馆借阅政策（Frame 8）：\n- 最多借阅数量：每名学生最多同时借阅 5 本书。\n- 借阅期限：自借出之日起 1 个自然月（遇月末无对应日期自动调整为当月最后一天）。\n- 状态更新：归还日期在确认还书前保持为空。若逾期未还，将标记为 Overdue。\n- 本馆为模拟数据，共 80 本图书，不支持未收录图书的借阅。"),
    ])

    # Category overview
    cat_summary = (
        "Our library has 8 categories located across Shelves 1 to 8:\n"
        "• Fiction — Shelf 1 (B01-B10)\n"
        "• Comics — Shelf 2 (B11-B20)\n"
        "• Encyclopedias — Shelf 3 (B21-B30)\n"
        "• Economics — Shelf 4 (B31-B40)\n"
        "• Science — Shelf 5 (B41-B50)\n"
        "• Literature — Shelf 6 (B51-B60)\n"
        "• Philosophy — Shelf 7 (B61-B70)\n"
        "• Artificial Intelligence — Shelf 8 (B71-B80)\n\n"
        "Which category would you like to explore?"
    )
    pairs.extend([
        ("categories", cat_summary),
        ("browse categories", cat_summary),
        ("what categories do you have", cat_summary),
        ("show me shelves", cat_summary),
        ("list categories", cat_summary),
        ("分类", "图书馆藏书共分为 8 个大类，分别位于 1 至 8 号书架：\n"
               "• 小说 (Fiction) — 1号书架\n"
               "• 漫画 (Comics) — 2号书架\n"
               "• 百科全书 (Encyclopedias) — 3号书架\n"
               "• 经济学 (Economics) — 4号书架\n"
               "• 科学 (Science) — 5号书架\n"
               "• 文学 (Literature) — 6号书架\n"
               "• 哲学 (Philosophy) — 7号书架\n"
               "• 人工智能 (Artificial Intelligence) — 8号书架\n\n您想浏览哪个类别？"),
    ])

    # Category-specific book listings
    for cat, info in CATEGORY_MAP.items():
        cat_books = [b for b in BOOKS_DATA if b["category"] == cat]
        row1_titles = [f"{b['id']}: {b['title']}" for b in cat_books if b["row"] == 1]
        row2_titles = [f"{b['id']}: {b['title']}" for b in cat_books if b["row"] == 2]
        
        reply = (
            f"📚 Category: {cat} (Shelf {info['shelf']})\n\n"
            f"Row 1:\n" + "\n".join(f"• {t}" for t in row1_titles) + "\n\n"
            f"Row 2:\n" + "\n".join(f"• {t}" for t in row2_titles) + "\n\n"
            f"Total available copies: 5 per title. Would you like details on any of these books?"
        )
        pairs.append((f"{cat.lower()} books", reply))
        pairs.append((f"browse {cat.lower()}", reply))
        pairs.append((f"show {cat.lower()}", reply))
        pairs.append((f"shelf {info['shelf']}", reply))
        pairs.append((f"what is on shelf {info['shelf']}", reply))

    # Individual book details and locations (Frame 1, 3, 4)
    for b in BOOKS_DATA:
        detail_reply = (
            f"📖 Book ID: {b['id']}\n"
            f"Title: {b['title']}\n"
            f"Author: {b['author']}\n"
            f"Category: {b['category']}\n"
            f"Location: Shelf {b['shelf']}, Row {b['row']}\n"
            f"Total Copies: {b['copies']} | Available Copies: {b['copies']}\n"
            f"Keywords: {b['keywords']}"
        )
        location_reply = f"📍 Location for '{b['title']}' ({b['id']}): Shelf {b['shelf']}, Row {b['row']}."

        pairs.append((b["id"].lower(), detail_reply))
        pairs.append((f"find {b['id'].lower()}", detail_reply))
        pairs.append((f"search {b['title'].lower()}", detail_reply))
        pairs.append((b["title"].lower(), detail_reply))
        pairs.append((f"where is {b['title'].lower()}", location_reply))
        pairs.append((f"location of {b['title'].lower()}", location_reply))
        pairs.append((f"where is {b['id'].lower()}", location_reply))
        pairs.append((f"books by {b['author'].lower()}", f"Books by {b['author']}:\n• {b['id']}: {b['title']} (Shelf {b['shelf']}, Row {b['row']})"))

    # Library Policies (Frame 8)
    policy_reply = (
        "📋 APU Library Policy Settings (Frame 8):\n"
        "• Maximum borrowing limit: 5 books per student at one time.\n"
        "• Borrowing period: Exactly one calendar month from the actual borrowing date.\n"
        "• Due date: One calendar month after Borrow_Date (adjusted to the last day of the following month if necessary, e.g. Jan 31 -> Feb 28/29).\n"
        "• Availability: A book can be borrowed only if Available_Copies > 0.\n"
        "• Return date: Recorded only when the return is actually confirmed.\n"
        "• Inventory & History: All catalogue records are simulated assignment data."
    )
    pairs.extend([
        ("library rules", policy_reply),
        ("library policies", policy_reply),
        ("policy", policy_reply),
        ("how many books can i borrow", "You can borrow a maximum of 5 books per student at one time."),
        ("how long can i borrow", "The borrowing period is one calendar month from the actual borrowing date."),
        ("borrowing period", "The borrowing period is one calendar month from the actual borrowing date."),
        ("due date rule", "The due date is one calendar month after the borrowing date. If the next month has fewer days, the last day of that month is used."),
    ])

    # Borrowing & Returning procedures (Frames 5, 6, 7)
    pairs.extend([
        ("how to borrow", "To borrow a book:\n1. Specify the Book ID (e.g. B01) or Title.\n2. Provide your Student ID (e.g. TP123456).\n3. Confirm the borrowing details.\n\nNote: You may borrow up to 5 books for one calendar month."),
        ("borrow book", "To borrow a book, please provide the Book ID or Title, along with your Student ID (e.g., 'Borrow B01 for TP123456')."),
        ("how to return", "To return a book, please provide your Student ID and the Book ID or Title you are returning. I will verify your active borrowing record and confirm the return."),
        ("return book", "To return a book, tell me your Student ID and Book ID (e.g., 'Return B01 for TP123456')."),
        ("borrowing history", "To view your borrowing history, please provide your Student ID (e.g., 'History for TP123456')."),
        ("my history", "Please enter your Student ID to retrieve your active and completed borrowing records."),
    ])

    # =====================================================================
    # FRAME 9: DISCUSSION & STUDY ROOM BOOKINGS
    # =====================================================================
    rooms_summary = (
        "🏢 Library Discussion & Study Rooms (6 Rooms Available):\n"
        "• R01: Discussion Room Alpha (4-6 pax) — 55\" 4K TV, Glass Whiteboard, Conference Speaker\n"
        "• R02: Discussion Room Beta (4-6 pax) — Ultra-wide Monitor, Power Hubs, USB-C Dock\n"
        "• R03: Collaborative Studio Hub (6-8 pax) — Dual 4K Displays, PTZ Conference Cam\n"
        "• R04: Silent Focus Pod 1 (1-2 pax) — Ergonomic Chair, Acoustic Paneling, Qi Charger\n"
        "• R05: Silent Focus Pod 2 (1-2 pax) — Standing Desk, Dual 27\" Arms, ANC Headphones\n"
        "• R06: Digital Media & Podcast Lab (2-4 pax) — Shure SM7B Mics, Audio Console, 4K Rig\n\n"
        "To book, say 'Book R01 for [StudentID]' (e.g., 'Book R01 for TP123456'). Max duration: 2 hours."
    )
    pairs.extend([
        ("book room", rooms_summary),
        ("study rooms", rooms_summary),
        ("discussion rooms", rooms_summary),
        ("how to book a room", rooms_summary),
        ("reserve room", rooms_summary),
        ("list rooms", rooms_summary),
        ("available rooms", rooms_summary),
        ("rooms", rooms_summary),
        ("meeting room", rooms_summary),
        ("podcast room", "Our Digital Media & Podcast Lab (R06, Level 1) is equipped with Shure SM7B studio microphones, a Rodecaster Pro II audio console, studio lighting, and a 4K editing rig. Capacity: 2-4 pax. To book, type 'Book R06 for [StudentID]'."),
        ("silent pod", "We have two Silent Focus Pods on Level 3 (R04 and R05) featuring acoustic soundproofing, ergonomic seating, and standing desk options for 1-2 persons. To book, type 'Book R04 for [StudentID]' or 'Book R05 for [StudentID]'."),
        ("room booking rules", "📋 Room Booking Rules:\n• Maximum booking duration: 2 hours per session per student per day.\n• Available time slots: 09:00-11:00, 11:00-13:00, 14:00-16:00, 16:00-18:00, 18:00-20:00.\n• Check-in: Must check in within 15 minutes of slot start time or the reservation is released.\n• Advance booking: Up to 3 days in advance.\n• Cleanliness: No hot food allowed inside study rooms."),
        ("预订房间", "🏢 图书馆研讨室与自习舱（共 6 间）：\n• R01: 研讨室 Alpha (4-6人) — 55寸4K智能电视、玻璃白板\n• R02: 研讨室 Beta (4-6人) — 带鱼屏显示器、电源中继站\n• R03: 协作工作室 Hub (6-8人) — 双4K屏、云台会议摄像头\n• R04: 专注静音舱 1 (1-2人) — 人体工学椅、隔音棉、无线快充\n• R05: 专注静音舱 2 (1-2人) — 电动升降桌、双屏支架、降噪耳机\n• R06: 数码新媒体与播客录音室 (2-4人) — 舒尔专业麦克风、调音台、4K剪辑主机\n\n预约方式：输入 '预订 R01 学号 TP123456'，每次限时 2 小时。"),
        ("自习室", "图书馆自习室包括 2 号楼的讨论研讨室（R01-R03）、3 号楼的独立静音舱（R04-R05）以及 1 号楼的新媒体实验室（R06）。每名学生每天最多可预订 1 次，每次上限 2 小时。"),
    ])

    for r in ROOMS_DATA:
        r_reply = (
            f"🏢 Room {r['id']}: {r['name']} ({r['type']})\n"
            f"• Location: {r['floor']}\n"
            f"• Capacity: {r['capacity']}\n"
            f"• Equipment: {r['equipment']}\n"
            f"• Suitable for: {r['suitable_for']}\n"
            f"To book this room, type: 'Book {r['id']} for [Your Student ID]'"
        )
        pairs.append((r["id"].lower(), r_reply))
        pairs.append((f"book {r['id'].lower()}", r_reply))
        pairs.append((f"where is {r['name'].lower()}", f"📍 {r['name']} ({r['id']}) is located at {r['floor']}. Capacity: {r['capacity']}."))
        pairs.append((f"room {r['id'].lower()}", r_reply))

    # =====================================================================
    # FRAME 10: LIBRARY OPERATING HOURS
    # =====================================================================
    hours_summary = (
        "⏰ APU Library Operating Hours:\n"
        "• Monday – Friday: 08:30 AM – 09:00 PM\n"
        "• Saturday: 09:00 AM – 05:00 PM\n"
        "• Sunday & Public Holidays: 10:00 AM – 04:00 PM\n"
        "• Level 3 Silent Study Commons: 24/7 access during semester\n"
        "• Final Exam Extended Hours: Levels 1-2 open until 11:00 PM / Level 3 24 Hours\n"
        "• Counter Services (Circulation, Fines, Room Keys): Closes 30 minutes before library closing."
    )
    pairs.extend([
        ("library hours", hours_summary),
        ("hours", hours_summary),
        ("opening hours", hours_summary),
        ("operating hours", hours_summary),
        ("when do you open", hours_summary),
        ("what time do you open", "The library opens at 08:30 AM on weekdays (Monday-Friday), 09:00 AM on Saturdays, and 10:00 AM on Sundays and Public Holidays."),
        ("what time do you close", "The library closes at 09:00 PM on weekdays, 05:00 PM on Saturdays, and 04:00 PM on Sundays. (During final exams, open until 11:00 PM / 24/7 Level 3)."),
        ("when do you close", "The library closes at 09:00 PM on weekdays (Monday-Friday), 05:00 PM on Saturdays, and 04:00 PM on Sundays."),
        ("is the library open", "The library is open Monday–Friday 08:30 AM–09:00 PM, Saturday 09:00 AM–05:00 PM, and Sunday 10:00 AM–04:00 PM. The Level 3 Silent Study Commons is accessible 24/7."),
        ("is library open today", hours_summary),
        ("weekend hours", "Weekend Hours:\n• Saturday: 09:00 AM – 05:00 PM\n• Sunday: 10:00 AM – 04:00 PM\nLevel 3 Silent Study Commons remains accessible 24/7 with valid student card access."),
        ("sunday hours", "Sunday Operating Hours: 10:00 AM – 04:00 PM. Level 3 Silent Study Commons is open 24/7."),
        ("exam hours", "During the Final Examination Period, Levels 1 and 2 remain open with extended hours until 11:00 PM, while the Level 3 Silent Study Commons operates 24/7!"),
        ("counter hours", "Service counters (book borrowing/returns, fine payment, room key collection) close 30 minutes before the library closes (8:30 PM weekdays, 4:30 PM Saturdays, 3:30 PM Sundays)."),
        ("开放时间", "⏰ 图书馆开放时间：\n• 周一至周五：08:30 AM – 09:00 PM\n• 周六：09:00 AM – 05:00 PM\n• 周日及公共假期：10:00 AM – 04:00 PM\n• 3号楼静音自习区：学期内 24/7 全天候开放\n• 期末考试期间：主馆延长开放至 11:00 PM，3楼通宵开放\n• 综合服务台（借还书、缴费、房间钥匙）：闭馆前 30 分钟停止办理业务。"),
        ("几点关门", "工作日（周一至周五）晚上 9:00 闭馆，周六下午 5:00 闭馆，周日下午 4:00 闭馆。考试期间延长至晚上 11:00。"),
        ("几点开门", "工作日早上 8:30 开门，周六早上 9:00 开门，周日及假期早上 10:00 开门。"),
    ])

    # =====================================================================
    # FRAME 11: OVERDUE FINES & LATE RETURN RULES
    # =====================================================================
    fines_summary = (
        "💰 APU Library Overdue Fines & Late Return Policy:\n"
        "• General Collection Books (B01-B80): RM 0.50 per day per book overdue.\n"
        "• Red Spot / 2-Hour Reserve Loans: RM 1.00 per hour per item.\n"
        "• Grace Period: 1 calendar day grace period before charges begin accumulating.\n"
        "• Maximum Fine Cap: RM 25.00 per book maximum.\n"
        "• Lost Book Replacement: Actual purchase price of book + RM 20.00 administrative fee.\n"
        "• Suspension Rule: Borrowing and room reservations are blocked if unpaid fines exceed RM 10.00.\n"
        "• Payment Methods: Student Portal e-Payment, Service Counter, Touch 'n Go, Credit/Debit card."
    )
    pairs.extend([
        ("overdue fines", fines_summary),
        ("fines", fines_summary),
        ("late fee", fines_summary),
        ("late return fine", fines_summary),
        ("how much is fine", "The overdue fine for general collection books (B01-B80) is RM 0.50 per day per book, capped at RM 25.00 maximum per book. There is a 1-day grace period."),
        ("how much is overdue fine", "General collection books incur RM 0.50 per day per book after a 1-day grace period, up to a maximum of RM 25.00 per book."),
        ("maximum fine", "The maximum overdue fine is capped at RM 25.00 per book."),
        ("grace period", "The library provides a 1 calendar day grace period after the due date before late fines begin accumulating."),
        ("how to pay fine", "You can pay overdue fines via:\n1. Student Portal e-Payment (Online)\n2. Library Service Counter (Level 1)\n3. Touch 'n Go eWallet, Debit Card, or Credit Card."),
        ("lost book policy", "For lost or damaged books, you are required to pay the replacement cost of the book plus an administrative processing fee of RM 20.00."),
        ("unpaid fines", "If unpaid overdue fines exceed RM 10.00, your borrowing privileges and study room reservation access will be temporarily suspended until settled."),
        ("逾期罚款", "💰 图书馆逾期滞纳金与罚款政策：\n• 普通藏书（B01-B80）：逾期每天每本 RM 0.50。\n• 2小时短期预约图书：逾期每小时 RM 1.00。\n• 宽限期：到期日后享有 1 个自然日宽限期，宽限期内归还免罚款。\n• 罚款上限：每本书最高上限 RM 25.00。\n• 图书遗失赔偿：图书原价 + RM 20.00 行政手续费。\n• 权限暂停：未结清罚款超过 RM 10.00 将自动冻结借书和预订研讨室权限。\n• 缴费渠道：学生门户网银、图书馆前台柜台、Touch 'n Go 电子钱包、银行卡。"),
        ("还书逾期", "图书逾期每天每本收费 RM 0.50（最高上限 RM 25.00）。建议及时归还或在到期前办理续借。"),
    ])

    # Simulation disclaimer
    disclaimer = (
        "ℹ️ Implementation Notice (Frame 5 Rule 10, Global Instruction 12):\n"
        "This is an AI Chatbot for a simulated library assignment. The 80-book catalogue, "
        "shelf positions, copy counts, and transactions are simulated data."
    )
    pairs.extend([
        ("is this real", disclaimer),
        ("is this real library", disclaimer),
        ("real inventory", disclaimer),
    ])

    return pairs


if __name__ == "__main__":
    pairs = build_training_pairs()
    print(f"Total Q&A training pairs generated: {len(pairs)}")
    print(f"Sample pair: {pairs[0]}")
