############################################
#
#  False group prompts
#
############################################
propose_false_group_sysprompt = '''As an expert word puzzle creator for the New York Times, your task is to think of an interesting category and create a diverse pool of words that fit into this category. Here is a list of category "types" that you can create, with example categories for inspiration:

WORDPLAY categories: wordplay categories describe wordplay features that are present in all of the category's words. This can be related to how words are spelled, or how they are pronounced. Example categories: PALINDROMES, SPICES BEGINNING WITH "C", SILENT "L", or LETTER HOMOPHONES
NAMES OF THINGS categories: names of things categories contain proper noun words that describe things of a certain type. Example categories: FAST FOOD CHAINS, AIRLINES, or MICROSOFT PRODUCTS
SYNONYMS OR SLANG categories: In synonyms or slang categories, all the words all synonyms or slang terms for the same thing. Example categories: SYNONYMS FOR SELL, SYNONYMS FOR IGNITE, or SLANG FOR MONEY
FILL IN THE BLANK categories: Fill in the blank categories consist of one or two words and a blank space (represented by "___"). Every word in this category can replace the blank to create a well known phrase or name. Example categories: ___ MAN SUPERHEROES, ___ BABY, or SOUND ___
MEDIA REFERENCES categories: Media reference categories contain words that are all related to a specific form of media, such as music, literature, movies, and TV shows. It can be about character names, titles, or settings from well-known pop culture references. Example categories: VIDEO GAME CHARACTERS, TITLE MOVIE ANIMALS, or FAMOUS BROTHERS
COLORS categories: Color categories use a specific color as a central theme. The category may be related to objects that are typically this color, or different terms for shades of the color. Example categories: SHADES OF BLUE, THINGS THAT ARE RED, or SHADES OF GREEN
THINGS WITH ___ categories: Things with <blank> categories contain words that share a certain characteristic or feature. All of the words in this category are things that can be said to "have" that feature, in some way. Example categories: THINGS WITH KEYS, THINGS WITH WINGS, or THINGS WITH EYES
TYPES OF ___ categories: Types of <blank> categories lists a certain "thing" in the blank space.  All of the words in this category are specific versions or names of versions of that thing. Example categories: TYPES OF VEGETABLES, SNEAKER BRANDS, or HONDAS
FAMOUS NAMES categories: Famous names categories use words that are well known first or last names. This can be the names of famous people in a certain category, or the category can a common first name, where the words are all the last names. Example categories: TOMS, FAMOUS TONYS, or AMERICAN POETS

Here are the steps you must follow for you task
Step 1: You will be given 4 random words and write a short story in 4 sentences that incorporates these words.

Step 2: Reflect on your story and think of interesting categories that could be used for this category type based on some themes from your story. List 2 possible categories. These categories must be broad yet specific, encompassing a diverse set of words with a clear unifying theme. Your 2 categories must be thematically distinct from each other and match one of the types of categories above.

Step 3: For each category, describe in one sentence the connection between words in this category.

Step 4: For each category, list a diverse set of 8 words that can logically and truthfully fit in this category. Every word you list must have more than one meaning. Explain why each word belongs in this category. Do not use compound words, only use single words.
These words can be uncommon, but do not use any overly rare words. Try to keep them to the vocabulary of a high school student. Make sure the words you list are not overly specific to this category - they should be words that could fit in multiple categories.

Each word has to logically comply with the category on its own, without needing inference or additional words. For example, if the category is "BANDS", "kiss" would be a valid word, because the band "Kiss" exists. However, "door" would not be a valid word, because the band name is "The Doors", not just "door".
Please ensure that the categories and words are diverse in parts of speech, rarity, and how they relate to the category, and that they match the type of category given to you. 

Your response should be detailed, creative, and demonstrate lateral thinking to provide a diverse and engaging set of word categories.

Format your response like this:
Step 1:
<write your short story>
Step 2:
<your reflection on story to draw inspiration>
Possible Categories:
<category 1 name>
<category 2 name>
<category 3 name>

Steps 3 and 4:
Category 1:
[
    Category Name: <category 1 name>
    Connection: <connection between words in category 1>
    Diverse set of words:
    <word 1> - <word 1 reasoning>
    <word 2> - <word 2 reasoning>
    ...
]
Category 2:
[
    ...
]

Follow this format exactly, do not include any additional information or formatting
'''
propose_false_group_userprompt = '''Here are four words to build a short story from: {random_words}'''

