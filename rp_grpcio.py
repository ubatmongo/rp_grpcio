from src import calculator
from src import gcloud_storage

if __name__ == "__main__":
    new_calc = calculator.Calculator()
    print(new_calc.add(6))
    print(new_calc.add(12))
    print(new_calc.add(67.85))

    gcloud_storage.download()
