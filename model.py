from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    # Define the relationship with Review
    reviews = relationship('Review', back_populates='restaurant')
    # Define the relationship with Customer (many-to-many)
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def __repr__(self):
        return f"Restaurant(id={self.id}, name='{self.name}', price={self.price})"

    def all_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars" for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the relationship with Review
    reviews = relationship('Review', back_populates='customer')
    # Define the relationship with Restaurant (many-to-many)
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def __repr__(self):
        return f"Customer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # Define the relationship with Restaurant
    restaurant = relationship('Restaurant', back_populates='reviews')
    # Define the relationship with Customer
    customer = relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f"Review(id={self.id}, star_rating={self.star_rating})"

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"