propose_first_false_group_sysprompt = '''As an expert word puzzle creator for the New York Times, your task is to think of a common connection between words, and create a diverse pool of words that fit into this category. Here is a list of category "types" that you can create, with example categories for inspiration:

WORDPLAY categories: wordplay categories describe wordplay features that are present in all of the category's words. This can be related to how words are spelled, or how they are pronounced. Example categories: PALINDROMES, SPICES BEGINNING WITH "C", SILENT "L", or LETTER HOMOPHONES
NAMES OF THINGS categories: names of things categories contain proper noun words that describe things of a certain type. Example categories: FAST FOOD CHAINS, AIRLINES, or MICROSOFT PRODUCTS
SYNONYMS OR SLANG categories: In synonyms or slang categories, all the words all synonyms or slang terms for the same thing. Example categories: SYNONYMS FOR SELL, SYNONYMS FOR IGNITE, or SLANG FOR MONEY
FILL IN THE BLANK categories: Fill in the blank categories consist of one or two words and a blank space (represented by "___"). Every word in this category can replace the blank to create a well known phrase or name. Example categories: ___ MAN SUPERHEROES, ___ BABY, or SOUND ___
MEDIA REFERENCES categories: Media reference categories contain words that are all related to a specific form of media, such as music, literature, movies, and TV shows. It can be about character names, titles, or settings from well-known pop culture references. Example categories: VIDEO GAME CHARACTERS, TITLE MOVIE ANIMALS, or FAMOUS BROTHERS
COLORS categories: Color categories use a specific color as a central theme. The category may be related to objects that are typically this color, or different terms for shades of the color. Example categories: SHADES OF BLUE, THINGS THAT ARE RED, or SHADES OF GREEN
THINGS WITH ___ categories: Things with <blank> categories contain words that share a certain characteristic or feature. All of the words in this category are things that can be said to "have" that feature, in some way. Example categories: THINGS WITH KEYS, THINGS WITH WINGS, or THINGS WITH EYES
TYPES OF ___ categories: Types of <blank> categories lists a certain "thing" in the blank space.  All of the words in this category are specific versions or names of versions of that thing. Example categories: TYPES OF VEGETABLES, SNEAKER BRANDS, or HONDAS
FAMOUS NAMES categories: Famous names categories use words that are well known first or last names. This can be the names of famous people in a certain category, or the category can a common first name, where the words are all the last names. Example categories: TOMS, FAMOUS TONYS, or AMERICAN POETS

You will be given a pool of words, and an original category that connects them. Here are the steps of your task:

Step 1: Go through every word in the pool, and think creatively of any alternate meanings for the word that you can think of. For each alternate meaning, give the name of the category that would include this word under the alternate meaning. THE CATEGORY NAME MAY NOT CONTAIN THE WORD ITSELF. For example, if the word is "coffee", the category cannot be "types of coffee". 
Try to make a clever "Fill in the blank" category first, and then think of other categories if that isn't possible. The new category must be thematically distinct from the original category, and match one of the types of categories above. 

Step 2: Reflect on the categories you created for each word. Reason about which one would best contain a diverse set of words that are all connected to the category. Select the best category to build a new word pool from.

Step 3: For your selected category, list a diverse set of 8 words that can logically and truthfully fit in this category. Every word you list must have more than one meaning. Explain why each word belongs in this category. Use only single words, not compound words. You cannot include any words from the provided word pool.
Each word has to logically comply with the category on its own, without needing inference or additional words. For example, if the category is "BANDS", "kiss" would be a valid word, because the band "Kiss" exists. However, "door" would not be a valid word, because the band name is "The Doors", not just "door".
Please ensure that the words are diverse in parts of speech, rarity, and how they relate to the category, and that they match the type of category given to you.

Your response should be detailed, creative, and demonstrate lateral thinking to provide a diverse and engaging set of word categories.

Format your response like this:
[
    Step 1: Alternate Categories for Each Word:
    <word_1>: 
        - <alternate meaning 1>, <alternate category name>
        - <alternate meaning 2>, <alternate category name>
    ...
    <word_2>: 
        - <alternate meaning 1>, <alternate category name>
        - <alternate meaning 2>, <alternate category name>
    ...
    ...
    Step 2: Selecting the Best Alternate Category:
    <reasoning for selecting the most clever and diverse category>
    Category Name: <your selected alternate category name>
    Existing word used: <single word from the original pool>
    Connection: <sentence explaining the connection between words in this group>
    Step 3: Diverse word pool:
    <new word 1> - <why word 1 fits into this category>
    <new word 2> - <why word 1 fits into this category> ...
]


Here is an example. Do not use this example as your response:
Input:
{
Here is an existing word pool and category:
SHADES OF WHITE
The words in this category are all names for shades of the color white
Words in this category:
"EGGSHELL", "LINEN", "SNOW", "VANILLA"
}

Output:
{
Step 1: Alternate Categories for Each Word:
EGGSHELL: 
- An eggshell is the outer cover of an egg, PARTS OF AN EGG
- A common phrase is "walking on eggshells", THINGS YOU CAN WALK ON
LINEN:
- Linen is a type of fabric, TYPES OF FABRIC
- A linen closet is a term for a room that stores fabric in a home, TYPE OF CLOSET
SNOW:
- Filling in the blank, snow can combine with "cone" to create snow cone which is a popular frozen treat, ___ CONE
- Filling in the blank, snow can combine with "day" so create snow day, a day off from school or work, ___ DAY
- Snow is a type of weather or precipitation, TYPES OF WEATHER
VANILLA:
- vanilla can be a term to describe something ordinary or boring, SYNONYMS FOR PLAIN
- vanilla is a type of bean used for flavoring, TYPES OF BEANS

Step 2: Selecting the Best Alternate Category:
My proposed alternate categories are PARTS OF AN EGG, THINGS YOU CAN WALK ON, TYPES OF FABRIC, TYPE OF CLOSET, TYPE OF WEATHER, ___ CONE, ___ DAY, SYNONYMS FOR PLAIN, and TYPE OF BEAN.
Of these, I think that "TYPES OF BEANS" or "___ DAY" could be the most clever and diverse, because they use clever alternate definitions of the respective words. 
I will choose "___ DAY", because it's a fill in the blank category, and there are many words that complete the phrase, many of which have alternate meanings. This will provide a good challenge to the players, who may not think of these words in the context of the larger phrase

Category name: ___ DAY
Existing word used: SNOW
Connection: All words in this category are types of beans

Step 3: Diverse word pool:
SICK - a SICK DAY is a day off from work due to illness
SUN - SUN DAY is a day of the week, but SUN also has many other meanings
PAY - PAY DAY is the day you receive your paycheck
BIRTH - BIRTH DAY is the day you were born
OFF - an OFF DAY is a day when someone isn't performing up to their usual ability
MAY - MAY DAY is a holiday, but MAY is usually a month
MID  - MID DAY is the middle of the day, but MID also has other meanings
DOOMS - DOOMS DAY is the end of the world, and DOOMS is an uncommon word to see on its own
}'''
propose_first_false_group_userprompt  = '''Here is an existing word pool and category:
{category_name}
{connection_explanation}
Words in this category:
{word_pool}
'''
propose_followup_false_group_sysprompt = '''As an expert word puzzle creator for the New York Times, your task is to think of a common connection between words, and create a diverse pool of words that fit into this category. Here is a list of category "types" that you can create, with example categories for inspiration:

WORDPLAY categories: wordplay categories describe wordplay features that are present in all of the category's words. This can be related to how words are spelled, or how they are pronounced. Example categories: PALINDROMES, SPICES BEGINNING WITH "C", SILENT "L", or LETTER HOMOPHONES
NAMES OF THINGS categories: names of things categories contain proper noun words that describe things of a certain type. Example categories: FAST FOOD CHAINS, AIRLINES, or MICROSOFT PRODUCTS
SYNONYMS OR SLANG categories: In synonyms or slang categories, all the words all synonyms or slang terms for the same thing. Example categories: SYNONYMS FOR SELL, SYNONYMS FOR IGNITE, or SLANG FOR MONEY
FILL IN THE BLANK categories: Fill in the blank categories consist of one or two words and a blank space (represented by "___"). Every word in this category can replace the blank to create a well known phrase or name. Example categories: ___ MAN SUPERHEROES, ___ BABY, or SOUND ___
MEDIA REFERENCES categories: Media reference categories contain words that are all related to a specific form of media, such as music, literature, movies, and TV shows. It can be about character names, titles, or settings from well-known pop culture references. Example categories: VIDEO GAME CHARACTERS, TITLE MOVIE ANIMALS, or FAMOUS BROTHERS
COLORS categories: Color categories use a specific color as a central theme. The category may be related to objects that are typically this color, or different terms for shades of the color. Example categories: SHADES OF BLUE, THINGS THAT ARE RED, or SHADES OF GREEN
THINGS WITH ___ categories: Things with <blank> categories contain words that share a certain characteristic or feature. All of the words in this category are things that can be said to "have" that feature, in some way. Example categories: THINGS WITH KEYS, THINGS WITH WINGS, or THINGS WITH EYES
TYPES OF ___ categories: Types of <blank> categories lists a certain "thing" in the blank space.  All of the words in this category are specific versions or names of versions of that thing. Example categories: TYPES OF VEGETABLES, SNEAKER BRANDS, or HONDAS
FAMOUS NAMES categories: Famous names categories use words that are well known first or last names. This can be the names of famous people in a certain category, or the category can a common first name, where the words are all the last names. Example categories: TOMS, FAMOUS TONYS, or AMERICAN POETS

You will be a pool of "fixed" words, and the category that connects them. Your task is to think of a new and different category that could encompass one of the words from this pool, then create a new diverse pool of words that fit into your new category.

You will also be given some existing "used words" word groups, consisting of categories and a word pool, that are already in the word puzzle you are creating. You are not allowed to use any of these words when you are creating new word pools.

Step 1: Go through each word in the pool, and think creatively of any alternate meanings for the word that you can think of. For each alternate meaning, give the name of the category that would include this word under the alternate meaning. THE CATEGORY NAME MAY NOT CONTAIN THE WORD ITSELF. For example, if the word is "coffee", the category cannot be "types of coffee".
Try to make a clever "Fill in the blank" category first, and then think of other categories if that isn't possible. The new category must be thematically distinct from the original category, and match one of the types of categories above. 

Step 2: Reflect on the alternate categories you created for each word. Reason about which one could most likely cover a diverse and tricky set of words and be the most clever. Select the best category to build a new word pool from. At this stage, consider the "used words" pool. If any of your alternate categories could ALSO include, or seem to include a used word, select that one. This will create a good challenge for players.

Step 3: For your selected category, list a diverse set of 8 words that can logically and truthfully fit in this category. Every word you list must have more than one meaning. Explain why each word belongs in this category. Use only single words, not compound words. You cannot include any words from the "fixed" or ""used" word pools.
Each word has to logically comply with the category on its own, without needing inference or additional words. For example, if the category is "BANDS", "kiss" would be a valid word, because the band "Kiss" exists. However, "door" would not be a valid word, because the band name is "The Doors", not just "door".
Ensure that the words are diverse in parts of speech, rarity, and how they relate to the category, and that they match your category.

Your response should be detailed, creative, and demonstrate lateral thinking to provide a diverse and engaging set of word categories.

Format your response like this:
[
    Step 1: Alternate Categories for Each Word:
    <word_1>: 
        - <alternate meaning 1>, <alternate category name>
        - <alternate meaning 2>, <alternate category name>
    ...
    <word_2>: 
        - <alternate meaning 1>, <alternate category name>
        - <alternate meaning 2>, <alternate category name>
    ...
    ...
    Step 2: Selecting the Best Alternate Category:
    <reasoning for selecting the most clever and diverse category>
    Category Name: <your selected alternate category name>
    Existing word used: <word from the original pool>
    Connection: <sentence explaining the connection between words in this group>
    Step 3: Diverse word pool:
    <new word 1> - <why word 1 fits into this category>
    <new word 2> - <why word 1 fits into this category> ...
]


Here is an example. Do not use this example as your response:
Input:
{
Here is the fixed word pool and category:
SHADES OF WHITE
The words in this category are all names for shades of the color white
Words in this category:
"EGGSHELL", "CHAMPAGNE", "SNOW"

Here are the used words and categories:
TYPES OF BEANS: "VANILLA", "NAVY", "COFFEE", "STRING", "GREEN", "BLACK", "BUTTER", "BAKED", "LIMA"
}

Output:
{
Step 1: Alternate Categories for Each Word:
EGGSHELL: 
- An eggshell is the outer cover of an egg, PARTS OF AN EGG
- A common phrase is "walking on eggshells", THINGS YOU CAN WALK ON
CHAMPAGNE:
- Champagne is a bubbly alcoholic drink, DRINKS
- Champagne is commonly used at parties and celebrations, THINGS FOUND AT A PARTY
SNOW:
- Filling in the blank, snow can combine with "cone" to create snow cone which is a popular frozen treat, ___ CONE
- Filling in the blank, snow can combine with "day" so create snow day, a day off from school or work, ___ DAY
- Snow is a type of weather or precipitation, TYPES OF WEATHER


Step 2: Selecting the Best Alternate Category:
My proposed alternate categories are PARTS OF AN EGG, THINGS YOU CAN WALK ON, DRINKS, THINGS FOUND AT A PARTY, TYPE OF WEATHER, ___ CONE, and  ___ DAY
Looking at the used words, I can see two wrods that could fit in my alternate categories. COFFEE is also a DRINK, and GREEN can combine with DAY to create the band GREEN DAY. Because there is an overlapping word, and it's a fill in the blank category, I will select the alternate category ___ DAY.
There are many words that complete the phrase, many of which have alternate meanings. This will provide a good challenge to the players, who may not think of these words in the context of the larger phrase

Category name: ___ DAY
Existing word used: SNOW
Connection: All words in this category are types of beans

Step 3: Diverse word pool:
SICK - a SICK DAY is a day off from work due to illness
SUN - SUN DAY is a day of the week, but SUN also has many other meanings
PAY - PAY DAY is the day you receive your paycheck
BIRTH - BIRTH DAY is the day you were born
OFF - an OFF DAY is a day when someone isn't performing up to their usual ability
MAY - MAY DAY is a holiday, but MAY is usually a month
MID  - MID DAY is the middle of the day, but MID also has other meanings
DOOMS - DOOMS DAY is the end of the world, and DOOMS is an uncommon word to see on its own
}'''


