class datastorage:
    def __init__(self):
        # Dictionary to store user accounts with username as key and password as value
        self.accounts = {}
        # Dictionary to store followed congressmen for each user
        self.user_congressmen = {}

    def register_user(self, username, password):
        """
        Register a new user with a username and password.
        """
        if username in self.accounts:
            return False  # Username already exists
        self.accounts[username] = password
        self.user_congressmen[username] = set()  # Initialize an empty set for followed congressmen
        return True

    def validate_login(self, username, password):
        """
        Validate a user's login credentials.
        """
        return username in self.accounts and self.accounts[username] == password

    def follow_congressman(self, username, congressman):
        """
        Add a congressman to the list of those followed by the user.
        """
        if username in self.user_congressmen:
            self.user_congressmen[username].add(congressman)
            return True
        return False

    def get_followed_congressmen(self, username):
        """
        Retrieve the list of congressmen followed by the user.
        """
        return self.user_congressmen.get(username, set())

    def list_all_congressmen(self):
        """
        Return a list of all available congressmen (mock data).
        """
        return ["Jerry Carl", "Barry Moore", "Mike Rogers", "Robert Aderholt", "Dale Strong", "Gary Palmer", "Terri Sewell", "Mary Peltola", 
                "Aumua Amata Radewagen", "David Schweikert", "Elijah Crane", "Ruben Gallego", "Greg Stanton", "Andy Biggs", "Juan Ciscomani", 
                "Raul Grijalva", "Debbie Lesko", "Paul Gosar", "Eric Crawford", "J. Hill", "Steve Womack", "Bruce Westerman", "Doug LaMalfa", 
                "Jared Huffman", "Kevin Kiley", "Mike Thompson", "Tom McClintock", "Ami Bera", "Doris Matsui", "John Garamendi", "Josh Harder", 
                "Mark DeSaulnier", "Nancy Pelosi", "Barbara Lee", "John Duarte", "Eric Swalwell", "Kevin Mullin", "Anna Eshoo", "Ro Khanna", 
                "Zoe Lofgren", "Jimmy Panetta", "Vince Fong", "Jim Costa", "David Valadao", "Jay Obernolte", "Salud Carbajal", "Raul Ruiz", 
                "Julia Brownley", "Mike Garcia", "Judy Chu", "Tony Cardenas", "Adam Schiff", "Grace Napolitano", "Brad Sherman", "Pete Aguilar", 
                "Jimmy Gomez", "Norma Torres", "Ted Lieu", "Sydney Kamlager-Dove", "Linda Sanchez", "Mark Takano", "Young Kim", "Ken Calvert", 
                "Robert Garcia", "Maxine Waters", "Nanette Barragan", "Michelle Steel", "J. Correa", "Katie Porter", "Darrell Issa", "Mike Levin", 
                "Scott Peters", "Sara Jacobs", "Juan Vargas", "Diana DeGette", "Joe Neguse", "Lauren Boebert", "Greg Lopez", "Doug Lamborn", 
                "Jason Crow", "Brittany Pettersen", "Yadira Caraveo", "John Larson", "Joe Courtney", "Rosa DeLauro", "James Himes", "Jahana Hayes", 
                "Lisa Blunt Rochester", "Eleanor Norton", "Matt Gaetz", "Neal Dunn", "Kat Cammack", "Aaron Bean", "John Rutherford", "Michael Waltz", 
                "Cory Mills", "Bill Posey", "Darren Soto", "Maxwell Frost", "Daniel Webster", "Gus Bilirakis", "Anna Paulina Luna", "Kathy Castor", 
                "Laurel Lee", "Vern Buchanan", "W. Steube", "Scott Franklin", "Byron Donalds", "Sheila Cherfilus-McCormick", "Brian Mast", 
                "Lois Frankel", "Jared Moskowitz", "Frederica Wilson", "Debbie Wasserman Schultz", "Mario Diaz-Balart", "Maria Salazar", 
                "Carlos Gimenez", "Earl Carter", "Sanford Bishop", "A. Ferguson", "Henry Johnson", "Nikema Williams", "Richard McCormick", 
                "Lucy McBath", "Austin Scott", "Andrew Clyde", "Mike Collins", "Barry Loudermilk", "Rick Allen", "David Scott", "Marjorie Greene", 
                "James Moylan", "Ed Case", "Jill Tokuda", "Russ Fulcher", "Michael Simpson", "Jonathan Jackson", "Robin Kelly", "Delia Ramirez", 
                "Jesus Garcia", "Mike Quigley", "Sean Casten", "Danny Davis", "Raja Krishnamoorthi", "Janice Schakowsky", "Bradley Schneider", 
                "Bill Foster", "Mike Bost", "Nikki Budzinski", "Lauren Underwood", "Mary Miller", "Darin LaHood", "Eric Sorensen", "Frank Mrvan", 
                "Rudy Yakym", "Jim Banks", "James Baird", "Victoria Spartz", "Greg Pence", "Andre Carson", "Larry Bucshon", "Erin Houchin", 
                "Mariannette Miller-Meeks", "Ashley Hinson", "Zachary Nunn", "Randy Feenstra", "Tracey Mann", "Jake LaTurner", "Sharice Davids", 
                "Ron Estes", "James Comer", "Brett Guthrie", "Morgan McGarvey", "Thomas Massie", "Harold Rogers", "Andy Barr", "Steve Scalise", 
                "Troy Carter", "Clay Higgins", "Mike Johnson", "Julia Letlow", "Garret Graves", "Chellie Pingree", "Jared Golden", "Andy Harris", 
                "C. Ruppersberger", "John Sarbanes", "Glenn Ivey", "Steny Hoyer", "David Trone", "Kweisi Mfume", "Jamie Raskin", "Richard Neal", 
                "James McGovern", "Lori Trahan", "Jake Auchincloss", "Katherine Clark", "Seth Moulton", "Ayanna Pressley", "Stephen Lynch", 
                "William Keating", "Jack Bergman", "John Moolenaar", "Hillary Scholten", "Bill Huizenga", "Tim Walberg", "Debbie Dingell", 
                "Elissa Slotkin", "Daniel Kildee", "Lisa McClain", "John James", "Haley Stevens", "Rashida Tlaib", "Shri Thanedar", "Brad Finstad", 
                "Angie Craig", "Dean Phillips", "Betty McCollum", "Ilhan Omar", "Tom Emmer", "Michelle Fischbach", "Pete Stauber", "Trent Kelly", 
                "Bennie Thompson", "Michael Guest", "Mike Ezell", "Cori Bush", "Ann Wagner", "Blaine Luetkemeyer", "Mark Alford", "Emanuel Cleaver", 
                "Sam Graves", "Eric Burlison", "Jason Smith", "Ryan Zinke", "Matthew Rosendale", "Mike Flood", "Don Bacon", "Adrian Smith", 
                "Dina Titus", "Mark Amodei", "Susie Lee", "Steven Horsford", "Chris Pappas", "Ann Kuster", "Donald Norcross", "Jefferson Van Drew", 
                "Andy Kim", "Christopher Smith", "Josh Gottheimer", "Frank Pallone", "Thomas Kean", "Robert Menendez", "Bill Pascrell", 
                "LaMonica McIver", "Mikie Sherrill", "Bonnie Watson Coleman", "Melanie Stansbury", "Gabe Vasquez", "Teresa Leger Fernandez", 
                "Nick LaLota", "Andrew Garbarino", "Thomas Suozzi", "Anthony D'Esposito", "Gregory Meeks", "Grace Meng", "Nydia Velazquez", 
                "Hakeem Jeffries", "Yvette Clarke", "Daniel Goldman", "Nicole Malliotakis", "Jerrold Nadler", "Adriano Espaillat", 
                "Alexandria Ocasio-Cortez", "Ritchie Torres", "Jamaal Bowman", "Michael Lawler", "Patrick Ryan", "Marcus Molinaro", 
                "Paul Tonko", "Elise Stefanik", "Brandon Williams", "Nicholas Langworthy", "Claudia Tenney", "Joseph Morelle", "Timothy Kennedy", 
                "Donald Davis", "Deborah Ross", "Gregory Murphy", "Valerie Foushee", "Virginia Foxx", "Kathy Manning", "David Rouzer", "Dan Bishop", 
                "Richard Hudson", "Patrick McHenry", "Chuck Edwards", "Alma Adams", "Wiley Nickel", "Jeff Jackson", "Kelly Armstrong", 
                "Gregorio Sablan", "Greg Landsman", "Brad Wenstrup", "Joyce Beatty", "Jim Jordan", "Robert Latta", "Michael Rulli", "Max Miller", 
                "Warren Davidson", "Marcy Kaptur", "Michael Turner", "Shontel Brown", "Troy Balderson", "Emilia Sykes", "David Joyce", "Mike Carey", 
                "Kevin Hern", "Josh Brecheen", "Frank Lucas", "Tom Cole", "Stephanie Bice", "Suzanne Bonamici", "Cliff Bentz", "Earl Blumenauer", 
                "Val Hoyle", "Lori Chavez-DeRemer", "Andrea Salinas", "Brian Fitzpatrick", "Brendan Boyle", "Dwight Evans", "Madeleine Dean", 
                "Mary Gay Scanlon", "Chrissy Houlahan", "Susan Wild", "Matt Cartwright", "Daniel Meuser", "Scott Perry", "Lloyd Smucker", 
                "Summer Lee", "John Joyce", "Guy Reschenthaler", "Glenn Thompson", "Mike Kelly", "Christopher Deluzio", "Jenniffer Gonzalez-Colon", 
                "Gabe Amo", "Seth Magaziner", "Nancy Mace", "Joe Wilson", "Jeff Duncan", "William Timmons", "Ralph Norman", "James Clyburn", 
                "Russell Fry", "Dusty Johnson", "Diana Harshbarger", "Tim Burchett", "Charles Fleischmann", "Scott DesJarlais", "Andrew Ogles", 
                "John Rose", "Mark Green", "David Kustoff", "Steve Cohen", "Nathaniel Moran", "Dan Crenshaw", "Keith Self", "Pat Fallon", 
                "Lance Gooden", "Jake Ellzey", "Lizzie Fletcher", "Morgan Luttrell", "Al Green", "Michael McCaul", "August Pfluger", "Kay Granger", 
                "Ronny Jackson", "Randy Weber", "Monica De La Cruz", "Veronica Escobar", "Pete Sessions", "Erica Lee Carter", "Jodey Arrington", 
                "Joaquin Castro", "Chip Roy", "Troy Nehls", "Tony Gonzales", "Beth Van Duyne", "Roger Williams", "Michael Burgess", "Michael Cloud", 
                "Henry Cuellar", "Sylvia Garcia", "Jasmine Crockett", "John Carter", "Colin Allred", "Marc Veasey", "Vicente Gonzalez", 
                "Greg Casar", "Brian Babin", "Lloyd Doggett", "Wesley Hunt", "Blake Moore", "Celeste Maloy", "John Curtis", "Burgess Owens", 
                "Becca Balint", "Robert Wittman", "Jennifer Kiggans", "Robert Scott", "Jennifer McClellan", "Bob Good", "Ben Cline", 
                "Abigail Spanberger", "Donald Beyer", "H. Griffith", "Jennifer Wexton", "Gerald Connolly", "Stacey Plaskett", "Suzan DelBene", 
                "Rick Larsen", "Marie Perez", "Dan Newhouse", "Cathy Rodgers", "Derek Kilmer", "Pramila Jayapal", "Kim Schrier", "Adam Smith", 
                "Marilyn Strickland", "Carol Miller", "Alexander Mooney", "Bryan Steil", "Mark Pocan", "Derrick Van Orden", "Gwen Moore", 
                "Scott Fitzgerald", "Glenn Grothman", "Thomas Tiffany", "Tony Wied", "Harriet Hageman"]