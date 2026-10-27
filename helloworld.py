import eztraink as ezk

#hello world program
#ASK A MODEL WITH << 
agent1=ezk.model("anthropic//claude_fable_5_1")#model can be named
answer=agent1<<"what is rag" #answers can be stored
print(answer)#answers can be printed diretly or from the varible that they are stored in

#TEXT IS JOINED BEFORE SENDING IT TO THE MODEL SO YOU CAN USE + to concatenate
topic="vector databases"
answer1=agent1<<"what is rag"+topic+"explain to a beginner")

#settings for every version
agent1=ezk.model("anthropic//fable_5_1",temp=0.2,max_tok=5000)

#settings for a sigle question
answer=agent1(temp=0.2,max_tok=5000)<<"explain llms in short"