propose_followup_false_group_userprompt  =  '''Here is the fixed word pool and category:
{category_name}
{connection_explanation}
Words in this category:
{false_word_pool}
Here are the used words:
{word_pool}
'''

############################################
#
#  False group prompts
#
############################################

propose_first_overlap_sysprompt = '''As an expert word puzzle creator for the New York Times, your task is to think of an interesting category and create a diverse pool of words that fit into this category. Here is a list of category "types" that you can create, with example categories for inspiration:

WORDPLAY categories: wordplay categories describe wordplay features that are present in all of the category's words. This can be related to how words are spelled, or how they are pronounced. Example categories: PALINDROMES, SPICES BEGINNING WITH "C", SILENT "L", or LETTER HOMOPHONES
NAMES OF THINGS categories: names of things categories contain proper noun words that describe things of a certain type. Example categories: FAST FOOD CHAINS, AIRLINES, or MICROSOFT PRODUCTS
SYNONYMS OR SLANG categories: In synonyms or slang categories, all the words all synonyms or slang terms for the same thing. Example categories: SYNONYMS FOR SELL, SYNONYMS FOR IGNITE, or SLANG FOR MONEY
FILL IN THE BLANK categories: Fill in the blank categories consist of one or two words and a blank space (represented by "___"). Every word in this category can replace the blank to create a well known phrase or name. Example categories: ___ MAN SUPERHEROES, ___ BABY, or SOUND ___
MEDIA REFERENCES categories: Media reference categories contain words that are all related to a specific form of media, such as music, literature, movies, and TV shows. It can be about character names, titles, or settings from well-known pop culture references. Example categories: VIDEO GAME CHARACTERS, TITLE MOVIE ANIMALS, or FAMOUS BROTHERS
COLORS categories: Color categories use a specific color as a central theme. The category may be related to objects that are typically this color, or different terms for shades of the color. Example categories: SHADES OF BLUE, THINGS THAT ARE RED, or SHADES OF GREEN
THINGS WITH ___ categories: Things with <blank> categories contain words that share a certain characteristic or feature. All of the words in this category are things that can be said to "have" that feature, in some way. Example categories: THINGS WITH KEYS, THINGS WITH WINGS, or THINGS WITH EYES
TYPES OF ___ categories: Types of <blank> categories lists a certain "thing" in the blank space.  All of the words in this category are specific versions or names of versions of that thing. Example categories: TYPES OF VEGETABLES, SNEAKER BRANDS, or HONDAS
FAMOUS NAMES categories: Famous names categories use words that are well known first or last names. This can be the names of famous people in a certain category, or the category can a common first name, where the words are all the last names. Example categories: TOMS, FAMOUS TONYS, or AMERICAN POETS

Step 1: You will be given 4 random words and write a short story in 4 sentences that incorporates these words.

Step 2: Reflect on your story and think of interesting categories that could be used for this category type based on some themes from your story. List 2 possible categories. These categories must be broad yet specific, encompassing a diverse set of words with a clear unifying theme. Your 2 categories must be thematically distinct from each other and match one of the types of categories above.

Step 3: For each category, describe in one sentence the connection between words in this category.

Step 4: For each category, list a diverse set of 8 words that can logically and truthfully fit in this category. Every word you list must have more than one meaning. Explain why each word belongs in this category. Do not use compound words, only use single words.

Please ensure that the categories and words are diverse in parts of speech, rarity, and how they relate to the category, and that they match the type of category given to you.

Your response should be detailed, creative, and demonstrate lateral thinking to provide a diverse and engaging set of word categories.

Format your response like this:
Step 1:
<write your short story>
Step 2:
<your reflection on story to draw inspiration>
Possible Categories:
<category 1 name>
<category 2 name>
<category 3 name>

Steps 3 and 4:
Category 1:
[
    Category Name: <category 1 name>
    Connection: <connection between words in category 1>
    Diverse set of words:
    <word 1> - <word 1 reasoning>
    <word 2> - <word 2 reasoning>
    ...
]
Category 2:
[
    ...
]
'''
propose_first_overlap_userprompt = '''Here are four words to build a short story from: {random_words}'''

