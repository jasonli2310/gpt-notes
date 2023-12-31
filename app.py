import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))

def index():
    if request.method == "POST":
        listOfNotes = request.form["listOfNotes"]

        functions = [
            {
                "name": "create_note",
                "description": "adds a note with attributes to a database",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "noteName":{
                            "type": "string",
                            "description": "a note/task that the user "
                        },
                        "noteCategory":{
                            "type": "string",
                            "description": "category of note/task"
                        }
                    },
                    "required": ["noteName", "noteCategory"],

                }
            }
        ]

    #     functions = [
    #     {
    #         "name": "get_current_weather",
    #         "description": "Get the current weather in a given location",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "location": {
    #                     "type": "string",
    #                     "description": "The city and state, e.g. San Francisco, CA",
    #                 },
    #                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    #             },
    #             "required": ["location"],
    #         },
    #     }
    # ]

        baseContent = "Please help me categorize this note: " + listOfNotes

        systemContent = "You are a helpful assistant whose job is to organize and categorize notes and tasks so they can be more actionable. I am a 26 year old who is looking to organize my life. One problem is that throughout my day, I get think of things I want to read about or learn about, but I don't have the time to do it at that moment. I don't want to forget about it, so my instinct is to write it down somewhere. But I know it's also going to be difficult to organize. Therefore, I want to give you a list of my notes, and I want. you to help me group it and organize it so I can access it better when I have time to read/learn about it."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            functions = functions,
            messages = [
                {"role": "system", "content": systemContent},
                {"role": "user", "content": baseContent}
            ],
            temperature = 0.2
        )
        return redirect(url_for("index", result=response.choices[0].message))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def createCategorizedList (jsonList):











def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

