# 恐らくのファイル構成
https://github.com/thunlp/ChatEval/tree/main/agentverse
- agentverse/
    - agents/
        - 1つのAgentのステップをモデル化している
        - base.py
            - アブストラクトメソッドで定義されている
            - BaseAgent(BaseModel)
                - step
                - astep
                - reset
                - add_message_to_memory
                - get_receiver
                - set_receiver
                - add_receiver
                - remove_receiver
        - 
    - environments/
        - rules/
        - 1度の会議全体を管理している気がする
        - base.py
            - args
                """
                Base class for environment.

                Args:
                    agents: List of agents
                    rule: Rule for the environment
                    max_turns: Maximum number of turns
                    cnt_turn: Current turn number
                    last_messages: Messages from last turn
                    rule_params: Variables set by the rule
                """
            - step
            - reset
            - is_done
        - llm_eval.py
            - step()
                - agentのインデックスを取得
                - 現在の環境の表現を取得？(プロンプトか？)
                - asyncio.gather()で全エージェントから次のメッセージを取得
                - ルールに従ってメッセージを選択
                - ruleに従い，記憶を更新
                - visible__agentを更新？
                - ターン値を更新
    - llms/
        - GPT
    - memory/
        - 恐らく各エージェントの記憶に関するもの

    - memory_manipulator/
    - tasks/
    <!--  -->
    - agentverse.py
    - initialization.py
    - message.py
        ```python
        class Message(BaseModel):
            content: str = Field(default="")
            sender: str = Field(default="")
            receiver: Set[str] = Field(default=set({"all"}))
            tool_response: List[Tuple[AgentAction, str]] = Field(default=[])
        ```
    - parser.py
    - registry.py
    - utils.py
    
- main.py


- 議論の流れ
    - A1, A2 の2人でどうやって議論を進めさせるか
    - 完成形
        - A1: 
        - A2: 
        - A1: 
        - A2: 
    - 実装上は
        - T1
            - A1:
            - A2: 
        - T2
            - A1: 
            - A2: