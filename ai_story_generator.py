import openai
import os

def generate_story(prompt, model="gpt-3.5-turbo", max_tokens=500):
    """Generates a short story based on the given prompt using OpenAI's GPT model."""
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is set in environment variables
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": "You are a creative story writer."},
                      {"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error generating story: {e}"

if __name__ == "__main__":
    prompt = input("Enter a story prompt: ")
    story = generate_story(prompt)
    print("\nGenerated Story:\n")
    print(story)
