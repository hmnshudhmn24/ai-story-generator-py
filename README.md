# AI Story Generator

## Overview
The **AI Story Generator** creates short stories based on user-provided prompts using OpenAI's GPT model. It leverages **natural language processing** to generate engaging and creative stories.

## Features
- Accepts a user-provided story prompt.
- Uses OpenAI's GPT model to generate a unique short story.
- Can be customized with different models and max token limits.

## Requirements
Ensure you have Python installed along with the following dependencies:
```
openai
```
Install the required dependency using:
```
pip install openai
```

## API Setup
1. Sign up at OpenAI and get an API key.
2. Set up the API key as an environment variable:
```
export OPENAI_API_KEY="your-api-key-here"
```

## Usage
1. Run the script:
```
python ai_story_generator.py
```
2. Enter a story prompt when prompted.
3. The generated story will be displayed.

## Example Input
```
Enter a story prompt: A lost astronaut discovers an ancient civilization on Mars.
```

## Example Output
```
Generated Story:
As the astronaut wandered through the Martian valleys, strange symbols began to appear on the rocks...
```

## Notes
- Ensure you have a valid OpenAI API key before running the script.
- Modify the `max_tokens` parameter for longer or shorter stories.

## License
This project is open-source and free to use for educational and personal purposes.
