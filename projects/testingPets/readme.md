Tasks 1-2: Code Review and Analysis

✅ Reviewed the buggy code and identified issues in all three functions

Task 3: Unit Tests for match_pet() Function

✅ Test Case 1: Verifies correct pet matching when all preferences match exactly
✅ Test Case 2: Tests "No match found" return when no pets match
✅ Additional test for partial matches (should fail with original buggy OR logic)

Task 4: Unit Tests for calculate_adoption_fee() Function

✅ Test Case 1: Young pet (1 year) returns fee of 100
✅ Test Case 2: Adult pet (3 years) returns fee of 50
✅ Test Case 3: Invalid age (-1) returns "Invalid age"
✅ Additional boundary test for exactly 2 years old

Task 5: Unit Tests for register_new_pet() Function

✅ Test Case 1: Successfully adds new pet to adoption list
✅ Test Case 2: Raises warning when adding duplicate pet (by name)

Task 6: Skip Test for Future Functionality

✅ Added @unittest.skip() decorator for exotic pet registration test

Task 7: Test Fixtures with setUp() and tearDown()

✅ setUp(): Initializes test data (pets list and adoption list) before each test
✅ tearDown(): Cleans up test data after each test

Task 8-9: Bug Identification and Fixes
Fixed three major bugs:

match_pet() Function:

Bug: Used OR logic instead of AND logic
Fix: Changed to AND logic so ALL preferences must match exactly


calculate_adoption_fee() Function:

Bug: No validation for negative ages
Fix: Added check to return "Invalid age" for negative ages


register_new_pet() Function:

Bug: Checked existing_pet["type"] instead of existing_pet["name"]
Fix: Changed to check existing_pet["name"] for proper duplicate detection



Task 10: Final Testing

✅ All tests now pass with the bug fixes
✅ Added comprehensive test coverage including edge cases

Key Features Added:

Comprehensive Documentation: Added detailed docstrings for all functions
Edge Case Testing: Tests for empty lists, boundary conditions, and multiple matches
Proper Error Handling: Validation for invalid inputs
Warning System: Proper duplicate detection with warnings
Verbose Test Output: Detailed test results when running
