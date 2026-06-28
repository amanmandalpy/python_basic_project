def quiz_game():

    questions = [
        {
            "question": "Who developed Python?",
            "options": ["a) James Gosling",
                        "b) Guido van Rossum",
                        "c) Dennis Ritchie",
                        "d) Bjarne Stroustrup"],
            "answer": "b"
        },

        {
            "question": "Which keyword is used to define a function?",
            "options": ["a) function",
                        "b) define",
                        "c) def",
                        "d) func"],
            "answer": "c"
        },

        {
            "question": "Which data type is mutable?",
            "options": ["a) Tuple",
                        "b) String",
                        "c) List",
                        "d) Integer"],
            "answer": "c"
        },

        {
            "question": "Which loop is used to iterate over a sequence?",
            "options": ["a) if",
                        "b) while",
                        "c) for",
                        "d) switch"],
            "answer": "c"
        },

        {
            "question": "Which symbol is used for comments?",
            "options": ["a) //",
                        "b) #",
                        "c) /* */",
                        "d) --"],
            "answer": "b"
        }
    ]

    score = 0

    print("\n******** Welcome to Python Quiz ********\n")

    for i, q in enumerate(questions, start=1):

        print(f"Q{i}. {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("\nEnter your answer: ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

        print("-" * 40)

    print("\nQuiz Finished\n")
    print("Correct Answers :", score)
    print("Wrong Answers   :", len(questions) - score)
    print("Score           :", score * 10, "/", len(questions) * 10)


quiz_game()