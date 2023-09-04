
# SQLAlchemy Restaurant Reviews

## Description

This project is a Python application that uses SQLAlchemy, a popular Object Relational Mapping (ORM) library, to manage restaurant reviews. It allows users to perform various actions, including adding and deleting reviews, finding the fanciest restaurant, and retrieving reviews for a specific restaurant.

## Project Setup

To set up and run this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/restaurant-reviews.git
   cd restaurant-reviews
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install sqlalchemy
   ```

4. **Run the Database Migration** (if applicable):

   If you're using a database other than SQLite, you may need to run database migrations or create the database schema according to your database configuration.

5. **Seed the Database**:

   ```bash
   python3 seed.py
   ```

   This will populate the database with sample data.

6. **Run the Application**:

   ```bash
   python3 app.py
   ```

   The application will start, and you can interact with it in the terminal.

7. **Customize and Extend**:

   Feel free to customize and extend the code to suit your specific requirements. You can modify the data models, add new features, or enhance the user interface.

## Author & License

**Author:** DENNIS DARIUS MUKOYA

**License:** This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
