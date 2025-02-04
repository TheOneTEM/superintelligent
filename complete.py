import requests


class Complete:
    def __init__(self, api_key, model="j1-jumbo"):
        self.key = api_key
        self.model = model

    def predict(
        self,
        prompt,
        numResults=1,
        maxTokens=8,
        stopSequences=[],
        topKReturn=0,
        temperature=0.0,
    ):
        response = requests.post(
            f"https://api.ai21.com/studio/v1/{self.model}/complete",
            headers={"Authorization": f"Bearer {self.key}"},
            json={
                "prompt": prompt,
                "numResults": numResults,
                "maxTokens": maxTokens,
                "stopSequences": stopSequences,
                "topKReturn": topKReturn,
                "temperature": temperature,
            },
        )
        return response.json()

    def complete(self, prompt, **kwargs):
        return self.predict(prompt, **kwargs)["completions"][0]["data"]["text"]