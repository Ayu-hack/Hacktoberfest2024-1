import bisect

class StockTracker:
    def __init__(self):
        # Initialize an empty list to store the stock prices
        self.prices = []

    def add_price(self, price):
        """
        Inserts the stock price into the sorted list while maintaining sorted order.
        Uses the 'bisect.insort' method, which efficiently inserts into a sorted list.
        Edge case handled: if price is not a valid positive number or not a number, it prints an error.
        """
        if isinstance(price, (int, float)) and price >= 0:
            # Insert the price in the correct sorted position
            bisect.insort(self.prices, price)
        else:
            # Handle invalid inputs like negative prices or non-numeric values
            print(f"Invalid price: {price}, price should be a positive number")

    def get_median(self):
        """
        Returns the median of the stock prices.
        - If no prices are present, return None.
        - For odd numbers of prices, return the middle one.
        - For even numbers of prices, return the average of the two middle prices.
        """
        if not self.prices:
            # No prices added yet, return None (edge case)
            return None

        # Calculate the length of the list of prices
        n = len(self.prices)

        # If the number of prices is even, calculate the average of the two middle elements
        if n % 2 == 0:
            return (self.prices[n // 2 - 1] + self.prices[n // 2]) / 2
        else:
            # If the number of prices is odd, return the middle element
            return self.prices[n // 2]

    def get_min(self):
        """
        Returns the minimum stock price.
        If no prices are available, return None (edge case).
        """
        return self.prices[0] if self.prices else None

    def get_max(self):
        """
        Returns the maximum stock price.
        If no prices are available, return None (edge case).
        """
        return self.prices[-1] if self.prices else None

# Test Cases
tracker = StockTracker()

# Edge case: no prices added yet
print("Median:", tracker.get_median())  # Output: None (no prices yet)

# Add stock prices and test the tracker
tracker.add_price(100)
tracker.add_price(200)
tracker.add_price(150)

# After adding [100, 150, 200]
print("Median:", tracker.get_median())  # Output: 150 (middle price)
print("Min:", tracker.get_min())        # Output: 100 (smallest price)
print("Max:", tracker.get_max())        # Output: 200 (largest price)

# Edge case: invalid input
tracker.add_price(-10)  # Invalid price: will print an error
tracker.add_price("abc")  # Invalid price: will print an error
