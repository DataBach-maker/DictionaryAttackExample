## libraries
import time
import hashlib
import pandas as pd

import random

class dictionary_attack:
    def __init__(self, path=str):

        self.file_path = file_path
        self.df = self.hash_table(file_path)
        
        self.success = "The password was found: "
        self.fail = "The password could not be cracked "

    def hash_table(self, path):

        df = pd.read_csv(
            path,
            delimiter="\n",
            header=None,
            names=["Passwords"],
            encoding="ISO-8859-1",
        )

        def sha_encode(x):
            return hashlib.sha256(x.encode()).hexdigest()

        df["Hash"] = df["Passwords"].astype(str).apply(sha_encode)
        return df

    def crack_password(self, password):

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        solution = self.df.loc[self.df["Hash"] == password_hash]

        if solution.empty:
            return self.fail
        else:
            return self.success + password


if __name__ == "__main__":
    difficult_password = "difficultpassword##!!?*?235465367453"
    easy_password = "123456"

    file_path = r"C:\Users\Nutzer\Desktop\Projects\DictionaryAttack\rockyou.txt"

    attack = DictionaryAttack(file_path)

    start_time_difficult = time.time()
    attempt_result_difficult = attack.crack_password(difficult_password)
    end_time_difficult = time.time()
    total_time_elapsed_difficult = end_time_difficult - start_time_difficult

    print(
        attempt_result_difficult,
        ", The code ran: ",
        "{0:.10f}".format(total_time_elapsed_difficult),
    )

    start_time_easy = time.time()
    attempt_result_easy = attack.crack_password(easy_password)
    end_time_easy = time.time()
    total_time_elapsed_easy = end_time_easy - start_time_easy

    print(
        attempt_result_easy,
        ", The code ran: ",
        "{0:.10f}".format(total_time_elapsed_easy),
    )