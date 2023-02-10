import openai

#OpenAI API key
openai.api_key = "INSERT API KEY HERE"

#Function for OpenAI prompts / responses
def generate_response(prompt):
    completion=openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.6,)
    message= completion.choices[0].text
    
    return message
