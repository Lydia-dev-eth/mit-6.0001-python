📄 README – MIT 6.100A PSet 3: Text Similarity & TF-IDF
📌 Overview
This program analyzes text files to measure similarity and word importance using:
Word frequencies
Letter frequencies
Similarity scoring
TF-IDF (Term Frequency–Inverse Document Frequency)
The implementation follows a step-by-step pipeline where raw text is cleaned, converted into lists, and then analyzed using dictionaries.
⚙️ Data Processing
load_file(filename)
Reads a file
Removes punctuation using string.punctuation
Converts everything to lowercase
👉 Output: cleaned string
text_to_list(input_text)
Converts text into a list of words
Splits manually using spaces and newlines
👉 Example:
"hello world\nhello" → ['hello', 'world', 'hello'] 
📊 Frequency Functions
get_frequencies(input_iterable)
Counts how many times each word appears
Uses a dictionary
👉 Example:
['hello', 'world', 'hello'] → {'hello': 2, 'world': 1} 
get_letter_frequencies(word)
Counts frequency of each letter in a word
👉 Example:
'hello' → {'h':1, 'e':1, 'l':2, 'o':1} 
🔍 Similarity
calculate_similarity_score(freq_dict1, freq_dict2)
This function compares two frequency dictionaries.
Steps:
Combine all unique keys from both dictionaries
For each element: 
Compute difference in frequency
Compute total frequency
Apply formula:
Similarity = 1 - (DIFF / ALL) 
Round to 2 decimal places
👉 Output: value between 0 and 1
🏆 Most Frequent Words
get_most_frequent_words(freq_dict1, freq_dict2)
Logic:
Combine keys from both dictionaries
Find: 
max word in dict1
max word in dict2
Compare their frequencies
Return: 
one word OR
both words if tied
📈 TF-IDF Implementation
get_tf(file_path)
Steps:
Load file
Convert to list of words
Count frequencies using get_frequencies
Divide each count by total number of words
Formula:
TF(word) = count(word) / total_words 
👉 Output:
{ word: TF value } 
get_idf(file_paths)
Steps:
Load all documents:
list_documents = [list of word lists] 
Flatten all words:
expand.extend(list1) 
Create unique word list:
if word not in uniq_list: uniq_list.append(word) 
For each word:
Count how many documents contain it:
if word in file: count += 1 
Apply formula:
IDF = log10(n / count) 
👉 Output:
{ word: IDF value } 
get_tfidf(tf_file_path, idf_file_paths)
Steps:
Compute TF:
TF_dic = get_tf(tf_file_path) 
Compute IDF:
IDF_dic = get_idf(idf_file_paths) 
Multiply:
TF-IDF = TF * IDF 
Store results:
tdidf[word] = TF_dic[word] * IDF_dic[word] 
Sort:
sorted(tdidf.items(), key=lambda item: (item[1], item[0])) 
Sorting rule:
First by TF-IDF score (ascending)
Then alphabetically
👉 Output:
[(word, score), ...] 
🧠 Key Design Choices
Used append for adding single words
Used extend to flatten lists of words
Used dictionaries for efficient counting
Ensured each document contributes only once in IDF
⚠️ Important Notes
Words are already lowercase (handled in load_file)
Punctuation is removed before processing
TF-IDF values depend on correct document counting
Sorting is required to pass test cases
✅ Example Output
TF: {'hello': 0.666..., 'world': 0.333...} IDF: {'hello': 0.0, 'world': 0.301..., 'friends': 0.301...} TF-IDF: [('hello', 0.0), ('world', 0.1003...)] 
🎯 Conclusion
This implementation demonstrates:
Text preprocessing
Frequency analysis
Similarity measurement
TF-IDF ranking
It shows how simple counting and math can be used to compare and analyze documents.
