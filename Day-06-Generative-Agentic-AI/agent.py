import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools.github_tool import get_github_repositories

user_query = input("You: ")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

client = genai.Client(api_key=api_key)
tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_github_repositories",
            description="Get public GitHub repositories for a given username.",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "username": types.Schema(
                        type="STRING",
                        description="The GitHub username."
                    )
                },
                required=["username"],
            ),
        )
    ]
)

print("Gemini client initialized")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_query,
    config=types.GenerateContentConfig(
        tools=[tool]
    )
)

function_call = response.candidates[0].content.parts[0].function_call

if not function_call:
    print("Gemini did not request a tool.")
    print(response.text)
    exit()


result = get_github_repositories(
    function_call.args["username"]
)

print("Tool result:")
print(result)

tool_response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        user_query,
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"repositories": result},
                )
            ],
        ),
    ],
)

print("Final response:")
print(tool_response.text)

print("Tool requested:", function_call.name)
print("Arguments:", function_call.args)