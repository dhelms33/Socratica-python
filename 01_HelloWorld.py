class Intro:
    def __init__(self):
        pass
    def hello_world(self):
        return "Hello World!"
    
def main():
    first_program_instance = Intro()
    first_program = first_program_instance.hello_world()
    print(first_program)

if __name__ == "__main__":
    main()