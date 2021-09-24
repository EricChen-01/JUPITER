import openai
openai.api_key = "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"

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="ada", prompt="to be or not to be.")

# print the completion
print(completion.choices[0].text)