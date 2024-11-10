import gym
from gym import spaces
import random
from transformers import pipeline
from stable_baselines3 import PPO
import pandas as pd

class ConnectionsEnv(gym.Env):
    def __init__(self, words, categories, prompt_file):
        super(ConnectionsEnv, self).__init__()
        self.words = words
        self.categories = categories
        self.lives = 4
        self.correct_guesses = 0
        self.done = False
        self.action_space = spaces.Discrete(len(words) // 4)
        self.observation_space = spaces.Box(low=0, high=1, shape=(len(words) + 1,), dtype=int)
        self.llm = pipeline("text-generation", model="gpt2")
        self.prompts = self.load_prompts(prompt_file)

    def load_prompts(self, file_path):
        with open(file_path, 'r') as file:
            prompts = file.read()
        return prompts

    def load_prompt(self, prompt_name):
        # Extract the specific prompt from the loaded prompts
        return self.prompts.split(prompt_name)[1].split("'''")[0].strip()

    def reset(self):
        self.lives = 4
        self.correct_guesses = 0
        self.done = False
        random.shuffle(self.words)
        return self._get_observation()

    def step(self, action):
        guessed_group = self.words[action * 4:(action + 1) * 4]
        correct_group = self._get_correct_group(guessed_group)

        if correct_group:
            self.correct_guesses += 1
            reward = 1
            done = self.correct_guesses == 4
            info = {"message": "Correct guess!"}
        else:
            self.lives -= 1
            reward = -1
            done = self.lives <= 0
            info = {"message": "Incorrect guess!"}

        return self._get_observation(), reward, done, info

    def _get_observation(self):
        return [1 if word in self.words else 0 for word in self.words] + [self.lives]

    def _get_correct_group(self, guessed_group):
        for category_words in self.categories.values():
            if set(guessed_group) == set(category_words):
                return True
        return False

    def render(self, mode='human'):
        print(f"Words: {self.words}, Lives: {self.lives}, Correct Groups: {self.correct_guesses}")

    def suggest_groupings(self):
        prompt = self.load_prompt("propose_false_group_sysprompt")  # Example of using a specific prompt
        # Convert all items in self.words to strings
        words_as_strings = [str(word) for word in self.words]
        formatted_prompt = prompt.format(random_words=', '.join(words_as_strings))
        response = self.llm(formatted_prompt, max_length=150, num_return_sequences=1)
        return response[0]['generated_text']

def load_words_and_categories(csv_file):
    df = pd.read_csv(csv_file)
    words = df['Word'].tolist()
    categories = {}
    for group in df['Group Name'].unique():
        categories[group] = df[df['Group Name'] == group]['Word'].tolist()
    return words, categories

# Example usage
csv_file_path = '/home/grads/g/ganatma/Research/Ganatma/TAMUDatathon24/Connections_Data.csv'  # Replace with your CSV file path
words, categories = load_words_and_categories(csv_file_path)

prompt_file_path = '/home/grads/g/ganatma/Research/Ganatma/TAMUDatathon24/prompts.py'  # Path to your prompts file
env = ConnectionsEnv(words, categories, prompt_file_path)

# Initialize the RL agent
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)

# Example of using the LLM to suggest groupings
suggested_groupings = env.suggest_groupings()
print("Suggested Groupings:", suggested_groupings)