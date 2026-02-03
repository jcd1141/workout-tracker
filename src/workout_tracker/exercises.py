"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        self.name = name
        if date == None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
            return f"{self.name}: {self.calculate_calories()} calories"


class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name: str, distance: float, duration: float, date: str = None):
        super().__init__(name, date)
        self.distance = distance
        self.duration = duration
    
    def calculate_calories(self) -> float:
        return self.distance*100
    
    def get_duration(self) -> float:
        return self.duration
    
    def __str__(self) -> str:
        return f"{self.name} ({self.distance} miles, {self.duration} min): {self.calculate_calories()} calories"