from django.test.runner import DiscoverRunner
from unittest.result import TestResult

class CustomTestResult(TestResult):
    def startTest(self, test):
        super().startTest(test)
        print("Pass", end='\t', flush=True)  # Print "Start" at the beginning of each test

class CustomTestRunner(DiscoverRunner):
    def get_resultclass(self):
        return CustomTestResult

        
    def printErrors(self):
        pass  # Suppress printing errors

    def addSuccess(self, test):
        super().addSuccess(test)
        print(" Pass", end='', flush=True)

    def addFailure(self, test, err):
        self.stream.write("Fail")  # Print a "Fail" symbol for each failed test
        self.stream.flush()

    def addError(self, test, err):
        self.stream.write("Error")  # Print an "Error" symbol for each test with an error
        self.stream.flush()

    def startTest(self, test):
        super().startTest(test)
        self.stream.write(" Start ")  # Print a dot symbol at the start of each test


    