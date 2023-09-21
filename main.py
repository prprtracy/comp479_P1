import os
import nltk

nltk.download('punkt')
nltk.download('stopwords')

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def Tokenizer_output(file_path):
    with open(file_path,'r')as file:
        text = file.read()
        tokens = word_tokenize(text)
        return tokens

def Lowercased_output(file_path):
    with open(file_path,'r')as file:
        text = file.read()
        lower_case = [token.lower() for token in Tokenizer_output(file_path)]
        return lower_case

def Stemmed_output(file_path):
    with open(file_path,'r')as file:
        text = file.read()
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in Tokenizer_output(file_path)]
        return stemmed_tokens

def No_Stopword_output(file_path,stop_words,stopwords_file_path):
    with open(file_path,'r')as file:
        text = file.read()
        
        # ==== Use the provided stopwords_file_path instead of the hardcoded path
        stop_words = Stopword_read(stopwords_file_path)
        No_Stopwords_tokens = [token for token in Tokenizer_output(file_path) if token not in stop_words ]
        return No_Stopwords_tokens

def Stopword_read(stopwords_file_path):
    with open(stopwords_file_path,'r') as stopwords_file:
        stop_words = [line.strip() for line in stopwords_file]
    return stop_words


def main():
    files_to_process = [
        'all-exchanges-strings.lc.txt',
        'all-orgs-strings.lc.txt',
        'all-people-strings.lc.txt',
        'all-places-strings.lc.txt',
        'all-topics-strings.lc.txt',
    ]

    # ==== using for loop to go through all 5 files  ====
    for file_name in files_to_process:
        file_path = os.path.join('./reuters21578.tar/', file_name)

        # ====Make the first word of each file as the stopwords and remove it from each file====
        # Stop_words = ["amex","adb-africa","abdel-hadi-kandeel","afghanistan","acq"]
        stopwords_filename = f'Stopwords_used_for_output_{file_name}'
        #print(stopwords_filename)
        stopwords_file_path = os.path.join('./Stopwords_used_for_output/',stopwords_filename)
        stop_words = Stopword_read(stopwords_file_path)

        # ==== print for the tokens that been tokenized
        tokens = Tokenizer_output(file_path)
        print(f'Tokenized File:{file_name}')
        print(tokens)
        print('\n\n')

        # ==== save the output of Tokenized file in to new txt file with name of 'Tokenizer_output_filename'
        Tokenizer_file_path = f'./Tokenizer_output/Tokenizer_output_{file_name}.txt'
        with open(Tokenizer_file_path,'w') as tokenizer_file:
            tokenizer_file.write('\n'.join(tokens))
        print(f'Tokenizer_output for {file_name} has been saved \n')

        #  ==== print for the tokens that been lower all tokens
        lower_tokens = Lowercased_output(file_path)
        print(f'Lowercase File:{file_name}')
        print(lower_tokens)
        print('\n\n')

        # ==== save the output of all text lowercase file in to new txt file with name of 'Lowercased_output_filename'
        lower_file_path = f'./Lowercased_output/Lowercased_output_{file_name}.txt'
        with open(lower_file_path, 'w') as lower_file:
            lower_file.write('\n'.join(lower_tokens))
        print(f'Lowercased_output for {file_name} has been saved \n')

        # ==== print for the tokens by using Porter stemmer
        stemmed_tokens = Stemmed_output(file_path)
        print(f'Stemmed File:{file_name}')
        print(stemmed_tokens)
        print('\n\n')

        # ==== save the output of the tokens by using Porter stemmer file in to new txt file with name of 'stemmed_output_filename'
        stemmed_file_path = f'./Stemmed_output/Stemmed_output_{file_name}.txt'
        with open(stemmed_file_path, 'w') as stemmed_file:
            stemmed_file.write('\n'.join(stemmed_tokens))
        print(f'Stemmed_output for {file_name} has been saved \n')

        # ==== print the tokens after remove the stopwords
        stopword_token = No_Stopword_output(file_path,stop_words,stopwords_file_path)
        print(f'No Stopwords File:{file_name}')
        print(stopword_token)
        print('\n\n')

        # ==== save the output of the tokens by using Porter stemmer file in to new txt file with name of 'stemmed_output_filename'
        No_stopwords_file_path = f'./No_stopword_output/No_stopword_output_{file_name}.txt'
        with open(No_stopwords_file_path, 'w') as No_stopwords_file:
            No_stopwords_file.write('\n'.join(stopword_token))
        print(f'No_stopword_output for {file_name} has been saved \n')





    #print("tokens for")
    #print(exchanges_tokens)

if __name__ == '__main__':
    main()



