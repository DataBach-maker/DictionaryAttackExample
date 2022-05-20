## libraries
import time
import hashlib
import pandas as pd

import random

class DictionaryAttack:
    def __init__(self, password=str):

        self.password = password
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

        self.success = "The password was found: "
        self.fail = "The password could not be cracked "

    def crack_password(self):
        
        with open(
            r"yourpath",
            "r",
            encoding="latin-1",
        ) as f:
            words = f.read().split()

            for word in words:
                word_hash = hashlib.sha256(word.encode()).hexdigest()

                if word_hash == self.password_hash:
                    return self.success + self.password
            else:
                return self.fail


if __name__ == "__main__":
    password_difficult = "difficultpassword##!!?*?235465367453"
    password_easy = "123456"

    start_time_difficult = time.time()
    attempt_result_difficult = DictionaryAttack(password_difficult).crack_password()
    end_time_difficult = time.time()
    total_time_elapsed_difficult = end_time_difficult - start_time_difficult

    print(
        attempt_result_difficult,
        ", The code ran: ",
        "{0:.10f}".format(total_time_elapsed_difficult),
    )

    start_time_easy = time.time()
    attempt_result_easy = DictionaryAttack(password_easy).crack_password()
    end_time_easy = time.time()

    total_time_elapsed_easy = end_time_easy - start_time_easy
    print(
        attempt_result_easy,
        ", The code ran: ",
        "{0:.10f}".format(total_time_elapsed_easy),
    )