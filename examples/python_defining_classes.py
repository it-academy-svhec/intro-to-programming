class Computer:
    # Define class variables; shared by all instances of a class
    def __init__(self, id, make, model, serial_number, form_factor):
        # Define instance variables; owned by each instance of a class, i.e., an object
        self.id = id
        self.make = make
        self.model = model
        self.serial_number = serial_number
        self.form_factor = form_factor

    def print_info(self):
        print(
            f"ID: {self.id}\nMake: {self.make}\nModel: {self.model}\nSerial #: {self.serial_number}\nForm factor: {self.form_factor}\n")


# Instantiate Computer class object (an instance of Computer)
office_desktop = Computer(1, "Dell", "Inspiron 5675", "A3B9ZH2", "Desktop")
office_desktop.print_info()

# Update Model
office_desktop.model = "Inspiron 9000"
office_desktop.print_info()