propose_followup_overlap_sysprompt = '''As an expert word puzzle creator for the New York Times, your task is to think of a common connection between words, and create a diverse pool of words that fit into this category. Here is a list of category "types" that you can create, with example categories for inspiration:

WORDPLAY categories: wordplay categories describe wordplay features that are present in all of the category's words. This can be related to how words are spelled, or how they are pronounced. Example categories: PALINDROMES, SPICES BEGINNING WITH "C", SILENT "L", or LETTER HOMOPHONES
NAMES OF THINGS categories: names of things categories contain proper noun words that describe things of a certain type. Example categories: FAST FOOD CHAINS, AIRLINES, or MICROSOFT PRODUCTS
SYNONYMS OR SLANG categories: In synonyms or slang categories, all the words all synonyms or slang terms for the same thing. Example categories: SYNONYMS FOR SELL, SYNONYMS FOR IGNITE, or SLANG FOR MONEY
FILL IN THE BLANK categories: Fill in the blank categories consist of one or two words and a blank space (represented by "___"). Every word in this category can replace the blank to create a well known phrase or name. Example categories: ___ MAN SUPERHEROES, ___ BABY, or SOUND ___
MEDIA REFERENCES categories: Media reference categories contain words that are all related to a specific form of media, such as music, literature, movies, and TV shows. It can be about character names, titles, or settings from well-known pop culture references. Example categories: VIDEO GAME CHARACTERS, TITLE MOVIE ANIMALS, or FAMOUS BROTHERS
COLORS categories: Color categories use a specific color as a central theme. The category may be related to objects that are typically this color, or different terms for shades of the color. Example categories: SHADES OF BLUE, THINGS THAT ARE RED, or SHADES OF GREEN
THINGS WITH ___ categories: Things with <blank> categories contain words that share a certain characteristic or feature. All of the words in this category are things that can be said to "have" that feature, in some way. Example categories: THINGS WITH KEYS, THINGS WITH WINGS, or THINGS WITH EYES
TYPES OF ___ categories: Types of <blank> categories lists a certain "thing" in the blank space.  All of the words in this category are specific versions or names of versions of that thing. Example categories: TYPES OF VEGETABLES, SNEAKER BRANDS, or HONDAS
FAMOUS NAMES categories: Famous names categories use words that are well known first or last names. This can be the names of famous people in a certain category, or the category can a common first name, where the words are all the last names. Example categories: TOMS, FAMOUS TONYS, or AMERICAN POETS

You will first be given a category, a sentence explaining the category, and a pool of words that belong to that category. You will also be given a "type" of category to create. You must follow these steps:

Step 1:  Go through every word in the word pool for the provided category. List an alternate category this word could truthfully belong into, different from the provided category. These categories must be thematically distinct and match one of the types of categories above.
Focus on using alternate definitions of the word.

Step 2: Reflect on the alternate categories you created for each word. Reason about which one would encompass a diverse set of words and be the most clever. Select the best category to build a new word pool from.

Step 3: For your selected category, list a diverse set of 8 words that can logically and truthfully fit in this category. Every word you list must have more than one meaning. Explain why each word belongs in this category. Do not use compound words, only use single words. DO NOT use any words from the provided word pool.

Please ensure that the words are diverse in parts of speech, rarity, and how they relate to the category, and that they match the type of category given to you.

Your response should be detailed, creative, and demonstrate lateral thinking to provide a diverse and engaging set of word categories.

Format your response like this:
[
    Step 1: Alternate Categories for Each Word:
    <list each word and an alternate category for it>
    Step 2: Selecting the Best Alternate Category:
    <reasoning for selecting the most clever and diverse category>
    Category Name: <your selected alternate category name>
    Connection: <sentence explaining the connection between words in this group>
    Step 3: Diverse word pool:
    
    <word 1> - <word 1 reasoning>
    <word 2> - word 2 reasoning> ...
]'''
propose_followup_overlap_userprompt  = '''Here is an existing word group:
{category_name}
{connection_explanation}
Words in this category:
{word_pool}'''
propose_followup_overlap_userprompt_multiple  = '''Here are some existing word groups:
{category_names_explanations}
Words pool:
{word_pool}'''

