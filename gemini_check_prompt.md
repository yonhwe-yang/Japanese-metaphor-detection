prompt = """あなたは認知言語学の専門家です。前段のモデル(Qwen)の判定を【検証】し、最終的な比喩分析を行ってください。
    #Example:
    1.Input Text: "昨日、新しい車を買った。"
    Qwen Hint: {{"metaphor": true, "trigger_words": ["买った"]}}
    Output: {{"metaphor": false, "reason": "単なる事実描写です。"}}
    2.Input: "人生は旅だ。"
    Qwen Hint: {{"has_metaphor": true, "trigger_words": ["人生","旅"]}}
    Output: {"is_metaphor": true, "source": "旅", "target": "人生"}
    
    要件：
1. 比喩かどうかを厳密に判断
2. 比喩表現を特定
3. source domain（源領域）
4. target domain（目標領域）
※必ずJSONで出力
※テキストにはメタファーが複数含まれている可能性がある
※簡潔に


    """