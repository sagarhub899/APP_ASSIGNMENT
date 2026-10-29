
from functools import wraps


# Decorator Function
def report_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("           DYNAMIC REPORT GENERATOR")
        print("=" * 60)

        result = func(*args, **kwargs)

        print("=" * 60)
        print("             END OF REPORT")
        print("=" * 60)

        return result

    return wrapper


# Report Class
class Report:

    # Class Variable
    company_name = "ABC Technologies Pvt. Ltd."

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    # Instance Method
    def add_content(self, text):
        self.contents.append(text)

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    # Static Method
    @staticmethod
    def line():
        print("-" * 60)

    # Magic Method: __str__
    def __str__(self):
        return (
            f"Report Title : {self.title}\n"
            f"Author       : {self.author}"
        )

    # Magic Method: __len__
    def __len__(self):
        return len(self.contents)

    # Display Report using Decorator
    @report_decorator
    def display_report(self):
        print("Company :", self.company_name)
        print(self)

        Report.line()
        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")

        Report.line()
        print("Total Sections :", len(self))


# Main Program

# Create First Report
r1 = Report(
    "Advanced Python Practical Report",
    "Mandar Joshi"
)

r1.add_content("Completed Experiment No. 2 successfully.")
r1.add_content(
    "Implemented Decorators, Class Methods, Static Methods "
    "and Magic Methods."
)
r1.add_content("Learned Object-Oriented Programming concepts.")
r1.add_content("Report prepared by Mandar Joshi.")

# Display First Report
r1.display_report()

# Change Company Name
print("\nChanging Company Name...\n")
Report.change_company("MIT ADT University")

# Create Second Report
r2 = Report(
    "Faculty Practical Demonstration",
    "Mandar Joshi"
)

r2.add_content("Practical demonstrated successfully.")
r2.add_content("Students understood decorators.")
r2.add_content("Students understood class methods.")
r2.add_content("Students understood magic methods.")
r2.add_content("Students performed the practical successfully.")

# Display Second Report
r2.display_report()
