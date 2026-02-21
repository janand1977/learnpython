from oops.util.emp import Emp


class MyContextManager:
    name: str

    def __enter__(self):
        print("Entering the context")
        self.name = "MyContextManager"
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

    # def __str__(self):
    #     return f"MyContextManager with name: {self.name}"

    def __repr__(self):
        return f"MyContextManager with name: {self.name}"


# with MyContextManager() as manager:
#     print(manager)
#     print("Inside the context")


ex = Emp("John", 30, 50000)
print(ex)
