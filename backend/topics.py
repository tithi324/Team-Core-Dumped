import json
from cerebras.cloud.sdk import Cerebras

topic_schema = {
    "type": "object",
    "properties": {
        "topics": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["topics"],
    "additionalProperties": False
}




def get_topics(subject):
    client = Cerebras(
        api_key="csk-hfkh8thyvx8nm5h53fyd6rntwjy4k63dk25ppf28kx346ff8",
    )
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an experienced guide who tells about the topics to learn to master any subject step by step in the simplest way possible. You only give the topic names."
            },
            {
                "role": "user",
                "content": f"I want to learn about {subject}",
            } 
        ],
        model="llama-4-scout-17b-16e-instruct",
        response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "topic_schema",
            "strict": True,
            "schema": topic_schema  
        }
    }
    )
    return json.loads(completion.choices[0].message.content)['topics']

if __name__ == '__main__':
    for topic in get_topics("reverse engineering"):
        print(f"{type(topic)} {topic}")
    