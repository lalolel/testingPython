import unittest
import warnings

# Task 9: Fix the match_pet function
# Function to match a pet with an adopter based on preferences
def match_pet(adopter_preferences, pets):
    """
    Match a pet with an adopter based on their preferences.
    All preferences (type, size, age) must match exactly.
    
    Args:
        adopter_preferences (dict): Dictionary with 'type', 'size', 'age' keys
        pets (list): List of pet dictionaries with 'name', 'type', 'size', 'age' keys
    
    Returns:
        str: Pet name if match found, otherwise "No match found"
    """
    for pet in pets:
        # Fixed: Changed OR logic to AND logic - all preferences must match
        if (adopter_preferences["type"] == pet["type"] and 
            adopter_preferences["size"] == pet["size"] and 
            adopter_preferences["age"] == pet["age"]):
            return pet["name"]
    return "No match found"

# Task 9: Fix the calculate_adoption_fee function
# Function to calculate adoption fee based on the pet's age
def calculate_adoption_fee(pet_age):
    """
    Calculate adoption fee based on pet's age.
    
    Args:
        pet_age (int): Age of the pet in years
    
    Returns:
        int or str: Fee amount (100 for young pets, 50 for adults) or "Invalid age" for negative ages
    """
    # Fixed: Added validation for negative ages
    if pet_age < 0:
        return "Invalid age"
    elif pet_age < 2:
        return 100  # Younger pets have higher fees
    else:
        return 50  # Adult pets have lower fees

# Task 9: Fix the register_new_pet function
# Function to add a new pet to the adoption list
def register_new_pet(new_pet, adoption_list):
    """
    Add a new pet to the adoption list with duplicate checking.
    
    Args:
        new_pet (dict): Dictionary with pet information including 'name'
        adoption_list (list): List of existing pets
    
    Returns:
        list: Updated adoption list
    """
    # Fixed: Changed from checking 'type' to checking 'name' for duplicates
    if any(existing_pet["name"] == new_pet["name"] for existing_pet in adoption_list):
        warnings.warn(f"{new_pet['name']} is already in the adoption list", UserWarning)
    else:
        adoption_list.append(new_pet)
    return adoption_list

