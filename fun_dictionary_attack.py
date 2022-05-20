## libraries
import time
import hashlib
import pandas as pd

import random

class dictionary_attack:
    def __init__(self, path=str):

        self.path = path
        self.df = self.readCSV(self.path)
        
        self.df = self.identify_weak_passwords(self.df)
        self.df = self.generate_additional_passwords(self.df)
        
        self.df = self.create_hash_table(self.df)
        
        self.success = "The password was found: "
        self.fail = "The password could not be cracked "
        
    def readCSV(self, path):
        
        df = pd.read_csv(
            path,
            delimiter="\n",
            header=None,
            names=["Passwords"],
            encoding="ISO-8859-1",
        )
        
        return df

    def identify_weak_passwords(self, df):
        
        strong_password_regex = '(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        df["is_Weak_Password"] = ~df.Passwords.str.contains(strong_password_regex, na=False)
        
        return df
    
    def generate_additional_passwords(self, df):
        
        expression_one = df.loc[df['is_Weak_Password'] == True].Passwords + "!"
        expression_two = df.loc[df['is_Weak_Password'] == True].Passwords + str(random.randint(1940, 2022))

        expressions = [expression_one, expression_two]

        for expression in expressions:
            result_df = pd.concat((df["Passwords"], expression), axis=0)
            
        return result_df
    
    
    def create_hash_table(self, path):

        def sha_encode(password):
            return hashlib.sha256(password.encode()).hexdigest()

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