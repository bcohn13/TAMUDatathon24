import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from accelerate import Accelerator

class WordGroupDataset(Dataset):
    """Custom dataset for word groups and their contexts"""
    def __init__(self, word_groups, contexts, tokenizer, max_length=128):
        self.tokenizer = tokenizer
        self.inputs = []
        
        for words, context in zip(word_groups, contexts):
            # Input prompt asks to find the context
            input_text = f"The words {', '.join(words)} are related because they share the context of?"
            # Target completion includes the context
            target_text = context
            
            # Encode both input and target
            input_encoding = tokenizer(input_text,
                                       truncation=True,
                                       max_length=max_length,
                                       padding="max_length",
                                       return_tensors="pt")
            
            target_encoding = tokenizer(target_text,
                                        truncation=True,
                                        max_length=max_length,
                                        padding="max_length",
                                        return_tensors="pt")
            
            self.inputs.append({
                'input_ids': input_encoding['input_ids'].squeeze(),
                'attention_mask': input_encoding['attention_mask'].squeeze(),
                'labels': target_encoding['input_ids'].squeeze()
            })
    
    def __len__(self):
        return len(self.inputs)
    
    def __getitem__(self, idx):
        return self.inputs[idx]

def fine_tune_gpt2(data, model_name='gpt2', output_dir='./fine_tuned_gpt2', num_epochs=2, batch_size=8):
    """
    Fine-tune GPT2 using Accelerate
    """
    accelerator = Accelerator()
    
    # Load model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Add padding token
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id
    
    # Prepare dataset
    word_groups = [entry['words'] for entry in data]
    contexts = [entry['context'] for entry in data]
    dataset = WordGroupDataset(word_groups, contexts, tokenizer)
    
    # Create data loader
    train_dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    # Prepare optimizer
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
    
    # Prepare model, optimizer, and dataloader with accelerator
    model, optimizer, train_dataloader = accelerator.prepare(model, optimizer, train_dataloader)
    
    # Training loop
    print("\nStarting fine-tuning...")
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        
        for batch_idx, batch in enumerate(train_dataloader):
            optimizer.zero_grad()
            
            outputs = model(
                input_ids=batch['input_ids'],
                attention_mask=batch['attention_mask'],
                labels=batch['labels']
            )
            
            loss = outputs.loss
            accelerator.backward(loss)
            optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 10 == 0:
                print(f"Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}, Loss: {loss.item():.4f}")
        
        avg_loss = total_loss / len(train_dataloader)
        print(f"Epoch {epoch+1}/{num_epochs}, Average Loss: {avg_loss:.4f}")
    
    # Save the model
    accelerator.wait_for_everyone()
    unwrapped_model = accelerator.unwrap_model(model)
    unwrapped_model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model saved to {output_dir}")

def get_fine_tuned_similarity(group, model, tokenizer, device):
    """
    Get context similarity using fine-tuned model
    """
    model.eval()
    
    # Create prompt
    prompt = f"The words {', '.join(group)} are related because they share the context of?"
    
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    # Generate context prediction
    with torch.no_grad():
        generated = model.generate(
            inputs['input_ids'],
            max_length=len(inputs['input_ids'][0]) + 20,
            num_return_sequences=1,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True
        )
        
        # Decode the generated text
        predicted_context = tokenizer.decode(
            generated[0][len(inputs['input_ids'][0]):],
            skip_special_tokens=True
        )
        
        # Calculate similarity score (you can adjust this logic)
        score = 1.0 if predicted_context else 0.0  # Placeholder for actual similarity logic
        
        return {
            'predicted_context': predicted_context,
            'score': score
        }

def process_connections_data(csv_path):
    """
    Process Connections CSV data into training format for GPT-2
    """
    df = pd.read_csv(csv_path)
    training_data = []
    
    for _, game_group in df.groupby('Game ID'):
        word_groups = {}
        
        for _, row in game_group.iterrows():
            group_name = str(row['Group Name'])
            word = str(row['Word'])
            
            if group_name not in word_groups:
                word_groups[group_name] = []
            word_groups[group_name].append(word)
        
        for group_name, words in word_groups.items():
            if len(words) == 4:
                training_data.append({
                    'words': [str(w) for w in words],
                    'context': str(group_name).lower()
                })
    
    return training_data

# Example usage
if __name__ == "__main__":
    # Load your dataset
    training_data = process_connections_data('/home/grads/g/ganatma/Research/Ganatma/TAMUDatathon24/Connections_Data.csv')
    
    # Fine-tune model
    fine_tune_gpt2(training_data)
    
    # Load the fine-tuned model for testing
    tokenizer = GPT2Tokenizer.from_pretrained('./fine_tuned_gpt2')
    model = GPT2LMHeadModel.from_pretrained('./fine_tuned_gpt2')
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)
    
    # Test the model
    test_group = ['piano', 'violin', 'cello', 'harp']
    result = get_fine_tuned_similarity(test_group, model, tokenizer, device)
    
    print("\nTest Results:")
    print(f"Group: {', '.join(test_group)}")
    print(f"Predicted Context: {result['predicted_context']}")
    print(f"Similarity Score: {result['score']:.3f}")