###########################################
#
#  Editing prompts
#
############################################

category_edit_sysprompt = '''As the senior puzzle editor for the New York Times, you will be presented with a puzzle created by one of your junior puzzle creators for a word association game called "Connections". Your task is to edit the category names of the puzzle to improve it.

Connections puzzles consist of four groups of four words. Each word group has a category name, which describes what the common connection between the four words is

Puzzles will be presented in this format:

<CATEGORY_1>: "<WORD_1>", "<WORD_2>", ...
<CATEGORY_2>: "<WORD_5>", "<WORD_6>", ...
...


Category names must make sense and be truthful - it must accurately describe the exact connection between the four words. Category names should be as specific as possible. 

Go through each of the word groups of the puzzle, and perform the following steps. Think out loud at each step.

Step 1 - Look at the category name and the four words that belong to it. 
Step 2 - Go through each word. Think out loud for each word: "Is <word> a <category name>?". Answer yes or no. The word can only fit in the category if the answer is "yes" using that word alone. It can't fit when you assume there are additional words. For example, "SAN" is not a "CITY IN CALIFORNIA", because it's missing the DIEGO.
If the answer for a word is "no", make not of it and think of a category name that it WOULD fit in.
Step 3 - Rewrite the category name to be more specific, condensing it to 1 or 2 words while remaining truthful to the connection. 
Step 4 - Rewrite this category to be less specific, using 1 to 4 words, making it more general while still accurately encompassing all the terms in the group.
Step 5 - Decide whether the original category name, the more specific category name, or the more general category name is better for accurately and cleverly representing the connection between the words in this group

Finally, print out the puzzle with your changes. Include the explanation of the connection between the words after each group.
Format your final edited puzzle like this:
Final Puzzle:
[
<NEW_CATEGORY_1>: "<WORD_1>", "<WORD_2>", ...
<explanation for category 1>
<NEW_CATEGORY_2>: "<WORD_5>", "<WORD_6>", ...
<explanation for category 1>
...
]'''

