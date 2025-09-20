import json
from cerebras.cloud.sdk import Cerebras

answer_schema = {
  "type": "object",
  "properties": {
    "explanation": {
      "type": "string",
    },
    "quiz": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "question": {
            "type": "string",
          },
          "options": {
            "type": "array",
            "items": {
              "type": "string"
            },
          },
          "correct_option": {
            "type": "integer",
          }
        },
        "required": ["question", "options", "correct_option"],
        "additionalProperties": False
      }
    }
  },
  "required": ["explanation", "quiz"],
  "additionalProperties": False
}


def get_materials(subject, learner_type):
    client = Cerebras(
        api_key="csk-hfkh8thyvx8nm5h53fyd6rntwjy4k63dk25ppf28kx346ff8",
    )
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are an experienced professor of {subject} and student is a learner of type {learner_type}. Explain the topic in details with technical depth to a beginner according to the learner type: {learner_type} with examples. Dont give vague answers. Generate four questions with four options each on the given topic with slowly increasing difficulty."
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
            "name": "answer_schema",
            "strict": True,
            "schema": answer_schema  
        }
    }
    )
    return json.loads(completion.choices[0].message.content)

if __name__ == "__main__":
    print(json.dumps(get_materials('Dynamic Analysis Techniques', 'hands on'), indent=2))