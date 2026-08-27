from langchain_core.prompts import PromptTemplate

while True:

    choice = input("Do you want to run Y/N: ")

    if choice.strip().lower() == "y":

        topic = input("Enter Topic: ")
        subject = input("Enter Subject: ")
        level = input("Enter Level: ")
        experience = input("Enter Experience: ")

        # Prompt 1
        template1 = PromptTemplate(
            input_variables=["topic"],
            template="Explain {topic} in simple English."
        )
        print("\nPrompt 1:")
        print(template1.format(topic=topic))

        # Prompt 2
        template2 = PromptTemplate(
            input_variables=["topic", "level"],
            template="Explain {topic} for a {level} learner."
        )
        print("\nPrompt 2:")
        print(template2.format(topic=topic, level=level))

        # Prompt 3
        template3 = PromptTemplate(
            input_variables=["topic"],
            template="Explain {topic} with real-world examples."
        )
        print("\nPrompt 3:")
        print(template3.format(topic=topic))

        # Prompt 4
        template4 = PromptTemplate(
            input_variables=["topic"],
            template="Explain the advantages and disadvantages of {topic}."
        )
        print("\nPrompt 4:")
        print(template4.format(topic=topic))

        # Prompt 5
        template5 = PromptTemplate(
            input_variables=["topic"],
            template="Compare {topic} with a artificial intelligence concept."
        )
        print("\nPrompt 5:")
        print(template5.format(topic=topic))

        # Prompt 6
        template6 = PromptTemplate(
            input_variables=["topic"],
            template="Explain {topic} step by step."
        )
        print("\nPrompt 6:")
        print(template6.format(topic=topic))

        # Prompt 7
        template7 = PromptTemplate(
            input_variables=["topic"],
            template="Give 5 important facts about {topic}."
        )
        print("\nPrompt 7:")
        print(template7.format(topic=topic))

        # Prompt 8
        template8 = PromptTemplate(
            input_variables=["topic"],
            template="Explain the importance of {topic}."
        )
        print("\nPrompt 8:")
        print(template8.format(topic=topic))

        # Prompt 9
        template9 = PromptTemplate(
            input_variables=["topic"],
            template="Give 5 real-world applications of {topic}."
        )
        print("\nPrompt 9:")
        print(template9.format(topic=topic))

        # Prompt 10
        template10 = PromptTemplate(
            input_variables=["topic"],
            template="Create a quiz about {topic}."
        )
        print("\nPrompt 10:")
        print(template10.format(topic=topic))

        # Prompt 11
        template11 = PromptTemplate(
            input_variables=["topic"],
            template="Write a short essay about {topic}."
        )
        print("\nPrompt 11:")
        print(template11.format(topic=topic))

        # Prompt 12
        template12 = PromptTemplate(
            input_variables=["topic"],
            template="Summarize {topic} in 5 bullet points."
        )
        print("\nPrompt 12:")
        print(template12.format(topic=topic))

        # Prompt 13
        template13 = PromptTemplate(
            input_variables=["topic"],
            template="Explain the history of {topic}."
        )
        print("\nPrompt 13:")
        print(template13.format(topic=topic))

        # Prompt 14
        template14 = PromptTemplate(
            input_variables=["topic"],
            template="Act as an expert and explain {topic}."
        )
        print("\nPrompt 14:")
        print(template14.format(topic=topic))

        # Prompt 15
        template15 = PromptTemplate(
            input_variables=["topic"],
            template="Explain common mistakes in {topic}."
        )
        print("\nPrompt 15:")
        print(template15.format(topic=topic))

        # Prompt 16
        template16 = PromptTemplate(
            input_variables=["topic"],
            template="Give a step-by-step guide to learn {topic}."
        )
        print("\nPrompt 16:")
        print(template16.format(topic=topic))

        # Prompt 17
        template17 = PromptTemplate(
            input_variables=["topic"],
            template="Explain the future of {topic}."
        )
        print("\nPrompt 17:")
        print(template17.format(topic=topic))

        # Prompt 18
        template18 = PromptTemplate(
            input_variables=["topic"],
            template="Create interview questions about {topic}."
        )
        print("\nPrompt 18:")
        print(template18.format(topic=topic))

        # Prompt 19
        template19 = PromptTemplate(
            input_variables=["topic", "subject"],
            template="Act as a subject matter expert in {subject} and explain {topic}."
        )
        print("\nPrompt 19:")
        print(template19.format(topic=topic, subject=subject))

        # Prompt 20
        template20 = PromptTemplate(
            input_variables=["topic", "experience", "subject", "level"],
            template="Act as a subject matter expert with {experience} years of experience in {subject}. Explain {topic} for a {level} learner."
        )
        print("\nPrompt 20:")
        print(template20.format(
            topic=topic,
            experience=experience,
            subject=subject,
            level=level
        ))

        print("\n====================================")

    else:
        print("You exited.")
        break