category_edit_userprompt = '''{puzzle_string}'''

assign_difficulty_message_list = [{"role": "system", "content": '''You are an expert in word puzzles and wordplay. You are an expert in a new word game called "Connections".
Here is a tutorial of how the game "Connections" is played:
<
    You are given a grid of 16 words. Find four groups of four items that share something in common.
                                         
    Category examples:
        - FISH: Bass, Flounder, Salmon, Trout
        - FIRE ____: Ant, Drill, Island, Opal

    Categories will always be more specific than "5-LETTER WORDS", "NAMES", or "VERBS".
    Each puzzle only has one solution. Watch out for words that seem to belong to multiple categories!

    Each group is assigned a difficulty, which is revealed as you solve! Difficulty goes from "Most Straightforward" to "Tricky""
>

You will be presented with a full Connetions puzzle. The puzzle is composed of 4 word groups, which have a category and 4 words that belong to the category.
The word groups are given in a random order

Your task is analyze the word groups of the puzzle, and then rank them by difficulty.
 
First, go through each group and reason about how difficult they would be for a human to solve. The difficulty depends on how straightforward the connection between the four words is.

Then, list the puzzle's categories in order of increasing trickiness.

A straightforward word group is one where all four words have a simple theme connecting them. An example of a very straightfoward group is the word group COLORS: "RED", "GREEN', "BLUE", "ORANGE".
This is a straightforward group because the connection between the words is the first thing a player would think of when seeing the words. "RED", "GREEN", "BLUE", and "ORANGE" are most commonly words that refer to colors, so the category being "COLORS" is straightforward.

A tricky group is one where the connection between four words will take a lot of reasoning for a player to solve when seeing the words. An example of a trick group is SILENT 'W' WORDS: "ANSWER", "TWO", "WRIST", "WRONG".
This is a tricky group because it uses word play, and also does not deal with the most common definition of its words. The connection between the four words is not about their meaning, so this category is tricky.

Format your answer like this:
[
    <group category>: <group words>
    Reasoning: 
    <reason about how straightforward or tricky this group is>
                                  
    <group category>: <group words>
    Reasoning: 
    <reason about how straightforward or tricky this group is>
                                  
    ...

    Final reasoning:
    <Based on your reasoning, think about which group is the most straightforward, which group is most tricky, and which two groups fit inbetween>

    Ordered categories: <most straightforward group category>, <second most straightforward group category>, <second most tricky group category>, <trickiest group category>
]                         
'''},
{"role": "user", "content": '''
Rank this puzzle's word groups from most straightforward to trickiest:
 
NBA TEAMS: "BUCKS", "HEAT", "JAZZ", "NETS"
PALINDROMES: "KAYAK", "LEVEL", "MOM", "RACE CAR"
WET WEATHER: "HAIL", "RAIN", "SLEET", "SNOW"
KEYBOARD KEYS: "OPTION", "RETURN", "SHIFT", "TAB"'''},
{"role": "system", "content": '''
[
    NBA TEAMS: "BUCKS", "HEAT", "JAZZ", "NETS"
    Reasoning: 
    The connection between these words is that they are all the names of NBA teams. This group is a bit tricky, because it uses alternate defitions of its words. Instead of the normal definition of words like HEAT and NETS, the words are actually the names of NBA teams.
 
    PALINDROMES: "KAYAK", "LEVEL", "MOM", "RACE CAR"
    Reasoning: 
    The connection between these words is that they are all palindromes. This word group is very tricky, because it relies on wordplay, and it doesn't use the definitions of the words at all. Players must notice that all of the words are the same spelled forwards and backwards. This group is pretty tricky.
    
    WET WEATHER: "HAIL", "RAIN", "SLEET", "SNOW"
    Reasoning:  
    The connection between these words is that they are all types of wet weather. This group is straightforward, because it uses the most common definition of its words. For example, the most common use of the words RAIN and SNOW is to refer to a form of wet weather
    
    KEYBOARD KEYS: "OPTION", "RETURN", "SHIFT", "TAB"
    Reasoning: : 
    The connection between these words is that they are all the names of keyboard keys. This group is pretty tricky, because it uses niche alternate definitions of its words. "OPTION" and "RETURN" are not words that make people think of keyboards, so this group is pretty tricky to solve.

    Final reasoning:
    The most straightforward group in this puzzle is WET WEATHER, and the trickiest group is PALINDROMES because of the wordplay it uses. NBA TEAMS and KEYBOARD KEYS are both somewhat tricky. Of the two, I think that NBA TEAMS is more straightforward, because NBA team names are pretty well known, so it shouldn't be too hard for a player to connect those 4 words. So NBA TEAMS will be second, and KEYBOARD KEYS is third.

    Ordered categories: WET WEATHER, NBA TEAMS, KEYBOARD KEYS, PALINDROMES
]'''},
]
assign_difficulty_user_prompt = ''' Perfect. Here is a new puzzle. Rank this puzzle's word groups from most straightforward to trickiest:
{puzzle}
'''