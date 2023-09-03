# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the engine and session
engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the models


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

    def customers(self):
        # Return a collection of all the customers who reviewed the Restaurant
        return [review.customer for review in self.reviews]

    @classmethod
    def fanciest(cls):
        # Return the restaurant instance with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        # Return a list of strings with all the reviews for this restaurant
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars." for review in self.reviews]


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the relationship between Customer and Review
    reviews = relationship('Review', back_populates='customer')

    def restaurants(self):
        # Return a collection of all the restaurants that the Customer has reviewed
        return [review.restaurant for review in self.reviews]

    def full_name(self):
        # Return the full name of the customer
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Return the restaurant instance that has the highest star rating from this customer
        reviews = sorted(
            self.reviews, key=lambda review: review.star_rating, reverse=True)
        return reviews[0].restaurant if reviews else None

    def add_review(self, restaurant, rating):
        # Create a new review for the restaurant with the given restaurant_id
        review = Review(restaurant=restaurant,
                        customer=self, star_rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        # Remove all the reviews for this restaurant
        session.query(Review).filter(Review.restaurant ==
                                     restaurant, Review.customer == self).delete()
        session.commit()


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

    # Define the relationship between Review and Restaurant
    restaurant = relationship('Restaurant', back_populates='reviews')

    # Define the relationship between Review and Customer
    customer = relationship('Customer', back_populates='reviews')

    def customer(self):
        # Return the Customer instance for this review
        return self.customer

    def restaurant(self):
        # Return the Restaurant instance for this review
        return self.restaurant

    def full_review(self):
        # Return a string formatted as "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars."
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
