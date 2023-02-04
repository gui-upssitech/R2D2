from termcolor import colored

class Tester:

    def __init__(self):
        self.num_test = 0
        self.num_test_ok = 0

    def test(self, desc: str, test, expected):
        self.num_test += 1
        
        print(
            colored(f"[Test {self.num_test}]", "grey"), 
            f"{desc}", 
            colored(f"(expecting {expected})", "grey"), 
            end=" "
        )
        
        if test == expected:
            self.num_test_ok += 1
            print(colored("PASS", "green"))
        else:
            print(colored("FAIL", "red"))

    def summary(self):
        print(f"{self.num_test_ok}/{self.num_test} tests passed")