class TestPetAdoptionCenter(unittest.TestCase):
    
    # Task 7: Create test fixtures using setUp() and tearDown()
    def setUp(self):
        """
        Set up test fixtures before each test.
        Initialize a list of pets for testing.
        """
        self.pets = [
            {"name": "Buddy", "type": "dog", "size": "medium", "age": 3},
            {"name": "Whiskers", "type": "cat", "size": "small", "age": 1},
            {"name": "Max", "type": "dog", "size": "large", "age": 5},
            {"name": "Luna", "type": "cat", "size": "small", "age": 2}
        ]
        self.adoption_list = []
    
    def tearDown(self):
        """
        Clean up after each test.
        Reset the pet list and adoption list.
        """
        self.pets = []
        self.adoption_list = []
    
    # Task 3: Write unit tests for match_pet() function
    def test_match_pet(self):
        """
        Test the match_pet function for correct matching behavior.
        """
        # Test Case 1: Test that the correct pet is matched when preferences match exactly
        adopter_preferences = {"type": "cat", "size": "small", "age": 1}
        result = match_pet(adopter_preferences, self.pets)
        self.assertEqual(result, "Whiskers", "Should match Whiskers for exact preferences")
        
        # Test Case 2: Test that function returns "No match found" when no pet matches
        adopter_preferences_no_match = {"type": "bird", "size": "small", "age": 1}
        result_no_match = match_pet(adopter_preferences_no_match, self.pets)
        self.assertEqual(result_no_match, "No match found", "Should return 'No match found' when no pets match")
        
        # Additional Test Case: Test partial match (should not match with fixed AND logic)
        adopter_preferences_partial = {"type": "dog", "size": "small", "age": 1}  # Only type matches some pets
        result_partial = match_pet(adopter_preferences_partial, self.pets)
        self.assertEqual(result_partial, "No match found", "Should not match when only some preferences match")
    
    # Task 4: Write unit tests for calculate_adoption_fee() function
    def test_calculate_adoption_fee(self):
        """
        Test the calculate_adoption_fee function for correct fee calculation.
        """
        # Test Case 1: Test that a young pet (1 year) returns correct fee (100)
        young_pet_fee = calculate_adoption_fee(1)
        self.assertEqual(young_pet_fee, 100, "Young pets (under 2 years) should have fee of 100")
        
        # Test Case 2: Test that an adult pet (3 years) returns correct fee (50)
        adult_pet_fee = calculate_adoption_fee(3)
        self.assertEqual(adult_pet_fee, 50, "Adult pets (2+ years) should have fee of 50")
        
        # Test Case 3: Test that invalid pet age (-1) returns "Invalid age"
        invalid_age_result = calculate_adoption_fee(-1)
        self.assertEqual(invalid_age_result, "Invalid age", "Negative ages should return 'Invalid age'")
        
        # Additional Test Case: Test boundary condition (exactly 2 years)
        boundary_age_fee = calculate_adoption_fee(2)
        self.assertEqual(boundary_age_fee, 50, "Pets exactly 2 years old should have adult fee (50)")
    
    # Task 5: Write unit tests for register_new_pet() function
    def test_register_new_pet(self):
        """
        Test the register_new_pet function for adding pets and handling duplicates.
        """
        # Test Case 1: Test that a new pet is successfully added to adoption list
        new_pet = {"name": "Charlie", "type": "dog", "size": "medium", "age": 2}
        updated_list = register_new_pet(new_pet, self.adoption_list)
        self.assertIn(new_pet, updated_list, "New pet should be added to the adoption list")
        self.assertEqual(len(updated_list), 1, "Adoption list should have one pet after adding")
        
        # Test Case 2: Test that a warning is raised when attempting to add duplicate pet
        duplicate_pet = {"name": "Charlie", "type": "cat", "size": "small", "age": 1}  # Same name, different details
        
        # Use assertWarns to check that a warning is raised
        with self.assertWarns(UserWarning):
            register_new_pet(duplicate_pet, updated_list)
        
        # Verify the list length hasn't changed (duplicate wasn't added)
        final_list = register_new_pet(duplicate_pet, updated_list)
        self.assertEqual(len(final_list), 1, "Duplicate pet should not increase list size")
    
    # Task 6: Write a test that skips execution for future functionality
    @unittest.skip("Skipping exotic pet registration - feature not yet implemented")
    def test_register_exotic_pet(self):
        """
        Test for adding exotic pets (like parrots) to the adoption list.
        This test is skipped as the feature is planned for future implementation.
        """
        exotic_pet = {"name": "Polly", "type": "parrot", "size": "small", "age": 2}
        updated_list = register_new_pet(exotic_pet, self.adoption_list)
        self.assertIn(exotic_pet, updated_list, "Exotic pet should be added to adoption list")
    
    # Additional comprehensive tests for better coverage
    def test_empty_pet_list(self):
        """
        Test match_pet function with empty pet list.
        """
        adopter_preferences = {"type": "dog", "size": "medium", "age": 3}
        result = match_pet(adopter_preferences, [])
        self.assertEqual(result, "No match found", "Should return 'No match found' for empty pet list")
    
    def test_multiple_matching_pets(self):
        """
        Test that match_pet returns the first matching pet when multiple pets match.
        """
        # Add another cat with same characteristics as Whiskers
        test_pets = self.pets + [{"name": "Shadow", "type": "cat", "size": "small", "age": 1}]
        adopter_preferences = {"type": "cat", "size": "small", "age": 1}
        result = match_pet(adopter_preferences, test_pets)
        self.assertEqual(result, "Whiskers", "Should return first matching pet (Whiskers)")
    
    def test_zero_age_pet(self):
        """
        Test calculate_adoption_fee with zero age (should be treated as young pet).
        """
        zero_age_fee = calculate_adoption_fee(0)
        self.assertEqual(zero_age_fee, 100, "Zero age pets should have young pet fee (100)")

if __name__ == "__main__":
    # Task 10: Run all tests to ensure everything works correctly
    print("Running Pet Adoption Center Tests...")
    print("=" * 50)
    
    # Run the tests with verbose output
    unittest.main(verbosity=2)
